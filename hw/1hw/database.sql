/* Taken from https://www.chegg.com/homework-help/questions-and-answers/create-tables-described-sample-data-write-sql-queries-given-problems-note-confidence-level-q25020012  */

CREATE TABLE Product ( maker VARCHAR(20), model INT PRIMARY KEY, type VARCHAR(10));

CREATE TABLE PC ( model INT PRIMARY KEY,

speed DECIMAL (4,2),

ram INT,

hd INT,

price DECIMAL (7,2)

);

CREATE TABLE Laptop ( model INT PRIMARY KEY,

speed DECIMAL (4,2),

ram INT,

hd INT,

screen DECIMAL (3,1),

price DECIMAL (7,2)

);

CREATE TABLE Printer ( model INT PRIMARY KEY,

color CHAR (6),

type VARCHAR(10),

price DECIMAL (7,2)

);

INSERT INTO Product VALUES ('A', 1001, 'pc');

INSERT INTO Product VALUES ('A', 1002, 'pc');

INSERT INTO Product VALUES ('A', 1003, 'pc');

INSERT INTO Product VALUES ('A', 2004, 'laptop');

INSERT INTO Product VALUES ('A', 2005, 'laptop');

INSERT INTO Product VALUES ('A', 2006, 'laptop');

INSERT INTO Product VALUES ('B', 1004, 'pc');

INSERT INTO Product VALUES ('B', 1005, 'pc');

INSERT INTO Product VALUES ('B', 1006, 'pc');

INSERT INTO Product VALUES ('B', 2007, 'laptop');

INSERT INTO Product VALUES ('C', 1007, 'pc');

INSERT INTO Product VALUES ('D', 1008, 'pc');

INSERT INTO Product VALUES ('D', 1009, 'pc');

INSERT INTO Product VALUES ('D', 1010, 'pc');

INSERT INTO Product VALUES ('D', 3004, 'printer');

INSERT INTO Product VALUES ('D', 3005, 'printer');

INSERT INTO Product VALUES ('E', 1011, 'pc');

INSERT INTO Product VALUES ('E', 1012, 'pc');

INSERT INTO Product VALUES ('E', 1013, 'pc');

INSERT INTO Product VALUES ('E', 2001, 'laptop');

INSERT INTO Product VALUES ('E', 2002, 'laptop');

INSERT INTO Product VALUES ('E', 2003, 'laptop');

INSERT INTO Product VALUES ('E', 3001, 'printer');

INSERT INTO Product VALUES ('E', 3002, 'printer');

INSERT INTO Product VALUES ('E', 3003, 'printer');

INSERT INTO Product VALUES ('F', 2008, 'laptop');

INSERT INTO Product VALUES ('F', 2009, 'laptop');

INSERT INTO Product VALUES ('G', 2010, 'laptop');

INSERT INTO Product VALUES ('H', 3006, 'printer');

INSERT INTO Product VALUES ('H', 3007, 'printer');

INSERT INTO PC VALUES (1001, 3.66, 1024, 250, 2114);

INSERT INTO PC VALUES (1002, 2.10, 512, 250, 995);

INSERT INTO PC VALUES (1003, 1.42, 512, 80, 478);

INSERT INTO PC VALUES (1004, 2.80, 1024, 250, 649);

INSERT INTO PC VALUES (1005, 3.20, 512, 250, 630);

INSERT INTO PC VALUES (1006, 3.20, 1024, 320, 1049);

INSERT INTO PC VALUES (1007, 2.20, 1024, 200, 510);

INSERT INTO PC VALUES (1008, 2.20, 2048, 250, 770);

INSERT INTO PC VALUES (1009, 2.00, 1024, 250, 650);

INSERT INTO PC VALUES (1010, 2.80, 2048, 300, 770);

INSERT INTO PC VALUES (1011, 1.86, 2048, 160, 959);

INSERT INTO PC VALUES (1012, 2.80, 1024, 160, 649);

INSERT INTO PC VALUES (1013, 3.06, 512, 80, 529);

INSERT INTO Laptop VALUES (2001, 2.00, 2048, 240, 20.1, 3673);

INSERT INTO Laptop VALUES (2002, 1.73, 1024, 80, 17.0, 949);

INSERT INTO Laptop VALUES (2003, 1.80, 512, 60, 15.4, 549);

INSERT INTO Laptop VALUES (2004, 2.00, 512, 60, 13.3, 1150);

INSERT INTO Laptop VALUES (2005, 2.16, 1024, 120, 17.0, 2500);

INSERT INTO Laptop VALUES (2006, 2.00, 2048, 80, 15.4, 1700);

INSERT INTO Laptop VALUES (2007, 1.83, 1024, 120, 13.1, 1429);

INSERT INTO Laptop VALUES (2008, 1.60, 1024, 100, 15.4, 900);

INSERT INTO Laptop VALUES (2009, 1.60, 512, 80, 14.1, 680);

INSERT INTO Laptop VALUES (2010, 2.00, 2048, 160, 15.4, 2300);

INSERT INTO Printer VALUES (3001, 'true', 'ink-jet', 99);

INSERT INTO Printer VALUES (3002, 'false', 'laser', 139);

INSERT INTO Printer VALUES (3003, 'true', 'laser', 899);

INSERT INTO Printer VALUES (3004, 'true', 'ink-jet', 120);

INSERT INTO Printer VALUES (3005, 'false', 'laser', 99);

INSERT INTO Printer VALUES (3006, 'true', 'ink-jet', 100);

INSERT INTO Printer VALUES (3007, 'true', 'laser', 899);

commit;

