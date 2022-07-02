#!/usr/bin/env python3
""" Module AUTH """

from db import DB
from user import User
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> str:
    """ Returns a hashed password """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
       Returns a string representation
       of a new UUID.
    """
    return str(uuid.uuid1())
