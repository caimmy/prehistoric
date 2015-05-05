# _*_ coding:utf-8 _*_
__author__ = 'caimiao'
__date__ = '15-3-30'


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, g

from archgis import archgis_app
from archaeology import archaeology_app


app = Flask(__name__)
app.config.from_pyfile('application.cfg')

app.register_blueprint(archgis_app, url_prefix='/gis')
app.register_blueprint(archaeology_app, url_prefix='/arch')

@app.route('/')
def hello_world():
    return '阿三服阿斯顿服'

@app.errorhandler(404)
def test_404(error):
    return '<h1>404 occur</h1><br />%s' % (str(error)), 404


@app.before_request
def before_request():
    from models import db_session
    g.db = db_session

@app.teardown_request
def tear_down(exception):
    if hasattr(g, "db"):
        g.db.close()

if "__main__" == __name__:
    app.run(host='0.0.0.0', port=5000)