recipes = {}


def add_recipe():

    name = input("Recipe Name: ")

    ingredients = []

    print("Enter ingredients. Type 'done' to finish.")

    while True:

        ingredient = input("Ingredient: ")

        if ingredient.lower() == "done":
            break

        ingredients.append(ingredient)

    instructions = input("Cooking Instructions: ")

    recipes[name] = {
        "Ingredients": ingredients,
        "Instructions": instructions
    }

    print("Recipe saved.")


def view_recipe():

    name = input("Recipe Name: ")

    if name not in recipes:
        raise Exception("Recipe not found.")

    recipe = recipes[name]

    print("\n========== RECIPE ==========")
    print("Name:", name)

    print("\nIngredients:")

    for ingredient in recipe["Ingredients"]:
        print("-", ingredient)

    print("\nInstructions:")
    print(recipe["Instructions"])


def view_all():

    for name in recipes:
        print("-", name)


while True:

    try:

        print("\n========== RECIPE MANAGER ==========")
        print("1. Add Recipe")
        print("2. View Recipe")
        print("3. View All Recipes")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            add_recipe()

        elif choice == 2:
            view_recipe()

        elif choice == 3:
            view_all()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")

    except Exception as e:
        print("Error:", e)