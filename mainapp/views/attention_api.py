import random
from mainapp import db
from middleware.valid_login import is_login
from mainapp.models import Attention, Recommend, User, Life
from flask import jsonify, request
from flask import Blueprint


my_blue = Blueprint('attention_blue', __name__)

@my_blue.route('/talent/',methods=('POST','GET'))    #才艺
@is_login
def get_talent():
    newlist1 = []
    newlist2 = []
    tanlent_list = db.session.query(Life).all()
    for i in range(12):
        num = random.choice(tanlent_list)
        newlist1.append(num)
    for talent in newlist1:
        images = talent.images
        username = talent.user.username
        address = talent.user.address
        vipid = talent.user.vipid
        labels = talent.anchorlabel.labels
        studiono = talent.studiono
        talent_data = {
            "images": images,
            "userid": username,
            "location": address,
            "vipclass": vipid,
            "tag": labels,
            "studiono": studiono
        }
        newlist2.append(talent_data)
    talents_data = {
        'status': 1,
        'talents': newlist2
    }
    return jsonify(talents_data)


@my_blue.route('/near/',methods=('POST','GET'))   #附近
@is_login
def get_near():
    newlist1 = []
    near_list = db.session.query(Life).all()
    for nearuser in near_list:
        images = nearuser.images
        username = nearuser.user.username
        address = nearuser.user.address
        vipid = nearuser.user.vipid
        labels = nearuser.anchorlabel.labels
        studiono = nearuser.studiono
        near_data = {
            "image": images,
            "name": username,
            "address": address,
            "vipclass": vipid,
            "l_label":labels,
            "studiono":studiono
        }
        newlist1.append(near_data)
    data = {
        'nears': newlist1
    }
    return jsonify(data)


@my_blue.route('/attention/', methods=('POST', 'GET'))  # 关注
@is_login
def get_attention():
    newlist = []
    attent_list = db.session.query(Attention).all()  # **用户所有关注
    for attention in attent_list:
        id = attention.user.id
        username = attention.user.username
        userimage = attention.user.userimage
        # attent_list2 = db.session.query(Life).filter_by(id=id).all()
        # for live in attent_list2:
        #     studiono = live.studiono
        att_data = {
            # "studiono": studiono,
            "username": username,
            "userimage": userimage,
        }
        newlist.append(att_data)
    newlist1 = []
    reco_list = db.session.query(Life).all()  # **用户所有关注
    for recuser in reco_list:
        studiono = recuser.studiono
        username = recuser.user.username
        userimage = recuser.user.userimage
        address = recuser.user.address
        rec_data = {
            "userid": username,
            "userimage": userimage,
            "location":address,
            "studiono":studiono
        }
        newlist1.append(rec_data)
    data = {
        'attentionliving': newlist,
        'recommend': newlist1

    }
    return jsonify(data)


@my_blue.route('/star/',methods=('POST','GET'))    #新星
@is_login
def get_star():
    newlist = []
    newlist1 = []
    new_list = db.session.query(Life).all()
    for i in range(12):
        num = random.choice(new_list)
        newlist1.append(num)
    for newuser in newlist1:
        images = newuser.images
        username = newuser.user.username
        address = newuser.user.address
        vipid = newuser.user.vipid
        labels = newuser.anchorlabel.labels
        studiono = newuser.studiono
        new_data = {
            "image": images,
            "name": username,
            "address": address,
            "vipclass": vipid,
            "labels":labels,
            "studiono":studiono
        }
        newlist.append(new_data)
    data = {
        "status":0,
        "new_data":newlist
    }
    return jsonify(data)


@my_blue.route('/change/', methods=('POST', 'GET'))  # 换
@is_login
def get_change():
    newlist1 = []
    newlist2 = []
    reco_list = db.session.query(Life).all()  # **用户主播
    for i in range(len(reco_list)):
        num = random.choice(reco_list)
        newlist1.append(num)
    print(newlist1)
    for recuser in newlist1:
        username = recuser.user.username
        userimage = recuser.user.userimage
        address = recuser.user.address
        rec_data = {
            "username": username,
            "userimage": userimage,
            "address":address
        }
        newlist2.append(rec_data)
    data = {
        "data":newlist2
    }

    return jsonify(data)



# @my_blue.route('/recommend/', methods=('POST','GET'))  #
# @is_login
# def get_recommend():
#     newlist = []
#     newlist1 = []
#     reco_list = db.session.query(Life).all()  # **
#     for i in range(4):
#         num = random.choice(reco_list)
#         newlist1.append(num)
#     for recommend in newlist1:
#         images = recommend.images
#         username = recommend.user.username
#         address = recommend.user.address
#         vipclass = recommend.user.vipid
#         labels = recommend.anchorlabel.labels
#         studiono = recommend.studiono
#         reco_data = {
#             "image": images,
#             "name": username,
#             "address": address,
#             "vipclass": vipclass,
#             "labels": labels,
#             "studiono": studiono
#         }
#         newlist.append(reco_data)
#
#     newlist2 = []
#     reco_list1 = db.session.query(Life).all()  # **
#     for recuser in reco_list1:
#         studiono = recuser.studiono
#         recname = recuser.user.username
#         recimage = recuser.user.userimage
#         recadd = recuser.user.address
#         rec_data = {
#             "recname": recname,
#             "recimage": recimage,
#             "recadd": recadd,
#             "studiono": studiono
#         }
#         newlist2.append(rec_data)
#     data = {
#         "reco1":newlist1,
#         "reco2":newlist2
#     }
#     return jsonify(data)



@my_blue.route('/onclick/', methods=('POST', 'GET'))
def get_click():
    try:
        req_data = request.get_json()
        userid = req_data['userid']
        user = db.session.query(User).filter(User.userid == userid).first()
        id = user.id
        atteneions = Attention(id=id,userid=userid)
        db.session.add(atteneions)
        db.session.commit()
    except Exception as e:
        print(e)
    data = {
        'status': 0,
        'msg': "插入成功"
    }
    return jsonify(data)


@my_blue.route('/live/', methods=( 'GET',))
def get_live():
    try:
        req_data = request.get_json()
        userid = req_data['userid']
        user = db.session.query(User).filter(User.userid == userid).first()
    except Exception as e:
        print(e)
    data = {
        "stutus":"你瞌睡吗？",
        "data":"主播所有信息"
    }
    return jsonify(data)
















