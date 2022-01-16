from flask import Blueprint, render_template

bp = Blueprint("index", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/home", methods=["GET", "POST"])
def home():
    return render_template("homePage.html", myvar="hi")
