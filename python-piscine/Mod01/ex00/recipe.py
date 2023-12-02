class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if not isinstance(name, str):
            raise ValueError("The name must be a string.")
        if not isinstance(cooking_lvl, int) or not 1 <= cooking_lvl <= 5:
            raise ValueError("The cooking level must be an integer between 1 and 5.")
        if not isinstance(cooking_time, int) or cooking_time < 0:
            raise ValueError("The cooking time must be a non-negative integer.")
        if not isinstance(ingredients, list) or not all(isinstance(item, str) for item in ingredients):
            raise ValueError("Ingredients must be a list of strings.")
        if not isinstance(description, str):
            raise ValueError("The description must be a string.")
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("The recipe type must be 'starter', 'lunch', or 'dessert'.")

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = (f"Name: {self.name}\n"
               f"Cooking Level: {self.cooking_lvl}\n"
               f"Cooking Time: {self.cooking_time} minutes\n"
               f"Ingredients: {', '.join(self.ingredients)}\n"
               f"Description: {self.description}\n"
               f"Type: {self.recipe_type}")
        return txt
