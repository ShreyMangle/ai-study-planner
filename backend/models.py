from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    learning_style = Column(String)
    pace_factor = Column(Float)
    peak_hours = Column(String)


class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    difficulty = Column(Integer)
    confidence = Column(Integer)
    deadline_days = Column(Integer)
    weight = Column(Float)
