import functools
from glob import escape
from flask import (
    Blueprint, flash, g, redirect, request, session, url_for
)
from db import db
from db.models.user import UserData
# from werkzeug.security import check_password_hash, generate_password_hash


# auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/user/<user>")
def user(user):
    return f'''
        <p>Hello, {escape(user)}!</p>
    '''


@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        submitAction = request.form.get('submit_button')
        if submitAction == 'login':

            global current_user_data
            # data = request.get_json(silent=True)
            # username = data['username']
            # password = data['password']

            username = request.form['username']
            password = request.form['password']
            print('User, ', username, password)

            error = None
            # verifications
            if not UsernameIsLegal(username):
                error = 'illegal username'
            elif not PasswordIsLegal(password):
                error = 'illegal password'

            elif not userIsExisted(username):
                error = 'wrong username or password'
            elif not passwordVerified(username, password):
                error = 'wrong username or password'
            elif userIsLogged(username):
                error = 'logged in already'

            if error is None:
                # verified, login user
                print('Verified')
                loginUser(username)
                current_user_data = {
                    'username': username, 'password': password}
                # return 'login successfully'

                return redirect(url_for('user'), user=username)
            else:
                print(error)
                # return error
        else:
            print('fk up')

    return '''
        <form method="post">
            <h2>Login</h2>
            <p>User Name: <input type=text name=username></p>
            <p>Password: <input type=password name=password></p>
            <p><input type=submit name=submit_button value=login></p>
        <form>
    '''


@auth_bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        submitAction = request.form.get('submit_button')
        if submitAction == 'register':

            # data = request.get_json(silent=True)
            # username = data['username']
            # password = data['password']

            username = request.form['username']
            password = request.form['password']
            print('User, ', username, password)
            error = None

            # verifications
            if not UsernameIsLegal(username):
                error = 'illegal username'
            elif not PasswordIsLegal(password):
                error = 'illegal password'

            elif userIsExisted(username):
                error = 'user existed'

            if error is None:
                # verified, register user
                print('New user created')
                addUser(username, password)
                loginUser(username)
                # return 'register successfully'

                return redirect(url_for('login'))
            else:
                print(error)
                # return error

    return '''
        <form method="post">
            <h2>Register</h2>
            <p>User Name: <input type=text name=username></p>
            <p>Password: <input type=password name=password></p>
            <p><input type=submit name=submit_button value=register></p>
        <form>
    '''


# Verifications

def userIsExisted(username):
    print('check user existence')
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
    return


# log in and out methods modifying session

def loginUser(username):
    current_user = db.session.query(UserData).filter_by(name=username).first()
    if current_user:
        session['username'] = current_user.name
        session['userid'] = current_user.id
    else:
        # raise error: undefined user
        pass
    return


def userIsLogged(username):
    # Bug: user could be covered by other login users
    if 'username' in session:
        current_user = session.get('username')
        return True if current_user == username else False
    return False


def logout():
    username = session.pop('username', None)
    session.pop('userid', None)
    if username:
        print('{} logged out successfully!'.format(username))
    return 'logout'


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
