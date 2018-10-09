import sqlite3
from node import BasicCell

def read_cell():

  conn = sqlite3.connect('static/database/index.db3')
  conn.row_factory = sqlite3.Row
  items = conn.execute('SELECT * FROM knowledge')

  rst = []
  lastCell = BasicCell()  # 设置初始Cell
  for item in items:
      cell = BasicCell(
          name = item['name'],
          href = item['href'],
          title = item['title'],
          style = item['style'],
          ofstx = item['x'],
          ofsty = item['y'],
          refcell = last_cell
      )
      key0 = item['id']
      brach0 = conn.execute('SELECT * FROM detail WHERE parent=? AND lvl=?', (key0,1))
      for brach in brach0:
          b = BasicBrach(brach['name'], brach['href'])
          key1 = brach['id']
          content = conn.execute('SELECT * FROM detail WHERE parent=? AND lvl=?', (key1,2))
          b.subs = [BasicBrach(name=c['name'], href=c['href']) for c in content]
          cell.subs.append(b)
       cell.subs = cells.subs if cell.subs != [] else None
       last_cell = cell
       rst.append(cell)
       
    conn.close()
    
    return rst
    

  
