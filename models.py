from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database import Base
import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    social_id = Column(String, nullable=False, unique=True)
    name = Column(String)
    profile_image_url = Column(String)
    is_blocked = Column(Boolean, default=False)
    is_subscribed = Column(Boolean, default=False)
    created_time = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, social_id, name, profile_image_url):
        self.social_id = social_id
        self.name = name
        self.profile_image_url = profile_image_url

    def __repr__(self):
        return '<User %r>' % (self.name)