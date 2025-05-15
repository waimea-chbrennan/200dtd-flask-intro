from flask import Flask
from flask import render_template
from random import randint
from sys import *

# Create the app
app = Flask(__name__)

# Setup Routing

@app.get("/")
def home():
    return render_template('pages/home.jinja')

@app.get("/random")
def random():
    set_int_max_str_digits(100000000)
    randNumber = randint(1,2**2**16)
    return render_template('pages/random.jinja', number=randNumber)

@app.get("/about")
def about():
    return render_template('pages/about.jinja')


@app.errorhandler(404)
def notFound(error):
    return "404: page not found :("