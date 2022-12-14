import functools
import re
from glob import escape
from random import getrandbits
from urllib import response
from flask import (
    Blueprint, g, redirect, request, session, url_for
)
from .config import login_user
from db import db
from db.models.user import UserData

from generated.login.LoginRequest import LoginRequest
from generated.logout.LogoutRequest import LogoutRequest
from generated.register.RegisterRequest import RegisterRequest
# from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/user')

# function for testing
# @auth_bp.route("/<user>")
# def userGreet(user):
#     return f'''
#         <p>Hello, {escape(user)}!</p>
#     '''


@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    responseData = {}
    responseData['code'] = 404

    if request.method == 'POST':
        requestData = LoginRequest(request)

        # use api gen get object of request
        username = requestData.userName
        password = requestData.password
        print('User, ', username, password)

        error = None
        # verifications
        if not userIsExisted(username):
            error = 'user not found'
            responseData['code'] = 1
        elif not passwordVerified(username, password):
            error = 'wrong password'
            responseData['code'] = 2
        elif userIsLogged(username):
            error = 'login already'
            responseData['code'] = 3

        if error is None or error == 'login already':
            # verified, login user
            print('Verified')
            temp_session = loginUser(username)
            responseData['code'] = 0
            responseData['session'] = temp_session

            # return redirect(url_for('auth.userGreet', user=username))
        else:
            print(error)
            responseData['session'] = None

    return responseData

    # return '''
    #     <form method="post">
    #         <h2>Login</h2>
    #         <p>User Name: <input type=text name=username></p>
    #         <p>Password: <input type=password name=password></p>
    #         <p><input type=submit name=submit_button value=login></p>
    #     <form>
    # '''


@auth_bp.route("/register", methods=['GET', 'POST'])
def register():
    responseData = {}
    responseData['code'] = 404

    if request.method == 'POST':

        requestData = RegisterRequest(request)
        username = requestData.userName
        password = requestData.password
        print('User, ', username, password)
        error = None

        # verifications
        if not UsernameIsLegal(username):
            error = 'invaild username'
            responseData['code'] = 10
        elif not PasswordIsLegal(password):
            error = 'invaild password'
            responseData['code'] = 20

        elif userIsExisted(username):
            error = 'user existed'
            responseData['code'] = 11

        if error is None:
            # verified, register user
            addUser(username, password)
            temp_session = loginUser(username)
            responseData['code'] = 0
            responseData['session'] = temp_session

            # return redirect(url_for('auth.userGreet', user=username))
        else:
            print(error)
            responseData['session'] = None

    return responseData
    # return '''
    #     <form method="post">
    #         <h2>Register</h2>
    #         <p>User Name: <input type=text name=username></p>
    #         <p>Password: <input type=password name=password></p>
    #         <p><input type=submit name=submit_button value=register></p>
    #     <form>
    # '''


# Verifications

def userIsExisted(username):
    user = db.session.query(UserData).filter_by(name=username).first()
    return True if user else False


def UsernameIsLegal(username):
    username_rule = r'^[A-Za-z\d_]{3,32}$'
    matching = re.fullmatch(username_rule, username)
    return True if matching else False


def PasswordIsLegal(password):
    p = r"^[A-Za-z\d~`!@#$%^&*()_\-+=\[\]\{\}|:;<>]{6,32}"
    matching = re.fullmatch(p, password)
    return True if matching else False


# user data interactions

def passwordVerified(username, password):
    user = db.session.query(UserData).filter_by(name=username).first()
    return True if password == user.password else False


def addUser(username, password):
    # Add user to database
    new_user = UserData(username, password)
    db.session.add(new_user)
    db.session.commit()
    print('New user created')
    return


def getGeneratedSession(user_id):
    for session, id in login_user.items():
        if id == user_id:
            return session
    return hex(getrandbits(128))


# log in and out methods modifying session

def loginUser(username):
    current_user = db.session.query(UserData).filter_by(name=username).first()
    if current_user:
        session['currentUserId'] = current_user.id
        temp_session = getGeneratedSession(current_user.id)
        login_user[temp_session] = current_user.id
        # print('user', username, 'login!')
        # print('session', temp_session)
    else:
        # raise error: undefined user
        print('undefined user')
        temp_session = None
    return temp_session


def userIsLogged(username):
    # Bug: user could be covered by other login users
    current_user = db.session.query(UserData).filter_by(name=username).first()
    if current_user:
        if current_user.id in login_user.values():
            return True
    return False


@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    responseData = {}
    responseData['code'] = -1
    responseData['userName'] = None
    if request.method == 'POST':
        requestData = LogoutRequest(request)
        session = requestData.session
        print('logout session', session)
        if (login_user.get(session)):
            login_user.pop(session)
            print('{} logged out successfully!'.format(
                requestData.userName))
            responseData['code'] = 0
            responseData['userName'] = requestData.userName
    return responseData


'''
    decorators and methods below is used for preventing accesses without logged.
'''


@auth_bp.before_app_request
def loadLoggedInUser():
    user_id = session.get('currentUserId')

    if user_id is None:
        g.user = None
    else:
        # get user from datebase and store into g.user for loginRequired
        g.user = user_id
    return


def loginRequired(view):
    @functools.wraps(view)
    def wrapped_view(**kw):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kw)
    return wrapped_view(view)
