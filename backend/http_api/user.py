import functools
import re
from glob import escape
from random import getrandbits
from urllib import response
from flask import (
    Blueprint, g, redirect, request, session, url_for
)
from db import db
from db.models.user import UserData

user_bp = Blueprint('auth', __name__, url_prefix='/user')


class User:
    # username
    # id
    # card[]
    # template[]
    pass
