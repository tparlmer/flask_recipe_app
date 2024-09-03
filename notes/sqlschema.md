Below is the SQL schema and suggested filepath

-- backend/src/database/schema.sql

-- Authors Table
CREATE TABLE Authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Recipes Table
CREATE TABLE Recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    additional TEXT,
    author_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES Authors(id)
);

-- Ingredients Table
CREATE TABLE Ingredients (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER NOT NULL,
    ingredient VARCHAR(255) NOT NULL,
    quantity VARCHAR(50),
    FOREIGN KEY (recipe_id) REFERENCES Recipes(id)
);

-- Instructions Table
CREATE TABLE Instructions (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER NOT NULL,
    step INTEGER NOT NULL,
    instructions TEXT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(id)
);

-- Tags Table
CREATE TABLE Tags (
    id SERIAL PRIMARY KEY,
    tag VARCHAR(50) NOT NULL UNIQUE
);

-- Recipe_Tags Table
CREATE TABLE Recipe_Tags (
    recipe_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (recipe_id, tag_id),
    FOREIGN KEY (recipe_id) REFERENCES Recipes(id),
    FOREIGN KEY (tag_id) REFERENCES Tags(id)
);