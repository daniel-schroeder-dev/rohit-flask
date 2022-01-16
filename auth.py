from flask import Blueprint, render_template, request

bp = Blueprint("auth", __name__)


@bp.route("/sign")
def sign():
    return render_template("sign.html")


@bp.route("/process", methods=["POST"])
def process():
    password = request.form["password"]
    if 1 == 1:
        return "You are now logged in"
    else:
        return "Login Failed"
