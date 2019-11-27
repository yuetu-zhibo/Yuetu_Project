from flask import Blueprint, request, jsonify

from mainapp import db

from mainapp.models import User, Gift

gift_blue = Blueprint('blue3', __name__)


@gift_blue.route('/gift/', methods=('GET',))
def audience():
    new_list = []
    # 礼物清单接口
    gift_list = db.session.query(Gift).all()
    for gift in gift_list:
        image = gift.image
        giftname = gift.giftname
        giftprice = gift.giftprice
        gift_data = {
            "image":image,
            "giftname":giftname,
            "giftprice":giftprice
        }
        # print(gift_data)
        new_list.append(gift_data)
    data = {
        'new': new_list
    }
    gifts = {
        'status': 1,
        'msg': "成功~~~",
        'data': data
    }
    return jsonify(gifts)
