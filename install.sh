#!/bin/bash
sudo apt-get install python-pip
sudo pip2 install web.py
sudo apt-get install sqlite3
sqlite3 python.db < sites.sql
