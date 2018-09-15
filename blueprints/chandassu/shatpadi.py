from flask import Blueprint, render_template

shatpadi_bp = Blueprint(
    "shatpadi_bp",
    __name__,
    url_prefix="shatpadi",
    template_folder="../../templates/chandassu/shatpadi",
)


@shatpadi_bp.route("/")
def shatpadi():
    content = {"title": "Shatpadi"}
    return render_template("shatpadi.html", content=content)


@shatpadi_bp.route("/shara")
def shara():
    content = {
        "title": "Shara",
        "heading": "ಶರ ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("shara.html", content=content)


@shatpadi_bp.route("/kusuma")
def kusuma():
    content = {
        "title": "Kusuma",
        "heading": "ಕುಸುಮ ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("kusuma.html", content=content)


@shatpadi_bp.route("/bhoga")
def bhoga():
    content = {
        "title": "Bhoga",
        "heading": "ಭೋಗ ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("bhoga.html", content=content)


@shatpadi_bp.route("/bhamini")
def bhamini():
    content = {
        "title": "Bhamini",
        "heading": "ಭಾಮಿನೀ ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("bhamini.html", content=content)


@shatpadi_bp.route("/vardhaka")
def vardhaka():
    content = {
        "title": "Vardhaka",
        "heading": "ವಾರ್ಧಕ ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("vardhaka.html", content=content)


@shatpadi_bp.route("/parivardhini")
def parivardhini():
    content = {
        "title": "Parivardhini",
        "heading": "ಪರಿವರ್ಧಿನೀ ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("parivardhini.html", content=content)
