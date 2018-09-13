from app.api import user

@user.route("/hello")
def hello():
    return "hello"