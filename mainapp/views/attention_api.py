import random
import json

from common import rd1
from mainapp import db

from mainapp.models import Attention, User, Life
from flask import jsonify, request
from flask import Blueprint

my_blue = Blueprint('attention_blue', __name__)


def R_get(tokens):
    userid = rd1.get(tokens)
    return userid


def get_talent():
    data = request.get_data()
    data = json.loads(data)
    if len(data) != 0:
        userid = R_get(data["token"])
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
            userid = talent.user.userid
            talent_data = {
                "username":username,
                "images": images,
                "userid": userid,
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
        # return jsonify(talents_data)
        return talents_data
    else:
        data = {
            'status':0,
            'mag': "没有用户ID"
        }
        return data

def get_near():
    data = request.get_data()
    data = json.loads(data)
    if len(data) != 0:
        userid = R_get(data["token"])
        user = db.session.query(User).filter(User.userid == userid).first()
        newlist2 = []
        newlist3 = []
        near_list = db.session.query(Life).all()
        if user in near_list:
            near_list.remove(user)
        for i in range(12):
            num1 = random.choice(near_list)
            newlist2.append(num1)
        for nearuser in newlist2:
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
            newlist3.append(near_data)
        near_data = {
            'nears': newlist3
        }
        # return jsonify(data)
        return near_data
    else:
        data = {
            'status':0,
            'mag': "没有用户ID"
        }
        return data

def get_attention():
    data = request.get_data()
    data = json.loads(data)
    if len(data) != 0:
        userid = R_get(data["token"])
        user = db.session.query(User).filter(User.userid == userid).first()
        newlist = []
        attent_list = db.session.query(Attention).filter(Attention.id == user.id).all()  # **用户所有关注
        for attention in attent_list:
            id = attention.user.id
            userid = attention.user.userid
            username = attention.user.username
            userimage = attention.user.userimage
            attent_list2 = db.session.query(Life).filter(Life.id == id).all()
            for live in attent_list2:
                studiono = live.studiono
                att_data = {
                    "userid":userid,
                    "studiono": studiono,
                    "username": username,
                    "userimage": userimage,
                }
                newlist.append(att_data)
        newlist1 = []
        reco_list = db.session.query(Life).all()  # **用户所有
        if user in reco_list:
            attent_list.remove(user)
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
        # return jsonify(data)
        return data
    else:
        data = {
            'status':0,
            'mag': "没有用户ID"
        }
        return data

def get_recommend():
    data = request.get_data()
    data = json.loads(data)
    if len(data) != 0:
        userid = R_get(data["token"])
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
        newlist4 = []
        reco_list2 = db.session.query(Life).all()  # **
        if user in reco_list2:
            reco_list.remove(user)
        for i in range(6):
            num1 = random.choice(reco_list)
            newlist4.append(num1)
        for recuser in newlist4:
            studiono = recuser.studiono
            recname = recuser.user.username
            recimage = recuser.user.userimage
            recadd = recuser.user.address
            userid = recuser.user.userid
            rec_data = {
                "userid":userid,
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
        return data
    else:
        data = {
            'status':0,
            'mag': "没有用户ID"
        }
        return data


@my_blue.route('/change', methods=('POST',))  # 换
def get_change():
    data = request.get_data()
    data = json.loads(data)
    if len(data) != 0:
        userid = R_get(data["token"])
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
    else:
        data = {
            'status':0,
            'mag': "没有用户ID"
        }
        return jsonify(data)



@my_blue.route('/home', methods=('POST', ))    #home
def get_pages():

    return jsonify({
        "recommend":get_recommend(),
        'attention': get_attention(),
        'near': get_near(),
        'talent': get_talent(),
    })


@my_blue.route('/talent',methods=('POST',))    #才艺
def newget_talent():
    data1 = get_talent()
    return jsonify(data1)


@my_blue.route('/near',methods=('POST',))   #附近
def newget_near():
    data2 = get_near()
    return jsonify(data2)


@my_blue.route('/recommend', methods=('POST',))   #推荐
def newget_recommend():
    data3 = get_recommend()
    return jsonify(data3)


@my_blue.route('/attention', methods=('POST',))    #关注
def newget_attention():
    data4 = get_attention()
    return jsonify(data4)




@my_blue.route('/onlyatt', methods=('POST',))  # 关注
def get_only():
    data = request.get_json()
    adduserid = data["userid"]
    attentionid = data["attentionid"]
    userself = db.session.query(User).filter(User.userid == adduserid).first()
    newattention = Attention(id = userself.id ,userid=attentionid)
    db.session.add(newattention)
    db.session.commit()
    return jsonify({
        "status":0,
        "msg":"关注成功"
    })










