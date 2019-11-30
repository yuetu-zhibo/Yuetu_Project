from flask import Blueprint, request, jsonify

from mainapp import db
from mainapp.models import User

start_blue = Blueprint('blue7', __name__)


@start_blue.route('/live/', methods=('GET',))
def name_test():
    # 实名认证接口
    userid = request.args.get('userid')
    user = db.session.query(User).filter(User.userid == userid).first()
    paper = user.paper
    if paper is None:
        return jsonify({
            'status': 1,
            'msg': '请先通过认证'
        })
    else:
        return jsonify({
            'status': 0,
            'msg': '已认证过，可进行直播'
        })