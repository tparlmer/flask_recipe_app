import os

class Config:
    DB_NAME = os.environ.get('DB_NAME', 'recipe_database')
    DB_USER = os.environ.get('DB_USER', 'your_user')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'your_password')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '5432')
