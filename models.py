from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, \
        String, MetaData, outerjoin, ForeignKey
from sqlalchemy.orm import column_property, sessionmaker

Base = declarative_base()

class UserPublic(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    nick = Column(String, unique=True)

class UserPrivate(Base):
    __tablename__ = "user_private"
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    key = Column(String)
    email = Column(String)

# This doesn't represent a real table in database, but combination (join) of
# "user" and "user_private".
class User(Base):
    __table__ = outerjoin(UserPublic.__table__, UserPrivate.__table__)
    id = column_property(UserPublic.__table__.c.id, UserPrivate.__table__.c.user_id)
