#!/usr/bin/env python3
""" Module AUTH """

from db import DB
from user import User
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Union


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Creates and saves a new user given an email and a password
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists.".format(email))
        except ValueError:
            raise
        except Exception:
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user


def _hash_password(password: str) -> str:
    """ Returns a hashed password """
    return hashpw(password.encode("utf-8"), gensalt())


def _generate_uuid() -> str:
    """
       Returns a string representation
       of a new UUID.
    """
    return str(uuid.uuid1())
