#!/usr/bin/python3
"""script that _starts a Fla_sk -web application"""


# import Flask class from flask module
from flask import Flask

# create an instance called app of the class by passong the __name__ variable
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """display "Hello HBNB!"

    Returns:
        str: text on the in_dex page
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    """display "HBNB"

    Returns:
        str: text on the page
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """display "C", followed by the val_ue of the text variable

    Args:
        text (str): text to be served on the page

    Returns:
        str: text on the page
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    """display "Python", followed by the val-ue of the text variable

    Args:
        text (str): text to be served on the page

    Returns:
        str: text on the page
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_route(n):
    """display "n is a number" on_ly if n is an integer

    Args:
        n (integer): number to be displa-yed on page

    Returns:
        str: text on the page
    """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(debug=True)
