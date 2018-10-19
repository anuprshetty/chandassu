from flask import Blueprint, render_template, request

test_bp = Blueprint(
    "test_bp", __name__, url_prefix="test", template_folder="../templates/test"
)


@test_bp.route("/")
def test():
    content = {
        "title": "Test",
        "heading": "ಪರೀಕ್ಷಿಸಿ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }
    return render_template("test.html", content=content)


@test_bp.route("/result", methods=["POST"])
def result():
    content = {
        "title": "Result",
        "heading": "ನಿಮ್ಮ ಪದ್ಯದ ಛಂದಸ್ಸಿನ ಮಾಹಿತಿ",
        "footer": {
            "previous": "home_bp.home",
            "next": "home_bp.home",
        },
    }

    poem = request.form.get("poem")
    print(f"poem: {poem}")
    return render_template("result.html", content=content)
