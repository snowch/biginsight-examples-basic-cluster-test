*********************************************************************
### README
*********************************************************************

This project contains sample scripts  to help you quickly get started with BigInsights. Following the steps below on your client machine, it should take you about 10 mins to perform any of the following actions programmatically against a BigInsights cluster. These scripts are tested on BigInsights on Cloud (bluemix) but they should also work for BigInsights on-premise.

The core idea is that you can run one of the example projects to see it working against your BigInsights cluster. You can then copy the project to your environment and adapt it to add your own custom logic.  Think of the example projects as working blueprints.

A design decision was taken that the build scripts should be as independent as possible to allow developers to take a standalone example script project and reuse it with minimal effort.  A side effect of this design decision is that there is some duplicated code in the example projects.

*********************************************************************

### Pre-requisites

- Java 7 or 8 installed and JAVA_HOME environment variable set
- You do NOT need to install gradle, the gradlew scripts will setup gradle for you


### Setup Instructions

- Clone this repository `git clone https://github.com/snowch/biginsight-examples.git`
- Copy `connection.properties_template` to `connection.properties`
- Edit `connection.properties` to add your BigInsights instance hostname and credentials
- Export the cluster certificate from your browser. The following steps apply to Firefox:
  - Click the lock icon in your browser's address bar.
  - Click More Information and then View Certificate on the Security page.
  - In the Certificate Viewer, select the Details tab and then click Export.
  - Save the certificate in this folder with the filename `certificate`
  - See [./certificate_template](./certificate_template) for an example certificate
- Ssh into the BigInsights cluster 'mastermanager' node to install the cluster's SSL certificate into ./ssh/known_hosts
- Ssh into the BigInsights cluster 'master-2' node to install the cluster's SSL certificate into ./ssh/known_hosts

*********************************************************************
### Running the scripts

See the README.md file in each example in the [[examples](examples)] folder for instructions how to run the script.
*********************************************************************

### Quick Links

Running `./gradlew` from the top level folder will print some key links, e.g.:

```
$ ./gradlew
--------------------------------------------------------------------------------------------------------------------------------------
                                                       CLUSTER DETAILS
--------------------------------------------------------------------------------------------------------------------------------------
Ambari URL         ::      https://ehaasp-12345-mastermanager.bi.services.bluemix.net:9443/
BigInsights URL    ::      https://ehaasp-12345-mastermanager.bi.services.bluemix.net:8443/gateway/default/BigInsightsWeb/index.html
YARN URL           ::      https://ehaasp-12345-mastermanager.bi.services.bluemix.net:8443/gateway/yarnui/yarn/apps
Master Mgr SSH URL ::      ssh://biadmin:@ehaasp-12345-mastermanager.bi.services.bluemix.net
Master 2   SSH URL ::      ssh://biadmin:@ehaasp-12345-master-2.bi.services.bluemix.net
--------------------------------------------------------------------------------------------------------------------------------------
```
