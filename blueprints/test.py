from flask import Blueprint, render_template, request

from console.src.features.chandassu_type import ChandassuType

test_bp = Blueprint(
    "test_bp", __name__, url_prefix="test", template_folder="../templates/test"
)


@test_bp.route("/")
def test():
    content = {
        "title": "Test",
        "heading": "ಪರೀಕ್ಷಿಸಿ",
        "footer": {
            "previous": "home_bp.gana_bp.amsha_gana",
            "next": "home_bp.practice_bp.practice",
        },
    }
    return render_template("test.html", content=content)


@test_bp.route("/result", methods=["POST"])
def result():
    test_poem = request.form.get("poem")

    chandassu_type = ChandassuType.get_chandassu_type(test_poem)

    content = {
        "title": "Result",
        "heading": "ನಿಮ್ಮ ಪದ್ಯದ ಛಂದಸ್ಸಿನ ಮಾಹಿತಿ",
        "chandassu_type": {
            "invalid": chandassu_type.invalid(),
            "name": chandassu_type.name(),
            "poem_chandassu": chandassu_type.poem_chandassu(),
        },
        "footer": {
            "previous": "home_bp.test_bp.test",
            "next": "",
        },
    }

    return render_template("test_result.html", content=content)
