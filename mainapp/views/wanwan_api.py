# from mainapp import db
# from mainapp.serializer import dumps
# from mainapp.models import User, Attention, Life
# from flask import redirect, request
# from flask import Blueprint
# from flask import jsonify
# blue7 = Blueprint('click_blue', __name__)
#
# @blue7.route('/onclick/',methods=('POST','GET'))   #
# def index():
#     # req_data = request.get_json()
#     # userid =  req_data['userid']
#     # id = 1
#     # user = db.session.query(User).filter(User.userid == userid).first()
#     # atteneions = Attention(id=id,userid=userid)
#     # db.session.add(atteneions)
#     # db.session.commit()
#     newlist = []
#     click_list = db.session.query(Attention).filter_by(id=1).all()  # **用户所有关注
#     for attention in click_list:
#         id = attention.user.id
#         userid = attention.user.userid
#         username = attention.user.username
#         userimage = attention.user.userimage
#         attent_list2 = db.session.query(Life).filter_by(id=id).all()
#         for live in attent_list2:
#             studiono = live.studiono
#         att_data = {
#             "userid":userid,
#             "studiono": studiono,
#             "username": username,
#             "userimage": userimage,
#         }
#         newlist.append(att_data)
#         data = {
#             'attentionliving': newlist
#
#         }
#     return jsonify(data)


# # # import random
# #
# import db
# from db.serializor import dumps
# from shouye.models import User, Life
# from flask import jsonify
# from flask import Blueprint
#
#
# blue9 = Blueprint('wan_blue', __name__)
#
# @blue9.route('/wan/', methods=('POST','GET'))  # 关注
# def attent():
#     newlist2 = []
#     near_list = db.session.query(Life).all()
#     for nearuser in near_list:
#
#     newlist = []
#     newlist2 = []
#     talent_list = db.session.query(Life.charisma).all()
#     for i in talent_list:
#         newlist.extend(i)
#         newlist.reverse()
#         for j in range(len(newlist)):
#             a = db.session.query(Life).filter_by(charisma=j).all()
#             for user in a:
#                 l_image = user.userimage
#                 l_name = user.username
#                 l_address = user.address
#                 l_vipclass = user.vipid
#                 near_data = {
#                     "image": l_image,
#                     "name": l_name,
#                     "address": l_address,
#                     "vipclass": l_vipclass
#                 }
#                 newlist2.append(near_data)
#         return jsonify(newlist2)
# # req_data = request.get_json()
#     # useid = req_data['userid']
#     # near_lisq_data.t = db.session.query()
#     # list1 = []
#     # talent_list = db.session.query(User).limit(12).all()  # **所有附近主播
#     # for i in talent_list:
#     #     j = dumps(i)
#     #     hh = j
#     #     list1.append(hh)
#     # return jsonify({
#     #     "data": [
#     #         [list1[0]["address"],list1[0]["userimage"],list1[0]["username"],list1[0]["userid"],list1[0]["vipid"]],
#     #         [list1[1]["address"], list1[1]["userimage"], list1[1]["username"], list1[1]["userid"], list1[1]["vipid"]],
#     #         [list1[2]["address"], list1[2]["userimage"], list1[2]["username"], list1[2]["userid"], list1[2]["vipid"]],
#     #         [list1[3]["address"], list1[3]["userimage"], list1[3]["username"], list1[3]["userid"], list1[3]["vipid"]],
#     #         [list1[4]["address"], list1[4]["userimage"], list1[4]["username"], list1[4]["userid"], list1[4]["vipid"]],
#     #         [list1[5]["address"], list1[5]["userimage"], list1[5]["username"], list1[5]["userid"], list1[5]["vipid"]]
#     #
#     #     ]
#     # })
#
#   # for nearuser in near_list:
#   #       r_vipid = nearuser.vipid
#   #       r_username = nearuser.username
#   #       r_userimage = nearuser.userimage
#   #       r_address = nearuser.address
#   #
#   #       near_data = {
#   #           "username":r_username,
#   #           "userimage":r_userimage,
#   #           "address":r_address,
#   #           "vipid": r_vipid
#   #       }
#   #
#   #       newlist.append(near_data)
#   #       print(near_data)
#   #   return jsonify(newlist)
#
#   data = request.get_json()
#         userid = data["userid"]
#         user = db.session.query(User).filter_by(userid=userid).first()
#         id = user.id
#         attents = db.session.query(Attention).filter_by(id=id).all()
# # import random
# #
# import random
#
# import db
# from db.serializor import dumps
# from middleware.valid_login import is_login
#
# from shouye.models import Attention, Recommend, User, Life
# from flask import jsonify, request
# from flask import Blueprint
#
# ue3 = Blueprint('guan_blue', __name__)
#
#
# @blue3.route('/attention/', methods=('POST', 'GET'))  # 关注
# # @is_login
# def attent():
#     try:
#         data = request.get_json()
#         userid = data["userid"]
#         print("接受到的ID:",userid)
#         user = db.session.query(User).filter_by(userid=userid).first()
#         id = user.id
#         print("user.id",id)
#         newlist = []
#         attent_list = db.session.query(Attention).filter_by(id=id).all()  # **用户所有关注
#         for attention in attent_list:
#             id = attention.user.id
#             userid = attention.user.userid
#             username = attention.user.username
#             userimage = attention.user.userimage
#             # attent_list2 = db.session.query(Life).filter_by(id=id).all()
#             # for live in attent_list2:
#             #     studiono = live.studiono
#             att_data = {
#                 "userid":userid,
#                 # "studiono": studiono,
#                 "username": username,
#                 "userimage": userimage,
#             }
#             newlist.append(att_data)
#         # newlist1 = []
#         # reco_list = db.session.query(Life).all()  # **用户所有关注
#         # for recuser in reco_list:
#         #     studiono = recuser.studiono
#         #     username = recuser.user.username
#         #     userimage = recuser.user.userimage
#         #     address = recuser.user.address
#         #     rec_data = {
#         #         "userid": username,
#         #         "userimage": userimage,
#         #         "location":address,
#         #         "studiono":studiono
#         #     }
#         #     newlist1.append(rec_data)
#         data = {
#             'attentionliving': newlist,
#             # 'recommend': newlist1
#
#         }
#     except Exception as e:
#         print(e)
#
#         return jsonify(data)
#
#
# bl