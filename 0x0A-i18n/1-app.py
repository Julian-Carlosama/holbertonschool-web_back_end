#!/usr/bin/env python3
""" Create routes app """


from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Class config """
    LANGUAGES = ["en", "fr"]
    Babel.default_locate = "en"
    Babel.default_timezone = "UTC"


app.config.from_object(Config)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """ get the route"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
