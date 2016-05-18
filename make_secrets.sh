#!/bin/bash

tar cf secrets.tar connection.properties certificate downloads/db2jcc*.jar
travis encrypt-file secrets.tar
