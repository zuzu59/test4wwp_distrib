import os
import errno
import csv
try:
    origin = open('urls.csv')
    output = open('sites.sql', 'w')
    reader = csv.reader(origin)
    i=0
    output.write("PRAGMA foreign_keys=OFF;\nBEGIN TRANSACTION;\nCREATE TABLE sites(ID SERIAL PRIMARY KEY NOT NULL,"
		+"JAHIA TEXT,WORDPRESS TEXT,STATUS TEXT,DATE DATETIME);\n")
    for row in reader:
    	output.write('INSERT INTO "sites" VALUES(' + str(i) + ', "'+ row[0] + '", "' + row[1]+ '", NULL, NULL);\n')
        i+=1
    output.write("COMMIT;")
    output.close()
    origin.close()
except IOError as ioex:
    print ('No credentials')
