CREATE TABLE explorer(id INTEGER PRIMARY KEY, name TEXT UNIQUE);
CREATE TABLE assessment(explorer_id INTEGER, skill TEXT, score INTEGER);
CREATE TABLE journal(explorer_id INTEGER, observed_at TEXT, entry TEXT);
INSERT INTO explorer VALUES (1,'Isla'),(2,'Anastasia'),(3,'Ravi'),(4,'Noor');
INSERT INTO assessment VALUES (1,'Navigation',8),(1,'Radio',7),(2,'Navigation',9),(2,'Radio',9),(3,'Navigation',6),(3,'Radio',10),(4,'Navigation',9),(4,'Radio',8);
INSERT INTO journal VALUES (2,'2026-02-01T08:00:00Z','Reached the lighthouse.'),(4,'2026-02-05T15:30:00Z','Packed the transmitter.'),(2,'2026-02-03T15:00:00Z','Trying to fix DNS. It''s always DNS.'),(1,'2026-02-06T09:00:00Z','Returned at low tide.');
