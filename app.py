from flask import (
    Flask, render_template, redirect, request
)
from recipe_model import Recipe

app = Flask(__name__)

# =============================================================================
# ROUTES
# =============================================================================

# HOME
@app.route('/')
def index():
    return redirect("/recipes")

# GETS ALL RECIPES
@app.route("/recipes")
def recipes():
    search = request.args.get("q")
    if search is not None:
        # search method is defined in Recipe class
        recipes_set = Recipe.search(search)
    else:
        # TODO - define all() method in Recipe class
        recipes_set = Recipe.all()
    return render_template("index.html", recipes=recipes_set)

# GETS NEW RECIPE FORM
@app.route("/recipes/new", methods=["GET"])
def recipes_new_get():
    return render_template("new.html", recipe=Recipe()) # Recipe() constructs a new Recipe object

# POSTS NEW RECIPE DATA TO DATABASE
@app.route("/recipes/new", methods=["POST"])
def recipes_new():
    recipe = Recipe(
        #TODO - need to generate new ID
        name=request.form["name"],
        additional=request.form["additional"],
        ingredients=request.form["ingredients"],
        instructions=request.form["instructions"],
        tags=request.form["tags"]
    )
    if recipe.save():
        return redirect("/recipes")
    else:
        return render_template("new.html", recipe=recipe)

# GETS RECIPE BY ID
@app.route("/recipes/<recipe_id>")
def recipes_view(recipe_id=0):
    recipe = Recipe.find(recipe_id)
    return render_template("show.html", recipe=recipe)

# GET EDIT RECIPE
@app.route("/recipes/<recipe_id>/edit", methods=["GET"])
def recipes_edit_get(recipe_id=0):
    recipe = Recipe.find(recipe_id)
    return render_template("edit.html", recipe=recipe)

# POST EDIT RECIPE
@app.route("/recipes/<recipe_id>/edit", methods=["POST"])
def recipes_edit_post(recipe_id=0):
    r = Recipe.find(recipe_id)
    #TODO - Fix below code
    r.update(
        name=request.form["name"],
        additional=request.form["additional"],
        ingredients=request.form["ingredients"],
        instructions=request.form["instructions"],
        tags=request.form["tags"]
    )
    if r.save():
        return redirect(f"/recipes/{recipe_id}")
    else:
        return render_template("edit.html", recipe=r)
    
# DELETE RECIPE
@app.route("/recipes/<recipe_id>/delete", methods=["POST"])
def recipes_delete(recipe_id=0):
    r = Recipe.find(recipe_id)
    r.delete()
    return redirect("/recipes")


if __name__ == '__main__':
    app.run(debug=True)