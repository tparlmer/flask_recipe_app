from flask import (
    Flask, redirect, render_template, request
)
from recipes_model import Recipe

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/recipes")

@app.route("/recipes")
def recipes():
    search = request.args.get("q")
    if search is not None:
        recipes_set = Recipe.search(search)
    else:
        recipes_set = Recipe.all()
    return render_template('index.html', recipes=recipes_set)