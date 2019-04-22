from flask import Blueprint, render_template

prasa_bp = Blueprint(
    "prasa_bp", __name__, url_prefix="prasa", template_folder="../templates/"
)


@prasa_bp.route("/")
def prasa():
    content = {
        "title": "Prasa",
        "heading": "ಪ್ರಾಸ",
        "footer": {
            "previous": "home_bp.chandassu_bp.chandassu",
            "next": "home_bp.yati_bp.yati",
        },
    }
    return render_template("prasa.html", content=content)
