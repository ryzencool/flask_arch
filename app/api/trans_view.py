from app.api import trans


@trans.route("/hello")
def hello():
    return "trans,hello"