import json

import redis
from flask import Blueprint, request
from flask import jsonify
from mainapp import db
from mainapp.models import User,Viptable,Attention,Userfan,Liveadmin,Life,Gift
from mainapp.serializer import dumps

user_function_blue = Blueprint('user_function_blue', __name__)

def R_get(tokens):
    r = redis.Redis(host='39.98.126.184', port=6379, db=1, decode_responses=True)
    userid = r.get(tokens)
    return userid

@user_function_blue.route('/search/',methods=('POST',))
def search_user():
    # 搜索接口
    data = request.get_json()
    if len(data) != 0:
        userid = R_get(data["token"])
        user = db.session.query(User).filter(User.userid == userid).first()
        #attentioned = db.session.query(Attention).filter(Attention.id == user_id).all()
        s_userid = data["s_userid"]
        s_user = db.session.query(User).filter(User.userid==s_userid).first()
        user_fans = db.session.query(Userfan).filter(Userfan.flower_user_id==s_user.userid).all()
        vip_class = db.session.query(Viptable).filter(Viptable.vipid == s_user.vipid).first()
        is_attentions = 0
        # newlist = []
        # for i in attentioned:
        #     attentionuserid = i.userid
        #     newlist.append(attentionuserid)
        #     if s_userid in newlist:
        #         return is_attentions == True
        #     else:
        #         return is_attentions == False
        return jsonify({
            'userimage': s_user.userimage,  # 用户头像
            'username': s_user.username,  # 用户名
            'vipid': vip_class.vipid if vip_class else "",  # vip
            'user_follow_num': len(user_fans),  # 粉丝数
            'userid':userid,
            'focus': is_attentions,
            'live':True
        })
    else:
        return jsonify({
            'status':0,
            'msg': "token不存在！"
        })

@user_function_blue.route('/see_user',methods=('GET',))
def see_users():
    # 点击查看他人信息接口
    data = request.args.get('token')
    userid = R_get(data)
    if userid:

        fans_list = []
        user = db.session.query(User).filter(User.userid == userid).first()
        user_attentions = db.session.query(Attention).filter(Attention.userid == user.userid).all()
        room = db.session.query(Life).filter(Life.rec_id == user.id).first()
        islive = room.status
        for useratt in user_attentions:
            username1 = useratt.user.username
            userid1 = useratt.user.userid
            userimage1 = useratt.user.userimage
            autograph1 = useratt.user.autograph
            data = {
                "username":username1,
                "userid":userid1,
                "userimage":userimage1,
                "autograph":autograph1
            }
            fans_list.append(data)
        attention_list = []
        user_fans = db.session.query(Attention).filter(Attention.id == user.id).all()
        for usefans in user_fans:
            username = usefans.user.username
            userid = usefans.user.userid
            userimage = usefans.user.userimage
            autograph = usefans.user.autograph
            data1 = {
                "username":username,
                "userid":userid,
                "userimage":userimage,
                "autograph":autograph
            }
            attention_list.append(data1)
        vip_class = db.session.query(Viptable).filter(Viptable.vipid==user.vipid).first()
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
                'vip_class':vip_class.vipid if vip_class else "",
                'user_attentions': attention_list,
                'user_follows': fans_list,
                'user_attention_num': len(attention_list),
                'user_follow_num': len(fans_list),
                'paper':user.paper if True else False,
                'islive':islive
            })
    else:
        return jsonify({
            'status':0,
            'msg': "token不存在！"
        })

@user_function_blue.route('/edit',methods=('POST',))
def edit_profile():
    # 修改个人信息接口
    try:
        data = request.get_json()
        if len(data) != 0:
            userid = R_get(data["token"])
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
        else:
            return jsonify({
                'status': 0,
                'msg': "token不存在！"
            })
    except:
        return jsonify({
            'status':1,
            'msg':'修改失败'
        })
    return jsonify({
        'status':0,
        'msg':'修改成功'
    })

@user_function_blue.route('/getvip/',methods=('POST',))
def get_vip():
    # 充值vip接口
    data = request.get_json()
    print("AAAAAAAAAA",data)
    if len(data) != 0:
        userid = R_get(data["token"])
        user = db.session.query(User).filter(User.userid == userid).first()
        gitvip = data["getvip"]
        print("CCCCCCCCCCCC",user,userid)
        if gitvip == '1':
            a = user.vipid if user.vipid else "0"
            if int(a) >= int(gitvip):
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
                    'static':1,
                    'msg':'余额不足请充值'
                })

        if gitvip == '2':
            a = user.vipid if user.vipid else "0"
            if int(a) >= int(gitvip):
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
                    'static':1,
                    'msg':'余额不足请充值'
                })
        if gitvip == '3':
            a = user.vipid if user.vipid else "0"
            if int(a) >= int(gitvip):
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
                    'static':1,
                    'msg':'余额不足请充值'
                })
        if gitvip == '4':
            a = user.vipid if user.vipid else "0"
            if int(a) >= int(gitvip):
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
                    'static':1,
                    'msg':'余额不足请充值'
                })
        if gitvip == '5':
            a = user.vipid if user.vipid else "0"
            if int(a) >= int(gitvip):
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
                    'static':1,
                    'msg':'余额不足请充值'
                })
        if gitvip == '6':
            a = user.vipid if user.vipid else "0"
            if int(a) >= int(gitvip):
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
                    'static':1,
                    'msg':'余额不足请充值'
                })
    else:
        return jsonify({
            'status':0,
            'msg': "token不存在！"
        })

