# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Anchorlabel(Base):
    __tablename__ = 'anchorlabels'

    labelsid = Column(Integer, primary_key=True)
    labels = Column(String(20), nullable=False)


class Attention(Base):
    __tablename__ = 'attentions'

    attentionid = Column(Integer, primary_key=True)
    id = Column(ForeignKey('user.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    userid = Column(Integer, nullable=False)

    user = relationship('User', primaryjoin='Attention.id == User.id', backref='attentions')


class Audience(Base):
    __tablename__ = 'audiences'

    id = Column(Integer, primary_key=True)
    rec_id = Column(ForeignKey('lives.rec_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    userid = Column(String(20), nullable=False)
    speak = Column(Integer)

    rec = relationship('Life', primaryjoin='Audience.rec_id == Life.rec_id', backref='audiences')


class Backpack(Base):
    __tablename__ = 'backpacks'

    id = Column(ForeignKey('user.id', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False)
    giftid = Column(String(20), primary_key=True, nullable=False)
    auotograph = Column(String(20))
    userid = Column(String(20), primary_key=True, nullable=False)

    user = relationship('User', primaryjoin='Backpack.id == User.id', backref='backpacks')


class Blacklist(Base):
    __tablename__ = 'blacklists'

    blackid = Column(Integer, primary_key=True)
    id = Column(ForeignKey('user.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    userneid = Column(String(20), nullable=False)

    user = relationship('User', primaryjoin='Blacklist.id == User.id', backref='blacklists')


class Celebrity(Base):
    __tablename__ = 'celebrity'

    id = Column(Integer, primary_key=True)
    rec_id = Column(ForeignKey('lives.rec_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    charisma = Column(String(20))

    rec = relationship('Life', primaryjoin='Celebrity.rec_id == Life.rec_id', backref='celebrities')


class DjangoContentType(Base):
    __tablename__ = 'django_content_type'
    __table_args__ = (
        Index('django_content_type_app_label_model_76bd3d3b_uniq', 'app_label', 'model'),
    )

    id = Column(Integer, primary_key=True)
    app_label = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)


class DjangoMigration(Base):
    __tablename__ = 'django_migrations'

    id = Column(Integer, primary_key=True)
    app = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    applied = Column(DateTime, nullable=False)


class DjangoSession(Base):
    __tablename__ = 'django_session'

    session_key = Column(String(40), primary_key=True)
    session_data = Column(String, nullable=False)
    expire_date = Column(DateTime, nullable=False, index=True)


class Gift(Base):
    __tablename__ = 'gifts'

    id = Column(Integer, primary_key=True)
    giftname = Column(String(20), nullable=False)
    giftprice = Column(String(20), nullable=False)
    image = Column(String(256), nullable=False)


class Good(Base):
    __tablename__ = 'good'

    id = Column(Integer, primary_key=True)
    anchorid = Column(String(20), nullable=False)


class Liveadmin(Base):
    __tablename__ = 'liveadmin'

    id = Column(Integer, primary_key=True)
    rec_id = Column(ForeignKey('lives.rec_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    user_id = Column(String(20), nullable=False)

    rec = relationship('Life', primaryjoin='Liveadmin.rec_id == Life.rec_id', backref='liveadmins')


class Life(Base):
    __tablename__ = 'lives'

    rec_id = Column(Integer, primary_key=True)
    studiono = Column(String(20), nullable=False)
    id = Column(ForeignKey('user.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    labelsid = Column(ForeignKey('anchorlabels.labelsid', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    gifts = Column(String(20))
    images = Column(String(256), nullable=False)
    charisma = Column(Integer)

    user = relationship('User', primaryjoin='Life.id == User.id', backref='lives')
    anchorlabel = relationship('Anchorlabel', primaryjoin='Life.labelsid == Anchorlabel.labelsid', backref='lives')


class Nearanchor(Base):
    __tablename__ = 'nearanchor'

    fuid = Column(Integer, primary_key=True)
    id = Column(ForeignKey('user.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    anchorid = Column(String(20), nullable=False)

    user = relationship('User', primaryjoin='Nearanchor.id == User.id', backref='nearanchors')


class Newstar(Base):
    __tablename__ = 'newstars'

    id = Column(Integer, primary_key=True)
    rec_id = Column(ForeignKey('lives.rec_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    charisma = Column(String(20), nullable=False)
    classification = Column(Integer, nullable=False)

    rec = relationship('Life', primaryjoin='Newstar.rec_id == Life.rec_id', backref='newstars')


class Recommend(Base):
    __tablename__ = 'recommends'

    id = Column(Integer, primary_key=True)
    rec_id = Column(ForeignKey('lives.rec_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    charisma = Column(String(20), nullable=False)

    rec = relationship('Life', primaryjoin='Recommend.rec_id == Life.rec_id', backref='recommends')


class Reegister(Base):
    __tablename__ = 'reegisters'

    registerid = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    password = Column(String(50), nullable=False)


class Rich(Base):
    __tablename__ = 'richs'

    id = Column(Integer, primary_key=True)
    anchorid = Column(String(20), nullable=False)
    balance = Column(String(20))


class Superuser(Base):
    __tablename__ = 'superusers'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    realname = Column(String(50))
    password = Column(String(100), nullable=False)
    sex = Column(String(20))
    card = Column(String(18))
    position = Column(String(80))
    email = Column(String(50))
    phone = Column(String(11))


class Talent(Base):
    __tablename__ = 'talents'

    tid = Column(Integer, primary_key=True)
    rec_id = Column(ForeignKey('lives.rec_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    anchorid = Column(String(20), nullable=False)

    rec = relationship('Life', primaryjoin='Talent.rec_id == Life.rec_id', backref='talents')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    vipid = Column(ForeignKey('viptables.vipid', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    userid = Column(String(20), nullable=False)
    username = Column(String(20))
    sex = Column(String(20))
    password = Column(String(100))
    paper = Column(String(18))
    balance = Column(String(20))
    userimage = Column(String(256))
    birth = Column(String(20))
    autograph = Column(String(150))
    telphone = Column(String(11))
    address = Column(String(20))
    realname = Column(String(50))

    viptable = relationship('Viptable', primaryjoin='User.vipid == Viptable.vipid', backref='users')


class Userfan(Base):
    __tablename__ = 'userfans'

    fansid = Column(Integer, primary_key=True)
    id = Column(ForeignKey('user.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    flower_user_id = Column(String(20), nullable=False)

    user = relationship('User', primaryjoin='Userfan.id == User.id', backref='userfans')


class Viptable(Base):
    __tablename__ = 'viptables'

    vipid = Column(Integer, primary_key=True)
    vipclass = Column(String(20), nullable=False)
