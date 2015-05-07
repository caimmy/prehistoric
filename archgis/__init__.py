# _*_ coding:utf-8 _*_
__author__ = 'caimiao'
__date__ = '15-3-30'

from flask import Blueprint, render_template, redirect, url_for, request
from archgis_lib import SettlementMgr
from utils.tools import getFailureResponse, changeResponseToSuccess, makeResponse

archgis_app = Blueprint('archgis', __name__, template_folder='templates')

@archgis_app.route('/', methods=['GET'])
def Index():
    return render_template('archgis/_index.html', query_url=url_for(".ajax_get_settlements"))

@archgis_app.route('/load_settles', methods=['POST'])
def ajax_get_settlements():
    ret_info = getFailureResponse()
    settlement_list = SettlementMgr.getAllSettlement()
    settle_pts = []
    for _p in settlement_list:
        settle_pts.append({'name': _p[0].name, 'long': _p[1].longitude, 'lati': _p[1].latitude,
                           'desc': _p[0].desc})
    changeResponseToSuccess(ret_info)
    ret_info['data'] = settle_pts
    return makeResponse(ret_info)

@archgis_app.route('/edit', methods=['GET'])
def GetEdit():
    return render_template('archgis/_edit.html', form_url=url_for('.AddSettlement'))

@archgis_app.route('/add_settlement', methods=['POST'])
def AddSettlement():
    form_data = request.form
    ins_id = SettlementMgr.addNewSettlement(form_data.get('settlement_name'), form_data.get('desc'), form_data.get('rel'),
                                            form_data.get('longitude'), form_data.get('latitude'),
                                            form_data.get('height_h'), form_data.get('height_l'), form_data.get('area'))
    return redirect(url_for('.GetEdit'))

@archgis_app.route('/test')
def Test():
    return render_template('archgis/_test.html')