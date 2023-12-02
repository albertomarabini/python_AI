cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_recipe_names(cookbook):
    print("Available recipes:")
    for recipe in cookbook:
        print(f"- {recipe}")

def print_recipe_details(cookbook, recipe_name):
    if recipe_name in cookbook:
        recipe = cookbook[recipe_name]
        print(f"Recipe for {recipe_name}:")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Meal type: {recipe['meal']}")
        print(f"Preparation time: {recipe['prep_time']} minutes")
    else:
        print(f"Recipe '{recipe_name}' not found.")

def delete_recipe(cookbook, recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print(f"Recipe '{recipe_name}' has been deleted.")
    else:
        print(f"Recipe '{recipe_name}' not found.")

def add_recipe(cookbook):
    name = input("Enter a name:\n")
    ingredients = input("Enter ingredients (separated by space):\n").split()
    meal_type = input("Enter a meal type:\n")
    prep_time = int(input("Enter a preparation time (in minutes):\n"))
    
    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal_type,
        "prep_time": prep_time
    }
    print(f"Recipe '{name}' has been added to the cookbook.")


while True:
    print("\nWelcome to the Python Cookbook!")
    print("List of available options:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    choice = input("Please select an option:\n>> ")

    if choice == '1':
        add_recipe(cookbook)
    elif choice == '2':
        recipe_name = input("Please enter a recipe name to delete:\n>> ")
        delete_recipe(cookbook, recipe_name)
    elif choice == '3':
        recipe_name = input("Please enter a recipe name to get its details:\n>> ")
        print_recipe_details(cookbook, recipe_name)
    elif choice == '4':
        print_recipe_names(cookbook)
    elif choice == '5':
        print("Cookbook closed. Goodbye!")
        break
    else:
        print("Sorry, this option does not exist. Please try again.")

# Define the functions print_recipe_names, print_recipe_details,
# delete_recipe, and add_recipe here

if __name__ == "__main__":
    main()