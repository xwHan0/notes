from flask import Flask, render_template, url_for
from kldMgr.db.readcell import read_cell

app = Flask(__name__, static_folder='static', template_folder='templates')


basic_cell = read_cell()


@app.route('/')
def index():
    return render_template('index.html', 
         basic_cell = basic_cell)


if __name__ == '__main__':
    app.run(debug=True)