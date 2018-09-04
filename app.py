from flask import Flask
from blueprints.kandapadya import kandapadya_bp


app = Flask(__name__)
app.register_blueprint(kandapadya_bp)


if __name__ == "__main__":
    app.run(debug=True)
