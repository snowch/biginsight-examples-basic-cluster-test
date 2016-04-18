#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function

import re
import sys
from operator import add

from pyspark import SparkContext
from pyspark.sql import SQLContext

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: exporttoswift <license file> <project id> <username> <password> <service> <container>", file=sys.stderr)
        exit(-1)

    license_filename = sys.argv[1]
    project_id       = sys.argv[2]
    username         = sys.argv[3]
    password         = sys.argv[4]
    service_name     = sys.argv[5]
    container        = sys.argv[6]

    sc = SparkContext()

    prefix = "fs.swift2d.service." + service_name

    sc._jsc.hadoopConfiguration().set("fs.swift2d.impl","com.ibm.stocator.fs.ObjectStoreFileSystem")

    sc._jsc.hadoopConfiguration().set(prefix + ".auth.url",     "https://identity.open.softlayer.com/v3/auth/tokens")
    sc._jsc.hadoopConfiguration().set(prefix + ".public",       "true")
    sc._jsc.hadoopConfiguration().set(prefix + ".tenant",       project_id)
    sc._jsc.hadoopConfiguration().set(prefix + ".password",     password)
    sc._jsc.hadoopConfiguration().set(prefix + ".username",     username)
    sc._jsc.hadoopConfiguration().set(prefix + ".auth.method", "keystoneV3")
    sc._jsc.hadoopConfiguration().set(prefix + ".region",      "dallas")

    sqlContext = SQLContext(sc)

    # read file from HDFS
    lines = sc.textFile(license_filename, 1)
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add) \
                  .filter(lambda x: x[0].isalnum())

    # Create a sql dataframe from the counts dataframe
    hhdf = sqlContext.createDataFrame(counts,['letter', 'count'])

    # destination url
    swift_file_url = "swift2d://{0}.{1}/counts".format(container, service_name)

    print('*' * 80)
    print(swift_file_url)
    print('*' * 80)

    # save to swift
    counts.saveAsTextFile(swift_file_url)

    sc.stop()
