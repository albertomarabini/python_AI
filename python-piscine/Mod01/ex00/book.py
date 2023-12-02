from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print(f"No recipe named {name} found.")
        return None

    def get_recipes_by_types(self, recipe_type):
        if recipe_type not in self.recipes_list:
            print(f"No recipes of type {recipe_type}.")
            return []
        return [recipe.name for recipe in self.recipes_list[recipe_type]]

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            raise ValueError("Invalid recipe. Must be a Recipe object.")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
        print(f"Recipe {recipe.name} added to the book.")
