from flask import Blueprint, jsonify, request
from mainapp import db
from mainapp.models import User, Userfan, Attention

feel_blue = Blueprint('blue6', __name__)


@feel_blue.route('/intereted/', methods=('POST',))
def interested():
    data = request.get_json()
    userid = data.get('userid')
    user = db.session.query(User).filter(User.userid == userid).first()
    id = user.id
    att_list = db.session.query(Attention).filter(Attention.id == id).all()
    user_list = db.session.query(User).all()
    list1 = []
    for i in user_list:
       if i not in att_list:
           list1.append(i)
    # 感兴趣推荐用户接口
    new_list = []
    for user in list1:
        userimage = user.userimage
        username = user.username
        userid = user.userid
        user_fans = db.session.query(Userfan).filter(Userfan.flower_user_id == userid).all()
        vipid = user.vipid
        user_data = {
            "userimage": userimage,
            "username": username,
            "vipid": vipid,
            'user_follow_num': len(user_fans),
            'userid':userid,
            "focus":0
        }
        new_list.append(user_data)
    data = {
        'new': new_list
    }
    users = {
        'status': 0,
        'msg': '成功',
        'data': data
    }
    return jsonify(users)


@feel_blue.route('/onclick/', methods=('POST',))
def attention():
    try:
        data = request.get_json()
        userid = data.get('userid')
        attentionid = data.get('attentionid')
        user = db.session.query(User).filter(User.userid == userid).first()
        id = user.id
        newattention = Attention(id=id,userid=user.userid)
        db.session.add(newattention)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({
            'status': 1,
            'msg': '已关注'
        })
    return jsonify({
        'status': 0,
        'msg': '关注成功'
    })