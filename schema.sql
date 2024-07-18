-- schema.sql

CREATE TABLE IF NOT EXISTS Authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    additional TEXT,
    author_id INTEGER,
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
    tag TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Recipe_Tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(id),
    FOREIGN KEY (tag_id) REFERENCES Tags(id)
);