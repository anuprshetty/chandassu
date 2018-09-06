from flask import Blueprint, render_template

gana_bp = Blueprint(
    "gana_bp", __name__, url_prefix="gana", template_folder="../templates/gana"
)


@gana_bp.route("/")
def gana():
    content = {"title": "Gana"}
    return render_template("gana.html", content=content)


@gana_bp.route("/matra-gana")
def matra_gana():
    content = {"title": "Matra Gana"}
    return render_template("matra_gana.html", content=content)


@gana_bp.route("/akshara-gana")
def akshara_gana():
    content = {"title": "Akshara Gana"}
    return render_template("akshara_gana.html", content=content)
