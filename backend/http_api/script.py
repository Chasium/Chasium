from glob import escape
from random import getrandbits
from urllib import response
from flask import (
    Blueprint, g, redirect, request, session, url_for, Request
)
from .config import login_user
from db import db
from db.models.cardScript import ScriptData

from generated.script.AddCardScriptRequest import AddCardScriptRequest

script_bp = Blueprint('script', __name__, url_prefix='/script')


@script_bp.route("/add", methods=['POST'])
def addCardScript():
    print('enter add Card Script')
    responseData = {}
    responseData['code'] = 1  # 出错状态
    requestData = AddCardScriptRequest(request)
    script = requestData.scriptContent
    print('got script: ', script)
    # TODO verification
    new_script = ScriptData(script)
    db.session.add(new_script)
    db.session.commit()
    print('New user created')
    responseData['code'] = 0
    # 需要return index吗？
    # index = new_script.getId()
    # print(index)
    return responseData
