# _*_ coding:utf-8 _*_
__author__ = 'caimiao'
__date__ = '15-3-30'


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, session

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '阿三服阿斯顿服'

@app.errorhandler(404)
def test_404(error):
    return '<h1>404 occur</h1><br />%s' % (str(error)), 404

if "__main__" == __name__:
    app.run(host='0.0.0.0', port=5000)