from flask import Blueprint, render_template

vrutta_bp = Blueprint(
    "vrutta_bp",
    __name__,
    url_prefix="vrutta",
    template_folder="../templates/vrutta",
)


@vrutta_bp.route("/")
def vrutta():
    content = {"title": "Vrutta"}
    return render_template("vrutta.html", content=content)


@vrutta_bp.route("/utpala-mala")
def utpala_mala():
    content = {"title": "Utpala Mala"}
    return render_template("utpala_mala.html", content=content)


@vrutta_bp.route("/champaka-mala")
def champaka_mala():
    content = {"title": "Champaka Mala"}
    return render_template("champaka_mala.html", content=content)


@vrutta_bp.route("/shardula-vikreedita")
def shardula_vikreedita():
    content = {"title": "Shardula Vikreedita"}
    return render_template("shardula_vikreedita.html", content=content)


@vrutta_bp.route("/mattebha-vikreedita")
def mattebha_vikreedita():
    content = {"title": "Mattebha Vikreedita"}
    return render_template("mattebha_vikreedita.html", content=content)


@vrutta_bp.route("/sragdhara")
def sragdhara():
    content = {"title": "Sragdhara"}
    return render_template("sragdhara.html", content=content)


@vrutta_bp.route("/maha-sragdhara")
def maha_sragdhara():
    content = {"title": "Maha Sragdhara"}
    return render_template("maha_sragdhara.html", content=content)