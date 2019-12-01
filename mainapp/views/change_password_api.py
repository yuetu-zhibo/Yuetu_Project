from flask import Blueprint, request, jsonify

from mainapp import db
from common import sms_
from common.crypo import encode4md5
from mainapp.models import User

change_blue = Blueprint('blue4', __name__)


@change_blue.route('/send_code', methods=('GET',))
def send_code():
    try:
        # 获取手机号
        phone = request.args.get('phone')
        sms_.send_code(phone)
    except:
        return jsonify({
            'status': 1,
            'msg': '发送失败，请重试'
        })

    return jsonify({
        'status': 0,
        'msg': '发送成功'
    })


@change_blue.route('/password', methods=('POST',))
def change():
    try:
        data = request.get_json()
        password = data.get('password')
        phone = data.get('phone')
        code = data.get('code')
        if sms_.validate_code(phone, code):
            user = db.session.query(User).filter(User.telphone == phone).first()
            user.password = encode4md5(password)
            db.session.add(user)
            db.session.commit()
    except Exception as e:
        return jsonify({
            'status': 1,
            'msg': '修改失败'
        })
    return jsonify({
        'status': 0,
        'msg': '修改成功'
    })
