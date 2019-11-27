from flask import Blueprint, request
from flask import jsonify
from mainapp import db
from mainapp.models import User,Viptable,Attention,Userfan,Liveadmin,Life,Audience
from mainapp.serializer import dumps

user_search_blue = Blueprint('user_search_blue', __name__)


@user_search_blue.route('/search/',methods=('POST',))
def search_user():
    # 搜索接口
    data = request.get_json()
    userid = data.get('userid')
    s_user = db.session.query(User).filter(User.userid==userid).first()
    user_fans = db.session.query(Userfan).filter(Userfan.flower_user_id==s_user.userid).all()
    #vip_class = db.session.query(Viptable).filter(Viptable.vipid==s_user.vipid).first()
    if not s_user:
        return jsonify({
            'status':1,
            'msg':'用户不存在'
        })
    else:
        return jsonify({
            'userimage':s_user.userimage, # 用户头像
            'username':s_user.username, # 用户名
            #'vipclass':dumps(vip_class), # vip
            'user_fans':len(user_fans), # 粉丝数
        })



@user_search_blue.route('/see_user/',methods=('GET',))
def see_users():
    # 点击查看他人信息接口
    userid = request.args.get("userid")
    print(userid)
    user = db.session.query(User).filter(User.userid == userid).first()
    user_attentions = db.session.query(Attention).filter(Attention.userid==user.userid).all()
    user_fans = db.session.query(Userfan).filter(Userfan.flower_user_id == user.userid).all()
    #vip_class = db.session.query(Viptable).filter(Viptable.vipid==user.vipid).first().vipclass
    if user is None:
        return jsonify({
            'status':1,
            'msg':'查无此人'
        })
    else:
        return jsonify({
            'username': user.username,
            'userid': user.userid,
            'userimage': user.userimage,
            'autograph': user.autograph,
            'sex': user.sex,
            #'vip_class': vip_class,
            'user_attentions': user_attentions,
            'user_follows': user_fans,
            'user_attention_num': len(user_attentions),
            'user_follow_num': len(user_fans)
        })


@user_search_blue.route('/edit',methods=('POST',))
def edit_profile():
    # 修改个人信息接口
    try:
        data = request.get_json()
        userid = data.get("userid")
        user = db.session.query(User).filter(User.userid == userid).first()
        userimage = data.get('userimage')
        username = data.get('username')
        sex = data.get('sex')
        birth = data.get('birth')
        print(birth)
        autograph = data.get('autograph')
        user.userimage = userimage
        user.username = username
        user.sex = sex
        user.birth = birth
        user.autograph = autograph
        db.session.add(user)
        db.session.commit()
    except:
        return jsonify({
            'status':1,
            'msg':'修改失败'
        })
    return jsonify({
        'status':0,
        'msg':'修改成功'
    })

