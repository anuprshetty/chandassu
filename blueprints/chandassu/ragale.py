from flask import Blueprint, render_template

ragale_bp = Blueprint(
    "ragale_bp",
    __name__,
    url_prefix="ragale",
    template_folder="../../templates/chandassu/ragale",
)


@ragale_bp.route("/")
def ragale():
    content = {"title": "Ragale"}
    return render_template("ragale.html", content=content)


@ragale_bp.route("/utsaha")
def utsaha():
    content = {
        "title": "Utsaha",
        "heading": "ಉತ್ಸಾಹ ರಗಳೆ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("utsaha.html", content=content)


@ragale_bp.route("/mandanila")
def mandanila():
    content = {
        "title": "Mandanila",
        "heading": "ಮಂದಾನಿಲ ರಗಳೆ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("mandanila.html", content=content)


@ragale_bp.route("/lalita")
def lalita():
    content = {
        "title": "Lalita",
        "heading": "ಲಲಿತ ರಗಳೆ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("lalita.html", content=content)
