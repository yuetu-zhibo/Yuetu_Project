from flask import Blueprint, request, jsonify

from mainapp import db

from mainapp.models import User

test_blue = Blueprint('blue2', __name__)


@test_blue.route('/test/', methods=('POST',))
def name_test():
    # 实名认证接口
    data = request.get_json()
    realname = data.get('realname')
    paper = data.get('paper')
    telphone = data.get('telphone')
    user = db.session.query(User).filter(User.telphone == telphone).first()

    if all((user.paper == paper,user.realname == realname)):
        return jsonify({
            'status':0,
            'msg':'已认证'
        })
    else:
        user.realname = realname
        user.paper = paper
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'status': 1,
            'msg': '认证成功'
        })

