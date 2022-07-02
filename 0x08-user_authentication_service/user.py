#!/usr/bin/env python3
""" User model """
from cgitb import reset
import sqlalchemy import Column, Integer, String
from sqlalchemy
Base = declarative_base()

class User(Base):
    """ Class user """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))