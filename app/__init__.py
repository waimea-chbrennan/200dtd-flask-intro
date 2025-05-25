from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from random import randint
from sys import *

# Create the app
app = Flask(__name__)





# ======================
# Setup Routing


# Loading a static page - Home page
@app.get("/")
def home():
    return render_template('pages/home.jinja')

# Random Number Page - passing a value into template
@app.get("/random/")
@app.get("/random")
def random():
    set_int_max_str_digits(100000000)
    randNumber = randint(1,2**2**16)
    return render_template('pages/random.jinja', number=randNumber)

# Number page - extracting value from route of page and passing into template
@app.get("/number/<int:num>/")
@app.get("/number/<int:num>")
def analyseNumber(num):
    print(f"You entered: {num}")
    return render_template('pages/number.jinja',number=num)

# Loading a static page - About Page
@app.get("/about/")
@app.get("/about")
def about():
    return render_template('pages/about.jinja')

# Form page - static page with a form 
@app.get("/form/")
@app.get("/form")
def form():
    return render_template('pages/form.jinja')

# Handle data posted form the form
@app.post("/processForm")
def processForm():
    print(f"Form data ${request.form}")
    return render_template(
        'pages/formData.jinja', 
        name=request.form["name"], 
        age=request.form["age"]
    )


# Handle any missing pages
@app.errorhandler(404)
def notFound(error):
    return render_template('pages/404.jinja')