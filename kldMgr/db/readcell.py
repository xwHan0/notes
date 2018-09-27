import sqlite3
from node import BasicCell

def read_cell():

  conn = sqlite3.connect('static/database/index.db3')
  conn.row_factory = sqlite3.Row
  c = conn.cursor()
  c.execute('SELECT * FROM knowledge')

  lastCell = BasicCell()  # 设置初始Cell
  cells = [BasicCell(k['id'],k['']) for k in c]
  for item in cells:
    # 设置
    key0 = item['id']
    # 查找一级子分支
    

  basic_cell = [BasicCell(k['name'],k['x'],k['y'],k['href'],k['style']) for k in c]

  c.close()
