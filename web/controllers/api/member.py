from web.controllers.api import route_api
from flask import request, jsonify
from application import app, db
import requests, json

@route_api.route("/member/login", methods=["GET", "POST"])
def login():
    resp = {'code':200,'msg': "操作成功", 'data':{}}
    req = request.values
    code = req['code'] if 'code' in req else ''
    if code is None or len(code) < 1:
        resp['code'] = -1
        resp['msg'] = "需要code"
        return jsonify(resp)

    url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code".format(app.config['MINA_APP']['appid'],app.config['MINA_APP']['appkey'],code)
    r = requests.get(url)
    res = json.loads(r.text)
    app.logger.info(res)
    return jsonify(resp)