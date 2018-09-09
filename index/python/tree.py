
class TreeLeaf():
    def __init__(self,content,height=30,width=100,offset=40):
        self.content = content
        self.height = height
        self.width = width
        self.offset = offset
        self.style = 'tree_list'
    
    def setXY(self,x,y):
        self.x = x
        self.y = y
        return self


class TreeBranch():
    def __init__(self, content, *args):
        self.content = content  # 目录文字
        self.sub = args     # 子项

    def setXY(self,x,y):
        self.x = x      # 设置左上角X坐标
        self.y = y      # 设置左上角Y坐标

        # 遍历子项
        height = 30
        width = 0
        for lef in self.sub:
            lef.setXY( self.x + 10, self.y + height )   # 设置坐标位置
            height += lef.height  # 累加子项高度
            width = max(width, lef.width)   # 获取最大子项宽度

        self.height = height
        self.width = width

        return self



