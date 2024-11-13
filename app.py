from flask import (
    Flask, render_template, redirect, request
)
from recipe_model import Recipe
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

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
    # Get form data - Remove trailing commas as they create tuples
    name = request.form["name"]
    additional = request.form.get("additional", "")  # Make additional optional
    ingredients = request.form.getlist("ingredients[]")  # Fix method name from getList to getlist
    quantities = request.form.getlist("quantities[]")  # Fix method name from getList to getlist
    instructions = request.form.getlist("instructions[]")  # Fix method name from getList to getlist
    tags = request.form.get("tags", "")  # Make tags optional

    # Combine ingredients with quantities if needed
    combined_ingredients = [{'ingredient': ing, 'quantity': qty} for ing, qty in zip(ingredients, quantities)]
    
    # Create a new Recipe object
    recipe = Recipe(
        name=name,
        additional=additional,
        ingredients=combined_ingredients,
        instructions=instructions,
        tags=tags
    )
    
    if recipe.save():
        return redirect("/recipes")
    else:
        return render_template("new.html", recipe=recipe), 400

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
    app.run(host='0.0.0.0', port=5000)
