#!/bin/bash

sudo echo "RUNNING Startup SCRIPT" && date
sudo date >> startlog.txt
node-red-pi >> startlog.txt 
