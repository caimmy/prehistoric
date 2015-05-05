# _*_ coding:utf-8 _*_
__author__ = 'caimiao'
__date__ = '15-3-30'

from flask import Blueprint, render_template

archgis_app = Blueprint('archgis', __name__, template_folder='templates')

@archgis_app.route('/', methods=['GET'])
def Index():
    return render_template('archgis/_index.html', name="hello archgis")

@archgis_app.route('/test')
def Test():
    return render_template('archgis/_test.html')