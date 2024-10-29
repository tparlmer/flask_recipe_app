-- schema.sql

CREATE TABLE IF NOT EXISTS Authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    additional TEXT,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES Authors(id)
);

CREATE TABLE IF NOT EXISTS Ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER,
    ingredient TEXT NOT NULL,
    quantity TEXT,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(id)
);

CREATE TABLE IF NOT EXISTS Instructions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER,
    step INTEGER NOT NULL,
    instructions TEXT,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(id)
);

CREATE TABLE IF NOT EXISTS Tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Recipe_Tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(id),
    FOREIGN KEY (tag_id) REFERENCES Tags(id)
);

CREATE INDEX idx_recipes_author ON Recipes(author_id);
CREATE INDEX idx_ingredients_recipe ON Ingredients(recipe_id);
CREATE INDEX idx_instructions_recipe ON Instructions(recipe_id);
CREATE INDEX idx_recipe_tags_recipe ON Recipe_Tags(recipe_id);
CREATE INDEX idx_recipe_tags_tag ON Recipe_Tags(tag_id);
