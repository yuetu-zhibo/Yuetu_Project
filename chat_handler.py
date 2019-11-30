#coding=utf-8
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.websocket import WebSocketHandler

from mainapp import db
from mainapp.models import User, Viptable

all_handlers = {}  # 用来存储与客户端交互的ChatHandler对象


class ChatHandler(WebSocketHandler):  # 服务端支持WebSocket协议
    def open(self, *args, **kwargs):
        userid = self.get_query_argument('userid')  # 用户id
        user = db.session.query(User).filter(User.userid == userid).first()
        vipid = user.vipid
        vip = db.session.query(Viptable).filter(Viptable.vipid == vipid).first()
        vipclass = vip.vipclass
        username = user.username
        studiono = self.get_query_argument('studiono')  # 房间id
        self.studiono = studiono
        self.username = username
        self.vipclass = vipclass

        if studiono not in all_handlers.keys():
            all_handlers[studiono] = set()

        all_handlers[studiono].add((username, self))
        self.send_msg('欢迎%s加入直播间' % username)

    def on_message(self, message):
        self.message = message
        self.send_msg('%s:%s:%s' % (self.vipclass, self.username, self.message))

    def send_msg(self, msg):
        for username, handler in all_handlers[self.studiono]:
            handler.write_message(msg)

    def check_origin(self, origin):
        return True


app = Application([
    (r'/chat/', ChatHandler)
], )
app.listen(8888)
IOLoop.instance().start()
