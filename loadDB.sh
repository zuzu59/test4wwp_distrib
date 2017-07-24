#!/bin/bash
python fillDB.py
sqlite3 python.db < sites.sql
sudo chmod a+rw python.db