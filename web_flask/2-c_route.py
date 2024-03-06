#!/usr/bin/python3
"""script that starts a Flask w_eb application"""


# import F_lask class from _flask module
from flask import Flask

# create an instance called app of the class by passong the __name__ variable
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """display "Hello HBNB!"

    Returns:
        str: text on the index page
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    """display "HBNB

    Returns:
        str: text on the page
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """_display "C", followed by the _value of the _text variable

    Args:
        text (str): text to be _served on the page

    Returns:
        str: text on the page
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
