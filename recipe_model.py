import sqlite3

# =============================================================================
# Recipe Model
# =============================================================================

class Recipe:
    def __init__(self, id=None, name='', additional='', ingredients=None, instructions=None, tags='', errors=None):
        self.id = id
        self.name = name
        self.additional = additional
        self.ingredients = ingredients if ingredients is not None else []
        self.instructions = instructions if instructions is not None else []
        self.tags = tags
        self.errors = errors

    def __repr__(self):
        return f"<Recipe {self.id}>"

    def validate(self):
        # Initialize errors as a dictionary to match template usage
        self.errors = {}
        
        # Validate name
        if not self.name or self.name.strip() == '':
            self.errors['name'] = "Name cannot be blank"
            
        # Validate ingredients
        if not self.ingredients or len(self.ingredients) == 0:
            self.errors['ingredients'] = "Ingredients cannot be blank"
            
        # Validate instructions  
        if not self.instructions or len(self.instructions) == 0:
            self.errors['instructions'] = "Instructions cannot be blank"
            
        return len(self.errors) == 0

    def save(self):
        if not self.validate():
            print(f"Recipe not saved: {self.errors}")
            return False

        conn = self.get_db_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        try:
            # Start transaction
            cursor.execute('BEGIN')

            # Save or update recipe
            if self.id is None:
                # Insert new recipe
                cursor.execute('''
                    INSERT INTO Recipes (name, additional)
                    VALUES (?, ?)
                ''', (self.name, self.additional))
                self.id = cursor.lastrowid
            else:
                # Update existing recipe
                cursor.execute('''
                    UPDATE Recipes 
                    SET name = ?, additional = ?
                    WHERE id = ?
                ''', (self.name, self.additional, self.id))

            # Delete existing ingredients and instructions (for updates)
            cursor.execute('DELETE FROM Ingredients WHERE recipe_id = ?', (self.id,))
            cursor.execute('DELETE FROM Instructions WHERE recipe_id = ?', (self.id,))

            # Save ingredients
            for ingredient in self.ingredients:
                cursor.execute('''
                    INSERT INTO Ingredients (recipe_id, ingredient, quantity)
                    VALUES (?, ?, ?)
                ''', (self.id, ingredient['ingredient'], ingredient['quantity']))

            # Save instructions
            for i, instruction in enumerate(self.instructions):
                cursor.execute('''
                    INSERT INTO Instructions (recipe_id, step, instructions)
                    VALUES (?, ?, ?)
                ''', (self.id, i + 1, instruction))

            # Commit transaction
            conn.commit()
            return True

        except Exception as e:
            conn.rollback()
            print(f"Error saving recipe: {e}")
            return False
        finally:
            conn.close()

    @classmethod
    def find(cls, recipe_id):
        conn = cls.get_db_connection()
        if conn is None:
            return None

        cursor = conn.cursor()
        try:
            # Get recipe details
            cursor.execute('''
                SELECT r.id, r.name, r.additional 
                FROM Recipes r
                WHERE r.id = ?
            ''', (recipe_id,))
            recipe_data = cursor.fetchone()
            
            if recipe_data is None:
                return None
                
            # Get ingredients
            cursor.execute('''
                SELECT ingredient, quantity 
                FROM Ingredients
                WHERE recipe_id = ?
            ''', (recipe_id,))
            ingredients = cursor.fetchall()
            
            # Get instructions
            cursor.execute('''
                SELECT instructions
                FROM Instructions 
                WHERE recipe_id = ?
                ORDER BY step
            ''', (recipe_id,))
            instructions = [row[0] for row in cursor.fetchall()]
            
            # Create and return Recipe object
            return cls(
                id=recipe_data[0],
                name=recipe_data[1], 
                additional=recipe_data[2],
                ingredients=ingredients,
                instructions=instructions
            )
            
        except Exception as e:
            print(f"Error finding recipe: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def all(cls):
        conn = Recipe.get_db_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        try:
            # Get all recipes
            cursor.execute('SELECT id, name, additional FROM Recipes')
            recipes = []
            for row in cursor.fetchall():
                recipe_id = row[0]
                
                # Get ingredients for this recipe
                cursor.execute('SELECT ingredient, quantity FROM Ingredients WHERE recipe_id = ?', (recipe_id,))
                ingredients = cursor.fetchall()
                
                # Get instructions for this recipe
                cursor.execute('SELECT instructions FROM Instructions WHERE recipe_id = ? ORDER BY step', (recipe_id,))
                instructions = [row[0] for row in cursor.fetchall()]
                
                # Create Recipe object
                recipe = cls(
                    id=row[0],
                    name=row[1],
                    additional=row[2],
                    ingredients=ingredients,
                    instructions=instructions
                )
                recipes.append(recipe)
                
            return recipes
        except Exception as e:
            print(f"Error executing query: {e}")
            return []
        finally:
            conn.close()
  
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

    @staticmethod
    def save_db():
        conn = Recipe.get_db_connection()
        if conn is None:
            raise Exception("Database connection failed")

        cursor = conn.cursor()
        try:
            # Example of using UPSERT for efficiency
            for recipe in Recipe.db.values():
                cursor.execute('''
                    INSERT INTO Recipes (id, name, additional)
                    VALUES (?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        name = excluded.name,
                        additional = excluded.additional
                ''', (recipe.id, recipe.name, recipe.additional))

                # Assuming you have methods to save ingredients, instructions, etc.
                recipe.save_ingredients(cursor)
                recipe.save_instructions(cursor)
                recipe.save_tags(cursor)

            conn.commit()
        except Exception as e:
            conn.rollback()  # Rollback the transaction on error
            print(f"Error executing query: {e}")
            raise e
        finally:
            conn.close()

    def delete(self):
        """Delete this recipe from the database"""
        try:
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM recipes WHERE id = ?", (self.id,))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error deleting recipe: {e}")
            return False
