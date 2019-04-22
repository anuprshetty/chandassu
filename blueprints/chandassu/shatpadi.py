from flask import Blueprint, render_template

shatpadi_bp = Blueprint(
    "shatpadi_bp",
    __name__,
    url_prefix="shatpadi",
    template_folder="../../templates/chandassu/shatpadi",
)


@shatpadi_bp.route("/")
def shatpadi():
    content = {
        "title": "Shatpadi",
        "heading": "ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.chandassu_bp.kandapadya",
            "next": "home_bp.chandassu_bp.shatpadi_bp.shara",
        },
    }
    return render_template("shatpadi.html", content=content)


@shatpadi_bp.route("/shara")
def shara():
    content = {
        "title": "Shara",
        "heading": "ಶರ ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.chandassu_bp.shatpadi_bp.shatpadi",
            "next": "home_bp.chandassu_bp.shatpadi_bp.kusuma",
        },
    }
    return render_template("shara.html", content=content)


@shatpadi_bp.route("/kusuma")
def kusuma():
    content = {
        "title": "Kusuma",
        "heading": "ಕುಸುಮ ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.chandassu_bp.shatpadi_bp.shara",
            "next": "home_bp.chandassu_bp.shatpadi_bp.bhoga",
        },
    }
    return render_template("kusuma.html", content=content)


@shatpadi_bp.route("/bhoga")
def bhoga():
    content = {
        "title": "Bhoga",
        "heading": "ಭೋಗ ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.chandassu_bp.shatpadi_bp.kusuma",
            "next": "home_bp.chandassu_bp.shatpadi_bp.bhamini",
        },
    }
    return render_template("bhoga.html", content=content)


@shatpadi_bp.route("/bhamini")
def bhamini():
    content = {
        "title": "Bhamini",
        "heading": "ಭಾಮಿನೀ ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.chandassu_bp.shatpadi_bp.bhoga",
            "next": "home_bp.chandassu_bp.shatpadi_bp.vardhaka",
        },
    }
    return render_template("bhamini.html", content=content)


@shatpadi_bp.route("/vardhaka")
def vardhaka():
    content = {
        "title": "Vardhaka",
        "heading": "ವಾರ್ಧಕ ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.chandassu_bp.shatpadi_bp.bhamini",
            "next": "home_bp.chandassu_bp.shatpadi_bp.parivardhini",
        },
    }
    return render_template("vardhaka.html", content=content)


@shatpadi_bp.route("/parivardhini")
def parivardhini():
    content = {
        "title": "Parivardhini",
        "heading": "ಪರಿವರ್ಧಿನೀ ಷಟ್ಪದಿ",
        "footer": {
            "previous": "home_bp.chandassu_bp.shatpadi_bp.vardhaka",
            "next": "home_bp.chandassu_bp.ragale_bp.ragale",
        },
    }
    return render_template("parivardhini.html", content=content)
