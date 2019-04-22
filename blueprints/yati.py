from flask import Blueprint, render_template

yati_bp = Blueprint(
    "yati_bp", __name__, url_prefix="yati", template_folder="../templates/"
)


@yati_bp.route("/")
def yati():
    content = {
        "title": "Yati",
        "heading": "ಯತಿ",
        "footer": {
            "previous": "home_bp.prasa_bp.prasa",
            "next": "home_bp.gana_bp.gana",
        },
    }
    return render_template("yati.html", content=content)
