USE test;
DROP TABLE IF EXISTS Friends;
CREATE TABLE Friends (
  id INTEGER,
  name VARCHAR(50),
  age INTEGER
);
INSERT INTO Friends VALUES (0, 'Monica Geller', 33);
INSERT INTO Friends VALUES (1, 'Rachel Green', 34);
INSERT INTO Friends VALUES (2, 'Joey Tribbiani', 35);
INSERT INTO Friends VALUES (3, 'Chandler Bing', 36);
INSERT INTO Friends VALUES (4, 'Ross Geller', 37);
