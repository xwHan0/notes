from flask import Flask, render_template, url_for

app = Flask(__name__)

items = [ \
    {'name':'Switch', 'x':100, 'y':100}, \
    {'name':'Flask', 'x':100, 'y':150, 'class':'tool'}, \
    {'name':'taskMgr', 'x':100, 'y':180, 'class':'tool'}, \
    ]

detail_components = [ \
    {'name':'bwMgr', 'x':300, 'y':300, 'width':300, 'height':100,
     'detail': [ \
            {'title':'Middleware', 'content':' Shaper | PPM | MSP | PPB | PS'},
            {'title':'Scheduler', 'content':' TDM | WRR | DPA | EIAA'},
            {'title':'Core', 'content':' Graph | hierachy-sc'},
        ]
    },
    {'name':'spaceMgr', 'x':300, 'y':500, 'width':300, 'height':100,
     'detail': [ \
            {'title':'Space', 'content':' headroom | shared | reserved'},
            {'title':'Algorithm', 'content':' dyn-threshold | multi-threshold '},
            {'title':'Core', 'content':' hierachy'},
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', items=items, detail_components=detail_components)

