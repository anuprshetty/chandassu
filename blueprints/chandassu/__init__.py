from flask import Blueprint, render_template
from .shatpadi import shatpadi_bp
from .ragale import ragale_bp
from .vrutta import vrutta_bp

chandassu_bp = Blueprint(
    "chandassu_bp",
    __name__,
    url_prefix="chandassu",
    template_folder="../../templates/chandassu",
)

chandassu_bp.register_blueprint(shatpadi_bp)
chandassu_bp.register_blueprint(ragale_bp)
chandassu_bp.register_blueprint(vrutta_bp)


@chandassu_bp.route("/")
def chandassu():
    content = {
        "title": "Chandassu",
        "heading": "ಛಂದಸ್ಸು",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.prasa_bp.prasa",
        },
    }
    return render_template("chandassu.html", content=content)


@chandassu_bp.route("/kandapadya")
def kandapadya():
    content = {
        "title": "Kandapadya",
        "heading": "ಕಂದ ಪದ್ಯ",
        "footer": {
            "previous": "home_bp.gana_bp.matra_gana",
            "next": "home_bp.chandassu_bp.shatpadi_bp.shatpadi",
        },
    }
    return render_template("kandapadya.html", content=content)
