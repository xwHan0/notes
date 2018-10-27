--ALTER TABLE tasks RENAME TO temp;  -- Rename table

--drop table milestones; --- Do not need when rename Table using ALTER 

CREATE TABLE special_func
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  func NCHAR(30),
  typ INTEGER default 1,
  style NCHAR(30),
  description TEXT default "",
  example TEXT default ""
);

--INSERT INTO descriptions(id,tid,type,owner,content,duration,date) select id,tid,type,owner,content,duration,date from temp;

--drop table temp;