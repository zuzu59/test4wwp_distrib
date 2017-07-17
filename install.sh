#!/bin/bash
sudo apt-get install python-pip
export LC_ALL=C
sudo pip2 install web.py
sudo apt-get install sqlite3
sqlite3 python.db < sites.sql
sudo chmod a+rw python.db
