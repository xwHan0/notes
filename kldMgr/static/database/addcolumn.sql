
CREATE TABLE tmp
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  x INTEGER default 0,
  y INTEGER default 0,
  width INTEGER default 100,
  height INTEGER default 30,
  style TEXT default "",
  href TEXT default "",
  svg TEXT default ""
);
  
INSERT INTO tmp(name,x,y,style,href) SELECT name,x,y,style,href FROM knowledge;
