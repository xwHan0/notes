
import functools

class schNode ():

    connectSize = 80
    nodeW = 50
    nodeH = 100
    nameSize = 20

    def __init__ (self, subNodes = [], algorithm = "RR", name = "", positionX = 0, positionY = 0 ):
        self.algorithm = algorithm
        self.name = name
        self.subNodes = subNodes
        self.positionX = positionX
        self.positionY = positionY

    def bind (self, subNodes):
        self.subNodes = subNodes

    # def sizeW (self): return schNode.connectSize + schNode.nodeW + schNode.nameSize
    # def sizeH (self): return self.subNodes[-1] + 30
    # def positionY (self): return ( self.subNodes[0] + self.subNodes[-1] ) / 2

    def getPositionX (self, offset = 0):
        """获取当前节点绘图的左上角横坐标信息。
        
        Keyword Arguments:
            offset {int} -- 默认的起始偏移量 (default: {0})
        """
        if len(self.subNodes) > 0:
            # positionXs = [node.getPositionX() for node in self.subNodes]
            positionXs = map( schNode.getPositionX, self.subNodes )
        else:
            positionXs = [0]
        return functools.reduce( max, positionXs, 0 ) + 100


    def positionCompile (self, offsetX = 0, offsetY = 0):
        """Calculate all nodes' (includes subNodes) position and update the position information into class instance.
               
        Keyword Arguments:
            offsetX {int} -- Pararent node x-axis position of up-left corner (default: {0})
            offsetY {int} -- Start y-axis position (default: {0})
        """
        
        # Update pjostion X
        self.positionX = offsetX - schNode.connectSize - schNode.nodeW - schNode.nameSize

        if len(self.subNodes) > 0:
            self.positionY = functools.reduce( lambda node: node.positionCompile( offsetX ), self.subNodes, 0 )
            self.positionOutput = ( self.subNodes[0].positionOutput + self.subNodes[-1].positionOutput ) / 2
        else:
            self.positionY = offsetY + 60
            self.positionOutput = offsetY + 30

        return self.positionY

#     def draw (self):
#         svg = ""
#         connectX = self.positionX    #連接綫起始位置X
#         connectCenterY = ( self.subNodes[0] + self.subNodes[-1] ) / 2     #連接綫終結位置Y
#         nodeX = connectX + schNode.connectSize  #調度器框起始位置X
#         nodeRX = schNode.nodeW / 2      #調度器框的X半徑
#         nodeRY = min( schNode.nodeH / 2, connectCenterY )   #調度器框的Y半徑
#         nameX = connectX + schNode.nodeW    #調度出口綫的位置X
#         for sub in self.subNodes:
#             if sub >= 0:
#                 svg = svg + "<line x1='{0}' y1='{1}' x2='{2}' y2='{3}' stroke='blank' />\n".format( connectX, sub, nodeX, connectCenterY )
#         svg = svg + "<ellipse cx='{0}' cy='{1}' rx='{2}' ry='{3}' stroke='red' fill='white'/>\n".format(nodeX + schNode.nodeW/2, connectCenterY, nodeRX, nodeRY)
#         svg = svg + "<line x1='{0}' y1='{1}' x2='{2}' y2='{1}' stroke='red' />\n".format( nameX, connectCenterY, nameX + schNode.nameSize )
#         return svg

# sc = schNode( 8 )

# print( sc.draw() )
        
sc = schNode([schNode(), schNode()])
print( sc.getPositionX() )