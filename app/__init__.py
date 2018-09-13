from flask import Flask
from app.api import user, trans
app_starter = Flask(__name__)

app_starter.register_blueprint(user, url_prefix="/user")
app_starter.register_blueprint(trans, url_prefix="/trans")