
SQLALCHEMY_ECHO = False
SERVER_PORT = 8999
DEBUG = False
AUTH_COOKIE_NAME = "imooc_food"

##过滤url

IGNORE_URLS ={
    "^/user/login"
}
API_IGNORE_URLS ={
    "^/api"
}

IGNORE_CHECK_LOGIN_URLS = {
    "^/static",
    "^/favicon.ico"
}

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1": "正常",
    "0": "已删除"
}
MINA_APP = {
    "appid":"wxb66d497f45566d96",
    "appkey":"8229e89bece68f4d738ca8495150a0ac"
}
UPLOAD = {
    'ext':['jpg','gif','bmp','jpeg','png'],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}
APP = {
    'domain':'http://127.0.0.1:8999'
}
PAY_STATUS_DISPLAY_MAPPING = {
    "0":"订单关闭",
    "1":"支付成功",
    "-8":"待支付",
    "-7":"待发货",
    "-6":"待确认",
    "-5":"待评价"
}