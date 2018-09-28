from flask import Blueprint, render_template

vrutta_bp = Blueprint(
    "vrutta_bp",
    __name__,
    url_prefix="vrutta",
    template_folder="../../templates/chandassu/vrutta",
)


@vrutta_bp.route("/")
def vrutta():
    content = {
        "title": "Vrutta",
        "heading": "ಖ್ಯಾತಕರ್ಣಾಟಕ ವೃತ್ತಗಳು",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("vrutta.html", content=content)


@vrutta_bp.route("/utpala-mala")
def utpala_mala():
    content = {
        "title": "Utpala Mala",
        "heading": "ಉತ್ಪಲಮಾಲಾ ವೃತ್ತ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("utpala_mala.html", content=content)


@vrutta_bp.route("/champaka-mala")
def champaka_mala():
    content = {
        "title": "Champaka Mala",
        "heading": "ಚಂಪಕಮಾಲಾ ವೃತ್ತ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("champaka_mala.html", content=content)


@vrutta_bp.route("/shardula-vikreedita")
def shardula_vikreedita():
    content = {
        "title": "Shardula Vikreedita",
        "heading": "ಶಾರ್ದೂಲವಿಕ್ರೀಡಿತ ವೃತ್ತ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("shardula_vikreedita.html", content=content)


@vrutta_bp.route("/mattebha-vikreedita")
def mattebha_vikreedita():
    content = {
        "title": "Mattebha Vikreedita",
        "heading": "ಮತ್ತೇಭವಿಕ್ರೀಡಿತ ವೃತ್ತ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("mattebha_vikreedita.html", content=content)


@vrutta_bp.route("/sragdhara")
def sragdhara():
    content = {
        "title": "Sragdhara",
        "heading": "ಸ್ರಗ್ಧರಾ ವೃತ್ತ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("sragdhara.html", content=content)


@vrutta_bp.route("/maha-sragdhara")
def maha_sragdhara():
    content = {
        "title": "Maha Sragdhara",
        "heading": "ಮಹಾಸ್ರಗ್ಧರಾ ವೃತ್ತ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("maha_sragdhara.html", content=content)
