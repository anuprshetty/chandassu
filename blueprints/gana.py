from flask import Blueprint, render_template

gana_bp = Blueprint(
    "gana_bp", __name__, url_prefix="gana", template_folder="../templates/gana"
)


@gana_bp.route("/")
def gana():
    content = {
        "title": "Gana",
        "heading": "ಗಣಗಳು",
        "footer": {
            "previous": "home_bp.yati_bp.yati",
            "next": "home_bp.gana_bp.matra_gana",
        },
    }
    return render_template("gana.html", content=content)


@gana_bp.route("/matra-gana")
def matra_gana():
    content = {
        "title": "Matra Gana",
        "heading": "ಮಾತ್ರಾ ಗಣ",
        "footer": {
            "previous": "home_bp.gana_bp.gana",
            "next": "home_bp.chandassu_bp.kandapadya",
        },
    }
    return render_template("matra_gana.html", content=content)


@gana_bp.route("/akshara-gana")
def akshara_gana():
    content = {
        "title": "Akshara Gana",
        "heading": "ಅಕ್ಷರ ಗಣ",
        "footer": {
            "previous": "home_bp.chandassu_bp.ragale_bp.lalita",
            "next": "home_bp.chandassu_bp.vrutta_bp.vrutta",
        },
    }
    return render_template("akshara_gana.html", content=content)


@gana_bp.route("/amsha-gana")
def amsha_gana():
    content = {
        "title": "Amsha Gana",
        "heading": "ಅಂಶ ಗಣ",
        "footer": {
            "previous": "home_bp.chandassu_bp.vrutta_bp.maha_sragdhara",
            "next": "home_bp.test_bp.test",
        },
    }
    return render_template("amsha_gana.html", content=content)
