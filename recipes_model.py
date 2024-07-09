# import json
# from operator import itemgetter
# import time
# from threading import Thread
# from random import random

# ========================
# Recipe Model
# ========================
PAGE_SIZE = 100

class Recipe:
    # mock recipe database

    def __init__(self, id=None, recipe_name=None, ingredients=None, instructions=None, image=None):
        self.id = id
        self.name = recipe_name
        self.ingredients = {}
        self.instructions = {}
        # self.image = image -> image will be added later
