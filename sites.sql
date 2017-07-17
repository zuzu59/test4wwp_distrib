PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE sites(
ID SERIAL PRIMARY KEY NOT NULL,
JAHYA TEXT,
WORDPRESS TEXT,
STATUS TEXT);
INSERT INTO "sites" VALUES(0,'http://brisken-lab.epfl.ch','http://10.92.104.248:8081/test-web-wordpress.epfl.ch/v1-testwp/briskenlab.html',NULL);
INSERT INTO "sites" VALUES(1,'http://gr-co.epfl.ch','http://10.92.104.248:8081/test-web-wordpress.epfl.ch/v1-testwp/gr-co.html',NULL);
INSERT INTO "sites" VALUES(2,'http://lanes.epfl.ch','http://10.92.104.248:8081/test-web-wordpress.epfl.ch/v1-testwp/lanes.html',NULL);
INSERT INTO "sites" VALUES(3,'http://ccc.epfl.ch','http://10.92.104.248:8081/test-web-wordpress.epfl.ch/v1-testwp/lcr.html',NULL);
INSERT INTO "sites" VALUES(4,'http://mathgeom.epfl.ch','http://10.92.104.248:8081/test-web-wordpress.epfl.ch/v1-testwp/mathgeom.html',NULL);
INSERT INTO "sites" VALUES(5,'http://mmspg.epfl.ch','http://10.92.104.248:8081/test-web-wordpress.epfl.ch/v1-testwp/mmspl.html',NULL);
INSERT INTO "sites" VALUES(6,'http://rdsg.epfl.ch/','http://10.92.104.248:8081/test-web-wordpress.epfl.ch/v1-testwp/rdsg.html',NULL);
INSERT INTO "sites" VALUES(7,'http://leure.epfl.ch','http://10.92.104.248:8081/test-web-wordpress.epfl.ch/v1-testwp/reme.html',NULL);
INSERT INTO "sites" VALUES(8,'http://scc.epfl.ch/page-22910-fr.html','http://10.92.104.248:8081/test-web-wordpress.epfl.ch/v1-testwp/sbsst.html',NULL);
COMMIT;
