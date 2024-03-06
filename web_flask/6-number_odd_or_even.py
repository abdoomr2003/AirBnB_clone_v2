#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
flask_app = Flask(__name__)


@flask_app.route("/", strict_slashes=False)
def homePage():
    """Hello HBNB"""
    return "Hello HBNB!"


@flask_app.route("/hbnb", strict_slashes=False)
def homePage2():
    """HBNB"""
    return "HBNB"


@flask_app.route("/c/<text>", strict_slashes=False)
def Text(text):
    """c"""
    spaces_word = text.replace('_', ' ')
    return f"C {spaces_word}"


@flask_app.route("/python/", defaults={'text': 'is cool'},
                 strict_slashes=False)
@flask_app.route("/python/<text>", strict_slashes=False)
def Text2(text):
    """py"""
    spaces_word = text.replace('_', ' ')
    return f"Python {spaces_word}"


@flask_app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """num"""
    return f"{n} is a number"


@flask_app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """html"""
    return render_template('5-number.html', n=n)


@flask_app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd(n):
    """html"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=5000)
