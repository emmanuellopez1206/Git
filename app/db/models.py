from app.db.database import Base
from sqlalchemy import Column,Integer,String,Boolean,DateTime
from datetime import datetime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship 

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    last_name = Column(String)
    address = Column(String)
    phone = Column(Integer)
    email = Column(String, unique=True)
    user_creation = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, default=False)
    sale = relationship("Sale", backref="user", cascade="delete, merge")

class Sale(Base):
    __tablename__ = "sale"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    sale = Column(Integer)
    products_sales = Column(Integer)


    