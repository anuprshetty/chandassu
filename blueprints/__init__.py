from flask import Blueprint, render_template
from .prasa import prasa_bp
from .yati import yati_bp
from .gana import gana_bp
from .chandassu import chandassu_bp
from .test import test_bp
from .practice import practice_bp

home_bp = Blueprint("home_bp", __name__, url_prefix="", template_folder="../templates/")

home_bp.register_blueprint(prasa_bp)
home_bp.register_blueprint(yati_bp)
home_bp.register_blueprint(gana_bp)
home_bp.register_blueprint(chandassu_bp)
home_bp.register_blueprint(test_bp)
home_bp.register_blueprint(practice_bp)


@home_bp.route("/")
def home():
    content = {"title": "Home"}
    return render_template("home.html", content=content)


@home_bp.route("/about")
def about():
    content = {"title": "About"}
    return render_template("about.html", content=content)
