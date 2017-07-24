#!/bin/bash
rm -R sites.sql
rm -R python.db
python fillDB.py
sqlite3 python.db < sites.sql
sudo chmod a+rw python.db
