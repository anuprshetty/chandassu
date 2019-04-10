from flask import Blueprint, render_template, request

from console.src.utils.random_poem import get_random_poem
from console.src.utils.constant import Constant
from console.src.features.chandassu_type import ChandassuType

practice_bp = Blueprint(
    "practice_bp",
    __name__,
    url_prefix="practice",
    template_folder="../templates/practice",
)


def get_practice_poem(original_poem):
    practice_poem = "\n" + original_poem.replace("\n", "\n\n")

    return practice_poem


def get_practice_poem_lines_count(practice_poem):
    practice_poem_lines_count = len(practice_poem.split("\n"))

    return practice_poem_lines_count


@practice_bp.route("/")
def practice():
    original_poem = get_random_poem()
    practice_poem = get_practice_poem(original_poem)
    practice_poem_lines_count = get_practice_poem_lines_count(practice_poem)

    content = {
        "title": "Practice",
        "heading": "ಅಭ್ಯಾಸ",
        "poems": {"original_poem": original_poem, "practice_poem": practice_poem},
        "practice_poem_lines_count": practice_poem_lines_count,
        "chandassu_kannada_names": Constant.chandassu_kannada_names,
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("practice.html", content=content)


@practice_bp.route("/result", methods=["POST"])
def result():
    original_poem = request.form.get("original_poem")
    practice_poem_chandassu = request.form.get("practice_poem")
    selected_chandassu_name = request.form.get("selected_chandassu_name")

    original_poem_chandassu_type = ChandassuType.get_chandassu_type(original_poem)

    content = {
        "title": "Result",
        "heading": "ಅಭ್ಯಾಸ ಪದ್ಯದ ಛಂದಸ್ಸಿನ ಮಾಹಿತಿ",
        "original_poem_info": {
            "invalid": original_poem_chandassu_type.invalid(),
            "name": original_poem_chandassu_type.name(),
            "poem_chandassu": original_poem_chandassu_type.poem_chandassu(),
        },
        "practice_poem_info": {
            "name": selected_chandassu_name,
            "poem_chandassu": practice_poem_chandassu,
        },
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }

    return render_template("practice_result.html", content=content)
