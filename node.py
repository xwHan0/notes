class BasicCell():
    def __init__(self, name, x = 0, y = 0, href='', style=''):
        self.name = name
        self.x = x
        self.y = y
        self.href = href
        self.style = style if style != '' else 'doc'