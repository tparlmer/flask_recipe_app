import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insert authors
cur.executescript("""
    BEGIN;
    INSERT INTO Authors (name) VALUES ('Thomas Parlmer');
    COMMIT;
""")

# Insert recipes
cur.executescript("""
    BEGIN;
    INSERT INTO Recipes (name, additional, author_id) VALUES 
    ('Wings', 'Use an air fryer', 1),
    ('Salad', 'Feeds 3-4 ppl', 1),
    ('Green Smoothie', 'Mix and match ingredients as you see fit', 1);
    COMMIT;
""")

# Insert ingredients
cur.executescript("""
    BEGIN;
    INSERT INTO Ingredients (recipe_id, ingredient, quantity) VALUES 
    (1, 'Uncut chicken wings', '1lbs'),
    (1, 'Nandos', '100g'),
    (1, 'Tomato sauce', '1 cup'),
    (2, 'Cucumber', '1 full cucumber'),
    (2, 'Red onion', '1/4 red onion'),
    (2, 'Cherry tomatoes', 'to taste'),
    (2, 'Red Wine Vinegar', 'to taste'),
    (2, 'Green pepper', '1/2 pepper'),
    (2, 'Salt', 'to taste'),
    (2, 'Pepper', 'to taste'),
    (3, 'Frozen Kale', 'to taste'),
    (3, 'Banana', '1 whole banana'),
    (3, 'frozen mango', 'to taste'),
    (3, 'greek yogurt', 'to taste'),
    (3, 'ginger', 'to taste');
    COMMIT;
""")

# Insert instructions
cur.executescript("""
    BEGIN;
    INSERT INTO Instructions (recipe_id, step, instructions) VALUES 
    (1, 1, 'Chop wings'),
    (1, 2, 'Marinate with Nandos sauce'),
    (1, 3, 'Put wings in air fryer for 20 minutes at 380 degrees F'),
    (1, 4, 'At 10 minutes, flip all wings in air fryer'),
    (1, 5, 'When wings have finished cooking, baste wings with Nandos sauce and put back in air fryer for 2 minutes'),
    (1, 6, 'Enjoy'),
    (2, 1, 'Dice all vegetables - put them in salad bowl'),
    (2, 2, 'add salt, pepper, and red wine vinegar'),
    (2, 3, 'toss and serve'),
    (3, 1, 'Blend kale with water first'),
    (3, 2, 'Add all other ingredients and blend'),
    (3, 3, 'drink and enjoy');
    COMMIT;
""")

# Insert tags
cur.executescript("""
    BEGIN;
    INSERT INTO Tags (tag) VALUES 
    ('Fingerfood'),
    ('Dinner'),
    ('Salad'),
    ('Supplement');
    COMMIT;
""")

# Insert recipe_tags
cur.executescript("""
    BEGIN;
    INSERT INTO Recipe_Tags (recipe_id, tag_id) VALUES 
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 2),
    (3, 4);
    COMMIT;
""")

connection.commit()
connection.close()