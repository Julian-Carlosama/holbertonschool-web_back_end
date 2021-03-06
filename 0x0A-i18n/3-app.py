#!/usr/bin/env python3
""" Create routes app """


from flask import Flask, render_template, request, jsonify
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Class config """
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"


@babel.localeselector
def get_locale():
    """ Function that determine
    the best match with our supported languages.
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """ get the route"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
