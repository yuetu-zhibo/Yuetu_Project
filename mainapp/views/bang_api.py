import random
import json
from mainapp import db
from mainapp.models import Attention, Recommend, User, Life
from flask import jsonify, request
from flask import Blueprint

from mainapp.views.attention_api import R_get

my_blue1 = Blueprint('bang_blue', __name__)


def day_bang():
    newlist1 = []
    newlist2 = []
    bang_list = db.session.query(Life).filter(Life.charisma).all()
    for i in range(10):
        num = random.choice(bang_list)
        charisma1 = num.charisma
        newlist1.append(charisma1)
    newlist3 = sorted(newlist1,reverse=True)
    for j in range(10):
        banguser = db.session.query(Life).filter(Life.charisma == newlist3[j]).first()
        images = banguser.user.userimage
        username = banguser.user.username
        charisma = banguser.charisma
        vipclass = banguser.user.vipid
        userid = banguser.user.userid
        data = {
            "userid":userid,
            "images":images,
            "username":username,
            "charisma":charisma,
            "vipclass":vipclass
        }
        newlist2.append(data)

    return newlist2


def week_bang():
    newlist1 = []
    newlist2 = []
    bang_list = db.session.query(Life).filter(Life.charisma).all()
    for i in range(10):
        num = random.choice(bang_list)
        charisma1 = num.charisma
        newlist1.append(charisma1)
    newlist3 = sorted(newlist1,reverse=True)
    for j in range(10):
        banguser = db.session.query(Life).filter(Life.charisma == newlist3[j]).first()
        images = banguser.user.userimage
        username = banguser.user.username
        charisma = banguser.charisma
        vipclass = banguser.user.vipid
        userid = banguser.user.userid
        data = {
            "userid":userid,
            "images":images,
            "username":username,
            "charisma":charisma,
            "vipclass":vipclass
        }
        newlist2.append(data)

    return newlist2


def month_bang():
    newlist1 = []
    newlist2 = []
    bang_list = db.session.query(Life).filter(Life.charisma).all()
    for i in range(10):
        num = random.choice(bang_list)
        charisma1 = num.charisma
        newlist1.append(charisma1)
    newlist3 = sorted(newlist1,reverse=True)
    for j in range(10):
        banguser = db.session.query(Life).filter(Life.charisma == newlist3[j]).first()
        images = banguser.user.userimage
        username = banguser.user.username
        charisma = banguser.charisma
        vipclass = banguser.user.vipid
        userid = banguser.user.userid
        data = {
            "userid":userid,
            "images":images,
            "username":username,
            "charisma":charisma,
            "vipclass":vipclass
        }
        newlist2.append(data)

    return newlist2



@my_blue1.route('/bang/', methods=('GET', ))    #榜
def get_bang():
    rich_data = {
        "day": day_bang(),
        'week': week_bang(),
        'month': month_bang()
    }
    luck_data = {
        "day": day_bang(),
        'week': week_bang(),
        'month': month_bang()
    }
    star_data = {
        "day": day_bang(),
        'week': week_bang(),
        'month': month_bang()
    }
    return jsonify(rich_data,luck_data,star_data)


my_blueindex = Blueprint('/Total/',__name__)
@my_blueindex.route('/total/', methods=('GET',))
def get_total():
    data = request.args.get('token')
    if R_get(data):
        return jsonify({
            'status':1,
            "msg": "token存在！"
        })
    else:
        return jsonify({
            'status':0,
            "msg":"token不存在！"
        })





