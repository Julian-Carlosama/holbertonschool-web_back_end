#!/usr/bin/env python3
""" Create routes app """


from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Class config """
    LANGUAGES = ["en", "fr"]


app.config.from_object("1-app.Config")
Babel.default_locale = "en"
Babel.default_timezone = "UTC"


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """ get the route"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
