import random
from mainapp import db
from middleware.valid_login import is_login
from mainapp.models import *
from flask import jsonify, request
from flask import Blueprint


my_blue = Blueprint('attention_blue', __name__)


@my_blue.route('/talent/',methods=('POST',))    #才艺
def get_talent():
    data = request.get_json()
    userid = data["userid"]
    user = db.session.query(User).filter(User.userid == userid).first()
    newlist1 = []
    newlist2 = []
    tanlent_list = db.session.query(Life).all()
    if user in tanlent_list:
        tanlent_list.remove(user)
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
            "username":username,
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


@my_blue.route('/near/',methods=('POST',))   #附近
def get_near():
    data = request.get_json()
    userid = data["userid"]
    user = db.session.query(User).filter(User.userid == userid).first()
    newlist1 = []
    near_list = db.session.query(Life).all()
    if user in near_list:
        near_list.remove(user)
    for nearuser in near_list:
        userids = nearuser.user.userid
        images = nearuser.images
        username = nearuser.user.username
        address = nearuser.user.address
        vipid = nearuser.user.vipid
        labels = nearuser.anchorlabel.labels
        studiono = nearuser.studiono
        near_data = {
            "userid":userids,
            "images": images,
            "username": username,
            "location": address,
            "vipclass": vipid,
            "tag":labels,
            "studiono":studiono
        }
        newlist1.append(near_data)
    data = {
        'nears': newlist1
    }
    return jsonify(data)


@my_blue.route('/attention/', methods=('POST',))  # 关注
def get_attention():
    data = request.get_json()
    userid = data["userid"]
    user = db.session.query(User).filter(User.userid == userid).first()
    newlist = []
    attent_list = db.session.query(Attention).filter(Attention.id == user.id).all()  # **用户所有关注
    for attention in attent_list:
        id = attention.user.id
        userid = attention.user.userid
        username = attention.user.username
        userimage = attention.user.userimage
        # attent_list2 = db.session.query(Life).filter(Life.id == id).all()
        # for live in attent_list2:
        #     studiono = live.studiono
        att_data = {
            "userid":userid,
            # "studiono": studiono,
            "username": username,
            "userimage": userimage,
        }
        newlist.append(att_data)
    newlist1 = []
    reco_list = db.session.query(Life).all()  # **用户所有
    if user in reco_list:
        attent_list.remove(user)
    # if attention in reco_list:
    #     reco_list.remove(attention)
    for recuser in reco_list:
        userid = recuser.user.userid
        studiono = recuser.studiono
        username = recuser.user.username
        userimage = recuser.user.userimage
        address = recuser.user.address
        rec_data = {
            "userid":userid,
            "username": username,
            "userimage": userimage,
            "location": address,
            "studiono": studiono
        }
        newlist1.append(rec_data)
    data = {
        'attentionliving': newlist,
        'recommend': newlist1

    }
    return jsonify(data)


@my_blue.route('/star/',methods=('POST',))    #新星
def get_star():
    data = request.get_json()
    userid = data["userid"]
    user = db.session.query(User).filter(User.userid == userid).first()
    newlist = []
    newlist1 = []
    new_list = db.session.query(Life).all()
    if user in newlist:
        newlist.remove(user)
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


@my_blue.route('/change/', methods=('POST',))  # 换
def get_change():
    data = request.get_json()
    userid = data["userid"]
    user = db.session.query(User).filter(User.userid == userid).first()
    newlist1 = []
    newlist2 = []
    reco_list = db.session.query(Life).all()  # **用户主播
    if user in reco_list:
        reco_list.remove(user)
    for i in range(6):
        num = random.choice(reco_list)
        newlist1.append(num)
    for recuser in newlist1:
        userid = recuser.user.userid
        username = recuser.user.username
        userimage = recuser.user.userimage
        address = recuser.user.address
        studiono = recuser.studiono
        rec_data = {
            "userid": userid,
            "username": username,
            "userimage": userimage,
            "location": address,
            "studiono": studiono
        }
        newlist2.append(rec_data)
    data = {
        "data":newlist2
    }

    return jsonify(data)


@my_blue.route('/recommend/', methods=('POST',))  #
def get_recommend():
    data = request.get_json()
    userid = data["userid"]
    user = db.session.query(User).filter(User.userid == userid).first()
    newlist = []
    newlist1 = []
    reco_list = db.session.query(Life).all()  # **
    if user in reco_list:
        reco_list.remove(user)
    for i in range(4):
        num = random.choice(reco_list)
        newlist1.append(num)
    for recommend in newlist1:
        users = recommend.user.userid
        images = recommend.images
        username = recommend.user.username
        address = recommend.user.address
        vipclass = recommend.user.vipid
        labels = recommend.anchorlabel.labels
        studiono = recommend.studiono
        reco_data = {
            "userid":users,
            "images": images,
            "username": username,
            "location": address,
            "vipclass": vipclass,
            "tag": labels,
            "studiono": studiono
        }
        newlist.append(reco_data)

    newlist2 = []
    reco_list1 = db.session.query(Life).all()  # **
    for recuser in reco_list1:
        studiono = recuser.studiono
        recname = recuser.user.username
        recimage = recuser.user.userimage
        recadd = recuser.user.address
        rec_data = {
            "username": recname,
            "images": recimage,
            "location": recadd,
            "studiono": studiono
        }
        newlist2.append(rec_data)
    bannerlist = [
        'https://hgcdn.handouzb.com/201919/1557474748c9c678.jpg',
        'https://hgcdn.handouzb.com/201947/15743220717c07ed.jpg',
        'https://hgcdn.handouzb.com/201910/155194952885d802.jpg',
        'https://hgcdn.handouzb.com/20180312/152152963868733e.jpg',
        'https://hgcdn.handouzb.com/201852/1545630525d9045c.jpg',
        'https://hgcdn.handouzb.com/201851/1545371917d7e402.jpg',
        'https://hgcdn.handouzb.com/201926/1561598046e687f6.jpg',
        'https://hgcdn.handouzb.com/201936/156739308802de66.jpg',
        'https://hgcdn.handouzb.com/201921/155850535063d820.jpg',
        'https://hgcdn.handouzb.com/20181250/1544692506a9a510.jpg'
    ]

    newlist3 = []
    for i in bannerlist:
        dict2 = {}
        dict2["img"]=i
        newlist3.append(dict2)
    data = {
        "banner":newlist3,
        "specialrecommend":newlist,
        "generalrecommend":newlist2
    }
    return jsonify(data)

@my_blue.route('/onclick/', methods=('POST',))  # 关注
def get_click():
    data = request.get_json()
    userid = data["userid"]
    user = db.session.query(User).filter(User.userid == userid).first()
    newlist = []
    attent_list = db.session.query(Attention).filter(Attention.id == user.id).all()  # **用户所有关注
    for attention in attent_list:
        newlist.append(attention)

    newlist1 = []
    reco_list = db.session.query(Life).all()  # **用户所有
    if user in reco_list:
        attent_list.remove(user)
    for i in range(6):
        num = random.choice(attent_list)
        newlist1.append(num)
    for recuser in reco_list:
        userid = recuser.user.userid
        studiono = recuser.studiono
        username = recuser.user.username
        userimage = recuser.user.userimage
        address = recuser.user.address
        rec_data = {
            "userid":userid,
            "username": username,
            "userimage": userimage,
            "location": address,
            "studiono": studiono
        }
        newlist1.append(rec_data)
    data = {
        'recommend': newlist1
    }
    return jsonify(data)


@my_blue.route('/live/', methods=( 'POST',))
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
















