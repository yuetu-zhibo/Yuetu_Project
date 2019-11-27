from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


_engine = create_engine("mysql+pymysql://root:root@39.98.126.184:3306/yuetu")
_engine.connect()

_Session = sessionmaker(bind=_engine)

session = _Session()