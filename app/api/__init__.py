from flask import Flask, Blueprint

user = Blueprint("user", __name__)
trans = Blueprint("trans", __name__)

from app.api import user_view
from app.api import trans_view