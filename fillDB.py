import os
import errno
import csv
try:
    # Insert urls
    credentials = open('../credentials/credentials.csv')
    output = open('sites.sql', 'w')
    reader = csv.reader(credentials)
    i=0
    output.write("PRAGMA foreign_keys=OFF;\nBEGIN TRANSACTION;\nCREATE TABLE sites(ID SERIAL PRIMARY KEY NOT NULL,"
		+"JAHIA TEXT,WORDPRESS TEXT,STATUS TEXT,USER_ID INT, DATE DATETIME);\n")
    next(reader)
    for row in reader:
    	output.write('INSERT INTO "sites" VALUES(' + str(i) + ', "'+ row[2] + '", "' + row[3]+ '", NULL, NULL, NULL);\n')
        i+=1
    credentials.close()

    # Insert users
    users = open('users.csv')
    reader = csv.reader(users)
    output.write("CREATE TABLE users (ID SERIAL PRIMARY KEY NOT NULL, NAME TEXT);")
    i = 0
    next(reader)
    for row in reader:
        if row[1] :
            output.write('INSERT INTO "users" VALUES(' + row[0] + ',"' + row[1] + ' ' + row[2] +'");')  
            i += 1
    output.write("COMMIT;")
    output.close()
except IOError as ioex:
    print ('No credentials')
