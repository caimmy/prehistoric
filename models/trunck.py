# _*_ coding:utf-8 _*_
__author__ = 'caimiao'
__date__ = '15-5-5'


from sqlalchemy import Column, Integer, String, DateTime, Enum, CHAR, Text
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    '''
    用户表
    '''
    __tablename__ = 'arch_user'

    id          = Column(Integer, primary_key=True, autoincrement=True)
    name        = Column(String(32), nullable=False)
    email       = Column(String(128), nullable=False)
    create_tm   = Column(DateTime, default=datetime.now())
    pwd         = Column(String(32))
    salt        = Column(String(32))
    avatar      = Column(String(256))

    def __repr__(self):
        return "<<Table User> name:%s, email:%s>" % (self.name, self.email)

class Settlement(Base):
    '''
    聚落点
    '''
    __tablename__ = 'arch_settlement'

    id          = Column(Integer, primary_key=True, autoincrement=True)
    name        = Column(String(128), nullable=False)
    desc        = Column(Text)
    ref         = Column(String(256))                   # 来源


class GeoPoint(Base):
    '''
    地理坐标
    '''
    __tablename__ = 'arch_geo_point'

    id          = Column(Integer, primary_key=True, autoincrement=True)
    longitude   = Column(String(64), nullable=False)
    latitude    = Column(String(64), nullable=False)
    height_l    = Column(Integer)                       # 高度的低点
    height_h    = Column(Integer)                       # 高度的高点
    area        = Column(Integer)                       # 面积（平方米）
    belong      = Column(Integer, nullable=False)       # 所属聚落点


