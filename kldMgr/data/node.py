class BasicCell():
    def __init__(self, name = '', title = '', href='', style='', width = 100, height = 30, refcell = None, refdir = 0, ofstx = 0, ofsty = 0):
        self.name = name
        self.title = title
        self.width = width
        self.height = height
        self.href = href
        self.style = style if style != '' else 'doc'
   
        if refcell:
            if refdir == 0:
                self.x = refcell.x + ofstx
                self.y = refcell.y + refcell.height + ofsty
            else:
                self.x = refcell.x + refcell.width + ofstx
                self.y = refcell.y + ofsty
        else:
            self.x = ofstx
            self.y = ofsty
            
        self.subs = []
        
        
class BasicBrach():
    def __init__(self, name = '', href = ''):
        self.name = name
        self.href = href
        self.subs = []