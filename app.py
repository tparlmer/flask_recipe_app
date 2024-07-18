from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    try:
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        print("Database connection successful")
        return conn
    except Exception as e:
        print(f"Databse connection failed: {e}")
        return None

# Currently going to show all data in the database as a test
@app.route('/')
def index():
    print("Index route hit")
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    
    cursor = conn.cursor()
    try:
        print("Executing SQL Query")
        cursor.execute('SELECT * FROM Recipes')
        recipes = cursor.fetchall()
        print(f"Query executed, fetched {len(recipes)} recipes")
        
        # Print each recipe
        for recipe in recipes:
            print(f"Recipe: {dict(recipe)}")

        print(f"Passing to template: {recipes}")

    except Exception as e:
        print(f"Error executing query: {e}")
        return "Database query failed", 500
    finally:
        conn.close()
    
    return render_template('index.html', recipes=recipes)

# Show Recipe route
# @app.route('/recipe/<int:recipe_id>')
# def show_recipe(recipe_id):

# New Recipe route

# Edit Recipe route

# Delete Recipe route

if __name__ == '__main__':
    app.run(debug=True)