import functools
from glob import escape
from random import getrandbits
from multiprocessing.spawn import import_main_path
from flask import (
    Blueprint, flash, g, redirect, request, session, url_for
)
from db import db
from db.models.user import UserData

from generated.login.LoginRequest import LoginRequest
from generated.register.RegisterRequest import RegisterRequest
# from werkzeug.security import check_password_hash, generate_password_hash

login_user = {}
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

        if error is None:
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
    return True if username else False


def PasswordIsLegal(password):
    return True if password else False


# user data interactions

def passwordVerified(username, password):
    user = db.session.query(UserData).filter_by(name=username).first()
    if password == user.password:
        return True
    return False


def addUser(username, password):
    # Add user to database
    new_user = UserData(username, password)
    db.session.add(new_user)
    db.session.commit()
    print('New user created')
    return


def getGeneratedSession(username):
    ss = login_user.get(username)
    if ss is None:
        return hex(getrandbits(128))
    return ss


# log in and out methods modifying session

def loginUser(username):
    current_user = db.session.query(UserData).filter_by(name=username).first()
    if current_user:
        session['username'] = current_user.name
        session['userid'] = current_user.id
        temp_session = getGeneratedSession(username)
        login_user[username] = temp_session
        print('user', username, 'login!')
    else:
        # raise error: undefined user
        print('undefined user')
        temp_session = None
    return temp_session


def userIsLogged(username):
    # Bug: user could be covered by other login users
    if 'username' in session:
        current_user = session.get('username')
        return True if current_user == username else False
    return False


@auth_bp.route('/logout')
def logout():
    username = session.pop('username', None)
    session.pop('userid', None)
    if username:
        print('{} logged out successfully!'.format(username))
    # return 'logout'
    return redirect(url_for('auth.login'))


'''
    decorators and methods below is used for preventing accesses without logged.
'''


@auth_bp.before_app_request
def loadLoggedInUser():
    user_id = session.get('userid')

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
