from flask import Flask, render_template, url_for
from tree import TreeLeaf, TreeBranch

class tree_list():
    def __init__(self,content,height=30,width=100,offset=40):
        self.content = content
        self.height = height
        self.width=width
        self.offset=offset
        self.style = 'tree_list'
    
    def setXY(self,x,y):
        self.x = x
        self.y = y
        return self


app = Flask(__name__)

items = [ \
    {'name':'Switch', 'x':100, 'y':100}, \
    {'name':'Flask', 'x':100, 'y':150, 'class':'tool'}, \
    {'name':'taskMgr', 'x':100, 'y':180, 'class':'tool'}, \
    {'name':'xrange', 'x':200, 'y':100, 'class':'tool'} \
    ]

detail_components = [ \
    {'name':'bwMgr', 'x':300, 'y':300, 'width':300, 'height':100,
     'detail': [ \
            {'title':'Middleware', 'content':' Shaper | PPM | MSP | PPB | PS'},
            {'title':'Scheduler', 'content':' TDM | WRR | WFQ | DPA | EIAA'},
            {'title':'Core', 'content':' Graph | hierachy-sc'},
        ]
    },
    {'name':'spaceMgr', 'x':300, 'y':500, 'width':300, 'height':100,
     'detail': [ \
            {'title':'Space', 'content':' headroom | shared | reserved'},
            {'title':'Algorithm', 'content':' dyn-threshold | multi-threshold '},
            {'title':'Core', 'content':' hierachy'},
        ]
    },
    {'name':'Flask', 'x':300, 'y':900, 'width':300, 'height':100,
     'detail': [ \
            {'title':'HTTP Component', 'content':' Route | Request | Response | Session | Redirect'},
            {'title':'Assist Component', 'content':' url_for | blueprint '},
            {'title':'Core', 'content':' hierachy'},
        ]
    }
]

branch = TreeBranch(
    "",
    TreeLeaf("apply"),
    TreeLeaf("xrange"),
    TreeLeaf("sort"),
    TreeLeaf("min/max"),
    TreeLeaf("filter"),
    TreeLeaf("map"),
    TreeLeaf("reduce")
    )

branch.setXY(400,100)



tree_lists = branch.sub

@app.route('/')
def index():
    return render_template('index.html', items=items, detail_components=detail_components, tree_lists=tree_lists)

if __name__ == '__main__':
    app.run()