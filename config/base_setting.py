
SQLALCHEMY_ECHO = False
SERVER_PORT = 8999
DEBUG = False
AUTH_COOKIE_NAME = "imooc_food"

##过滤url

IGNORE_URLS ={
    "^/user/login",
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