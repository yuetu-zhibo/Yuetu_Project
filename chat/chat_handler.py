import os

# from flask import request
from flask import request, jsonify, json
from tornado.websocket import WebSocketHandler
from tornado.web import Application
# from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

# from myloginapp.models import Life, User


# class IndexHandler(RequestHandler):
#     def get(self, *args, **kwargs):
#         # data = request.get_json()
#         # studiono = data.get('studiono')
#         # userid = data.get('userid')
#         userid = self.get_query_argument('userid')
#         studiono = self.get_query_argument('studiono')
#         self.render("chat_room.html",userid=userid, studiono=studiono)


# chat_handlers = set()  # 用来存储与客户端交互的ChatHandler对象
from mainapp import db
from mainapp.models import User, Viptable

all_handlers = {}


class ChatHandler(WebSocketHandler):  # 服务端支持WebSocket协议
    def open(self, *args, **kwargs):
        # data = request.get_json()
        # print(data)
        # studiono = data.get('studiono')
        # userid = data.get('userid')
        userid = self.get_query_argument('userid') # 用户id

        user = db.session.query(User).filter(User.userid == userid).first()
        vipid = user.vipid
        vip = db.session.query(Viptable).filter(Viptable.vipid == vipid).first()
        vipclass = vip.vipclass
        username = user.username
        print(username)
        studiono = self.get_query_argument('studiono')  # 房间id
        print(studiono)
        self.studiono = studiono
        self.username = username
        self.vipclass = vipclass
        # self.userid = userid

        if studiono not in all_handlers.keys():
            all_handlers[studiono] = set()

        all_handlers[studiono].add((username, self))
        self.send_msg('欢迎%s加入直播间' % username)

    def on_message(self, message):
        self.message = message
        self.send_msg('%s:%s:%s' % (self.vipclass,self.username, self.message))

        print(self.username, "正在发消息！")
        print(self.message)
        print(self.vipclass)

    # def on_close(self):
    #     all_handlers[self.studiono].remove(self)   # 从集合中移除
    #     [handler.write_message("%s下线了！" % (self.userid,)) for handler in all_handlers[self.studiono]]

    def send_msg(self, msg):
        for username, handler in all_handlers[self.studiono]:
            handler.write_message(msg)

    def check_origin(self, origin):
        return True


# settings = {
#     "template_path": os.path.join(os.getcwd(), 'templates'),
#     "static_path": os.path.join(os.getcwd(), 'chat_static'),
#     "debug": True
# }
app = Application([
    # (r'/index/', IndexHandler),
    (r'/chat/', ChatHandler)
], )
# **settings
app.listen(8888)
IOLoop.instance().start()
