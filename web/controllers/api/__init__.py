from flask import Blueprint
route_api = Blueprint('api_page', __name__)
from web.controllers.api.Member import *


@route_api.route("/")
def api():
    return "MINA V1.0"