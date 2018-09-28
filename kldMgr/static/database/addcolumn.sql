
CREATE TABLE tmp
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  x INTEGER default 0,
  y INTEGER default 0,
  href TEXT default "",
  style TEXT default "",
  title TEXT default ""
);
  
INSERT INTO tmp(name,x,y,href,style) SELECT name,x,y,href,style FROM knowledge;
