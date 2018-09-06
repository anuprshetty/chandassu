from flask import Blueprint, render_template
from .shatpadi import shatpadi_bp
from .ragale import ragale_bp

chandassu_bp = Blueprint(
    "chandassu_bp",
    __name__,
    url_prefix="chandassu",
    template_folder="../../templates/chandassu",
)

chandassu_bp.register_blueprint(shatpadi_bp)
chandassu_bp.register_blueprint(ragale_bp)


@chandassu_bp.route("/")
def chandassu():
    content = {"title": "Chandassu"}
    return render_template("chandassu.html", content=content)


@chandassu_bp.route("/kandapadya")
def kandapadya():
    content = {"title": "Kandapadya"}
    return render_template("kandapadya.html", content=content)
