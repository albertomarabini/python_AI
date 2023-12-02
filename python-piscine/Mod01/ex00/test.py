from book import Book
from recipe import Recipe

# Create some recipes
sandwich = Recipe("Sandwich", 1, 10, ["ham", "bread", "cheese", "tomatoes"], "A delicious sandwich", "lunch")
cake = Recipe("Cake", 3, 60, ["flour", "sugar", "eggs"], "Sweet and fluffy", "dessert")

# Create a book
my_cookbook = Book("My Cookbook")

# Add recipes to the book
my_cookbook.add_recipe(sandwich)
my_cookbook.add_recipe(cake)

# Print a specific recipe
my_cookbook.get_recipe_by_name("Cake")

# Print all lunch recipes
print("Lunch recipes:", my_cookbook.get_recipes_by_types("lunch"))
