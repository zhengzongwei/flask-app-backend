from flask import Blueprint
from app.api.v1.admin import admin
v1 = Blueprint('v1',__name__,url_prefix='/v1')

v1.register_blueprint(admin)