@user_function_blue.route('/recharge',methods=('POST',))
def recharge():
    # 充值接口
    data = request.get_json()
    if len(data) != 0:
        userid = R_get(data["token"])
        user = db.session.query(User).filter(User.userid == userid).first()
        r_charge = data.get("r_charge")
        balance = user.balance
        new_balance = int(r_charge) * 100000 + int(balance)
        user.balance = new_balance
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'static':0,
            'msg':'充值成功',
            'data':{
                'username':user.username,
                'userid':user.userid,
                'userimage':user.userimage
            }
        })
    else:
        return jsonify({
            'status':0,
            'msg': "token不存在！"
        })

@user_function_blue.route('/room_manage',methods=('POST',))
def room_manage():
    # 设置房间管理员
    try:
        data = request.get_json()
        if len(data) != 0:
            userid = R_get(data["token"])
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
        else:
            return jsonify({
                'status': 0,
                'msg': "token不存在！"
            })
    except:
        return jsonify({
            'static':1,
            'msg':'添加失败'
        })

@user_function_blue.route('/live_room',methods=('POST',))
def liveroom():
    # 主播开播进入直播间接口
    data = request.get_json()
    print("")
    if len(data) != 0:
        userid = R_get(data["token"])
        user = db.session.query(User).filter(User.userid == userid).first()
        room = db.session.query(Life).filter(Life.rec_id == user.id).first()
        roomid = room.studiono
        room_ip = "rtmp://39.98.126.184:1935/live/" + roomid
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
    else:
        return jsonify({
            'status':0,
            'msg': "token不存在！"
        })

@user_function_blue.route('/in_room',methods=('POST',))
def in_room():
    # 观众进入直播间接口
    data = request.get_json()
    if len(data) != 0:
        userid = R_get(data["token"])
        studiono = data['studiono']
        user = db.session.query(User).filter(User.userid == userid).first()
        room_ip = "rtmp://39.98.126.184:1935/live/" + studiono
        room = db.session.query(Life).filter(Life.studiono == studiono).first()
        r_user = db.session.query(User).filter(User.id == room.id).first()
        vip_class = db.session.query(Viptable).filter(Viptable.vipid == user.vipid).first()
        return jsonify({
            'static':0,
            'msg':'进入直播成功',
            'data':{
                "room_ip": room_ip,
                "userid": r_user.userid,
                "username": r_user.username,
                "userimage": r_user.userimage,
                "vipclass":vip_class.vipid if vip_class else "",
                "charisma": room.charisma,
                "user_balance":user.balance
            }
        })
    else:
        return jsonify({
            'status':0,
            'msg': "token不存在！"
        })

@user_function_blue.route('/reward',methods=('POST',))
def reward():
    # 送礼物接口
    data = request.get_json()
    if len(data) != 0:
        userid = R_get(data["token"])
        user = db.session.query(User).filter(User.userid == userid).first() # 用户
        roomid = data.get("studiono")
        room = db.session.query(Life).filter(Life.studiono == roomid).first() # 直播间
        charismas = room.charisma # 魅力值
        r_userid = room.user.userid
        r_user = db.session.query(User).filter(User.userid == r_userid).first() # 房主
        r_user_balance = r_user.balance # 主播余额
        g_id = data.get("id")
        balance = user.balance # 用户余额
        gift = db.session.query(Gift).filter(Gift.id == g_id).first() # 礼物对象
        gift_price = gift.giftprice # 礼物价格
        if int(balance) >= int(gift_price):
            user.balance = int(balance) - int(gift_price)
            r_user.balance = int(r_user_balance) + int(gift_price)
            room.charisma = charismas + int(gift_price)/10
            db.session.add(user,room)
            db.session.commit()
            return jsonify({
                'static':0,
                'msg':"赠送成功",
                'data':{
                    'userimage':user.userimage,
                    'username':user.username,
                    'charismas':room.charisma,
                    'giftimage':gift.image,
                    'giftname':gift.giftname,
                }
            })
        else:
            return jsonify({
                'static':1,
                'msg':'余额不足，赠送失败'
            })
    else:
        return jsonify({
            'status':0,
            'msg': "token不存在！"
        })