@user_search_blue.route('/getvip/',methods=('POST',))
def get_vip():
    # 充值vip接口
    userid = request.args.get("userid")
    user = db.session.query(User).filter(User.userid == userid).first()
    gitvip = request.args.get("getvip")
    if gitvip == '1':
        if int(user.vipid) >= int(gitvip):
            return jsonify({
                'static':2,
                'msg':'您已经是更高等级的vip了'
            })
        elif int(user.balance) >= 1000000:
            balance = user.balance
            new_balance = int(balance) - 1000000
            user.balance = new_balance
            user.vipid = gitvip
            db.session.add(user)
            db.session.commit()
            return jsonify({
                'static': 0,
                'msg': '恭喜成为红V'
            })
        else:
            return jsonify({
                'static':0,
                'msg':'余额不足请充值'
            })

    if gitvip == '2':
        if int(user.vipid) >= int(gitvip):
            return jsonify({
                'static':2,
                'msg':'您已经是更高等级的vip了'
            })
        elif int(user.balance) >= 3000000:
            balance = user.balance
            new_balance = int(balance) - 1000000
            user.balance = new_balance
            user.vipid = gitvip
            db.session.add(user)
            db.session.commit()
            return jsonify({
                'static': 0,
                'msg': '恭喜成为紫V'
            })
        else:
            return jsonify({
                'static':0,
                'msg':'余额不足请充值'
            })
    if gitvip == '3':
        if int(user.vipid) >= int(gitvip):
            return jsonify({
                'static':2,
                'msg':'您已经是更高等级的vip了'
            })
        elif int(user.balance) >= 5000000:
            balance = user.balance
            new_balance = int(balance) - 5000000
            user.balance = new_balance
            user.vipid = gitvip
            db.session.add(user)
            db.session.commit()
            return jsonify({
                'static': 0,
                'msg': '恭喜成为银冠'
            })
        else:
            return jsonify({
                'static':0,
                'msg':'余额不足请充值'
            })
    if gitvip == '4':
        if int(user.vipid) >= int(gitvip):
            return jsonify({
                'static':2,
                'msg':'您已经是更高等级的vip了'
            })
        elif int(user.balance) >= 10000000:
            balance = user.balance
            new_balance = int(balance) - 10000000
            user.balance = new_balance
            user.vipid = gitvip
            db.session.add(user)
            db.session.commit()
            return jsonify({
                'static': 0,
                'msg': '恭喜成为皇冠'
            })
        else:
            return jsonify({
                'static':0,
                'msg':'余额不足请充值'
            })
    if gitvip == '5':
        if int(user.vipid) >= int(gitvip):
            return jsonify({
                'static':2,
                'msg':'您已经是更高等级的vip了'
            })
        elif int(user.balance) >= 30000000:
            balance = user.balance
            new_balance = int(balance) - 30000000
            user.balance = new_balance
            user.vipid = gitvip
            db.session.add(user)
            db.session.commit()
            return jsonify({
                'static': 0,
                'msg': '恭喜成为钻冠'
            })
        else:
            return jsonify({
                'static':0,
                'msg':'余额不足请充值'
            })
    if gitvip == '6':
        if int(user.vipid) >= int(gitvip):
            return jsonify({
                'static':2,
                'msg':'您已经是更高等级的vip了'
            })
        elif int(user.balance) >= 50000000:
            balance = user.balance
            new_balance = int(balance) - 50000000
            user.balance = new_balance
            user.vipid = gitvip
            db.session.add(user)
            db.session.commit()
            return jsonify({
                'static': 0,
                'msg': '恭喜成为至尊'
            })
        else:
            return jsonify({
                'static':0,
                'msg':'余额不足请充值'
            })


@user_search_blue.route('/recharge/',methods=('POST',))
def recharge():
    # 充值vip接口
    userid = request.args.get("userid")
    user = db.session.query(User).filter(User.userid == userid).first()
    r_charge = request.args.get("r_charge")
    balance = user.balance
    new_balance = int(r_charge) * 100000 + int(balance)
    user.balance = new_balance
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'static':0,
        'msg':'充值成功'
    })

@user_search_blue.route('/room_manage/',methods=('POST',))
def room_manage():
    # 设置房间管理员
    try:
        data = request.get_json()
        userid = data.get('userid')
        user = db.session.query(User).filter(User.userid == userid).first()
        room = db.session.query(Life).filter(Life.id == user.id).first()
        m_userid = data.get('user_id')
        s_user = db.session.query(User).filter(User.userid == m_userid).first()
        lives = Liveadmin(rec_id=room.rec_id,user_id=s_user.userid)
        db.session.add(lives)
        db.session.commit()
        return jsonify({
            'static': 0,
            'msg': '设置管理员成功',
            'data':{
                'username':s_user.username,
                'userid':s_user.userid,
                'userimage':s_user.userimage
            }
        })
    except:
        return jsonify({
            'static':1,
            'msg':'添加失败'
        })

@user_search_blue.route('/live_room',methods=('POST',))
def liveroom():
    # 直播间接口
    try:
        data = request.get_json()
        userid = data.get('userid')
        user = db.session.query(User).filter(User.userid == userid).first()
        room = db.session.query(Life).filter(Life.id == user.id).first()
        room_ip = "rtmp://39.98.126.184:1935/live/"+room
        return jsonify({
            "static":"0",
            "msg":"进入直播间成功",
            "data":{
                "room_ip": room_ip,
                "userid": user.userid,
                "username": user.username,
                "userimage": user.userimage,
                "charisma": room.charisma,
            },
        })
    except:
        return jsonify({
            "static":1,
            "msg":"出错了，直播间不存在"
        })
