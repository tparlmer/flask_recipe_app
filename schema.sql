-- schema.sql

-- Drop tables if they exist
DROP TABLE IF EXISTS Recipe_Tags CASCADE;
DROP TABLE IF EXISTS Tags CASCADE;
DROP TABLE IF EXISTS Instructions CASCADE;
DROP TABLE IF EXISTS Ingredients CASCADE;
DROP TABLE IF EXISTS Recipes CASCADE;
DROP TABLE IF EXISTS Authors CASCADE;

-- Create tables
CREATE TABLE Authors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE Recipes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    additional TEXT,
    author_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES Authors(id) ON DELETE CASCADE
);

CREATE TABLE Ingredients (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER NOT NULL,
    ingredient TEXT NOT NULL,
    quantity TEXT,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(id) ON DELETE CASCADE
);

CREATE TABLE Instructions (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER NOT NULL,
    step INTEGER NOT NULL,
    instructions TEXT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(id) ON DELETE CASCADE
);

CREATE TABLE Tags (
    id SERIAL PRIMARY KEY,
    tag TEXT NOT NULL UNIQUE
);

CREATE TABLE Recipe_Tags (
    recipe_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (recipe_id, tag_id),
    FOREIGN KEY (recipe_id) REFERENCES Recipes(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES Tags(id) ON DELETE CASCADE
);

-- Create indexes
CREATE INDEX idx_recipes_author ON Recipes(author_id);
CREATE INDEX idx_ingredients_recipe ON Ingredients(recipe_id);
CREATE INDEX idx_instructions_recipe ON Instructions(recipe_id);
CREATE INDEX idx_recipe_tags_recipe ON Recipe_Tags(recipe_id);
CREATE INDEX idx_recipe_tags_tag ON Recipe_Tags(tag_id);

-- Insert some initial data
INSERT INTO Authors (name) VALUES ('System');
