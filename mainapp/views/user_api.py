#!/usr/bin/python3
# coding: utf-8
import random

from flask import Blueprint, request
from flask import jsonify
from sqlalchemy.orm import Query

from mainapp import db
from mainapp.common import sms_
from mainapp.common.crypo import encode4md5
from mainapp.common.token_ import new_token


from mainapp.models import User


user_blue = Blueprint('blue1', __name__)


@user_blue.route('/send_code/', methods=('GET',))
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


@user_blue.route('/regist/', methods=('POST', ))
def regist():
    # {"phone": "", "code": ""}
    try:
        data = request.get_json()
        phone = data.get('phone')
        code = data.get('code')
        password = data.get('password')
        print(phone)

        if sms_.validate_code(phone, code):
            userid = random.randint(100000,999999)
            user = User(userid = userid,telphone = phone,password = encode4md5(password))
            db.session.add(user)

            db.session.commit() # 提交事务
    except Exception as e:
        print(e)
        return jsonify({
            'status': 1,
            'msg': '注册失败'
        })

    return jsonify({
        'status': 0,
        'msg': '注册成功'
    })

@user_blue.route('/login/', methods=('POST',))
def login():
    # 获取请求上传的json数据
    # {'name': '', 'pwd': ''}
    try:
        req_data = request.get_json()  # dict
        logname, logpwd = req_data['logname'], req_data['logpwd']
        if len(logpwd.strip()) == 0:
            raise Exception('出现异常')
    except:
        return jsonify({
            'status': 1,
            'msg': '请求参数不完整，请提供name和pwd的json格式的参数'
        })

    query: Query = db.session.query(User).filter(User.telphone == logname)
    if query.count() == 0:
        return jsonify({
            'status': 2,
            'msg': '查无此用户'
        })
    else:
        login_user: User = query.first()
        if encode4md5(logpwd) == login_user.password:
            token = new_token()

            # 将token存在redis缓存中
            login_user.userimage="https://hgcdn.handouzb.com/201701/r1099.jpg"

            return jsonify({
                'status': 0,
                'msg': '登录成功',
                'token': token,
                'data': {
                    'telphone': login_user.telphone,
                    'password': login_user.password,
                    'userid':login_user.userid,
                    'userimages':login_user.userimage
                }
            })
        else:
            jsonify({
                'status': 3,
                'msg': '登录失败， 用户名或口令错误!',
            })