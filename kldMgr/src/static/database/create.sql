--ALTER TABLE tasks RENAME TO temp;  -- Rename table

--drop table milestones; --- Do not need when rename Table using ALTER 

CREATE TABLE detail
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  lvl INTEGER default 1,
  parent INTEGER default 0,
  style TEXT default "",
  href TEXT default ""
);

--INSERT INTO descriptions(id,tid,type,owner,content,duration,date) select id,tid,type,owner,content,duration,date from temp;

--drop table temp;