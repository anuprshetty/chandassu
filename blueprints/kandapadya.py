from flask import Blueprint, render_template

kandapadya_bp = Blueprint(
    "kandapadya_bp", __name__, template_folder="../templates/kandapadya/"
)


@kandapadya_bp.route("/kandapadya")
def kandapadya():
    content = {
        "title": "Kandapadya",
    }
    return render_template("kandapadya.html", content=content)
