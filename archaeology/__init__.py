# _*_ coding:utf-8 _*_
__author__ = 'caimiao'
__date__ = '15-5-5'

from flask import Blueprint, render_template

archaeology_app = Blueprint("archaeology", __name__, template_folder="templates")


@archaeology_app.route('/')
def Index():
    return render_template("archaeology/_index.html",
                           name="asdf")