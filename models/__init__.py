# _*_ coding:utf-8 _*_
__author__ = 'caimiao'
__date__ = '15-5-5'


from config import DEBUG_MODE, MYSQL_MASTER_HOST, MYSQL_MASTER_DB, MYSQL_MASTER_USER, MYSQL_MASTER_PWD
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


mysql_master_engine = create_engine("mysql://%s:%s@%s/%s?charset=utf8" %\
                              (MYSQL_MASTER_USER, MYSQL_MASTER_PWD, MYSQL_MASTER_HOST, MYSQL_MASTER_DB),
                                    pool_size=100, pool_recycle=3600, echo=DEBUG_MODE)


_mysql_master_factory = scoped_session(sessionmaker(bind=mysql_master_engine))

db_session = _mysql_master_factory()