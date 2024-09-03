import sqlite3

# =============================================================================
# Recipe Model
# =============================================================================

class Recipe:
    def __init__(self, id, name, additional, ingredients, instructions, tags, errors):
        self.id = id
        self.name = name
        self.additional = additional
        self.ingredients = ingredients
        self.instructions = instructions
        self.tags = tags
        self.errors = errors

    def __repr__(self):
        return f"<Recipe {self.id}>"

    @classmethod
    def all(cls):
        conn = Recipe.get_db_connection()
        if conn is None:
            return "Database connection failed", 500

        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM Recipes')
            recipes = cursor.fetchall()
            return recipes
        except Exception as e:
            print(f"Error executing query: {e}")
            return "Database query failed", 500
        finally:
            conn.close()

    #TODO - add save() method

    #TODO - add find() method

    # @classmethod
    # def search(cls, search_term):
    #     conn = Recipe.get_db_connection()
    #     if conn is None:
    #         return "Database connection failed", 500

    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute('SELECT * FROM Recipes WHERE name LIKE ?', (f"%{search_term}%",))
    #         recipes = cursor.fetchall()
    #         return recipes
    #     except Exception as e:
    #         print(f"Error executing query: {e}")
    #         return "Database query failed", 500
    #     finally:
    #         conn.close()

    @classmethod
    def search(cls, search_term):
        conn = cls.get_db_connection()
        if conn is None:
            return "Database connection failed", 500

        cursor = conn.cursor()
        try:
            cursor.execute('''
                SELECT r.id, r.name, r.additional, a.name 
                FROM Recipes r
                JOIN Authors a ON r.author_id = a.id
                WHERE r.name LIKE ?
            ''', (f"%{search_term}%",))
            recipe_data = cursor.fetchall()

            recipes = []
            for row in recipe_data:
                recipe_id = row[0]
                cursor.execute('''
                    SELECT ingredient, quantity FROM Ingredients
                    WHERE recipe_id = ?
                ''', (recipe_id,))
                ingredients = cursor.fetchall()

                cursor.execute('''
                    SELECT step, instructions FROM Instructions
                    WHERE recipe_id = ?
                    ORDER BY step
                ''', (recipe_id,))
                instructions = cursor.fetchall()

                cursor.execute('''
                    SELECT t.tag FROM Tags t
                    JOIN Recipe_Tags rt ON t.id = rt.tag_id
                    WHERE rt.recipe_id = ?
                ''', (recipe_id,))
                tags = cursor.fetchall()

                recipe = Recipe(
                    id=row[0],
                    name=row[1],
                    additional=row[2],
                    author=row[3],
                    ingredients=[{'ingredient': ing[0], 'quantity': ing[1]} for ing in ingredients],
                    instructions=[{'step': instr[0], 'instructions': instr[1]} for instr in instructions],
                    tags=[tag[0] for tag in tags]
                )

                print(f"Recipe: {recipe.__dict__}")  # Print the recipe object

                recipes.append(recipe)

            return recipes
        except Exception as e:
            print(f"Error executing query: {e}")
            return "Database query failed", 500
        finally:
            conn.close()

    @staticmethod
    def get_db_connection():
        try:
            conn = sqlite3.connect('database.db')
            conn.row_factory = sqlite3.Row
            print("Database connection successful")
            return conn
        except Exception as e:
            print(f"Databse connection failed: {e}")
            return None

    @staticmethod
    def get_recipe(recipe_id):
        conn = Recipe.get_db_connection()
        if conn is None:
            return "Database connection failed", 500

        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM Recipes WHERE id = ?', (recipe_id,))
            recipes = cursor.fetchall()
            return recipes
        except Exception as e:
            print(f"Error executing query: {e}")
            return "Database query failed", 500
        finally:
            conn.close()
