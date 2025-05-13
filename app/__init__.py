from flask import Flask
from flask import render_template
from random import randint

# Create the app
app = Flask(__name__)

# Setup Routing

@app.get("/")
def home():
    return render_template('pages/home.jinja')

@app.get("/random")
def random():
    return str(randint(1,2**1024))

@app.get("/about")
def about():
    return render_template('pages/about.jinja')