import json

try:
    import RecipeClass
except ModuleNotFoundError:
    print("Module to import not found")

recipes = {}


def updateRecipe(recipe_name):
    print("Please select what you would like to update:")
    print("1. Name\n 2. Ingredients\n 3. Instructions\n 4. Category\n 5. Calories\n "
          "6. Carbs\n 7. Protein\n 8. Go back to Main Menu")

    while True:
        userInput = input("What would you like to update? ")

        if userInput == '1':
            # Updating name
            new_name = get_valid_input("Enter the new name of the recipe: ", lambda x: len(x) > 0 and not x.isdigit())
            if new_name != recipe_name:
                recipes[new_name] = recipes.pop(recipe_name)
                recipes[new_name].name = new_name
                print(f"Recipe '{recipe_name}' has been renamed to '{new_name}'.")
                # Save to json file
                auto_save()
            break

        elif userInput == '2':
            # Updating ingredients
            update_ingredients(recipe_name)
            # Save to json file
            auto_save()
            break

        elif userInput == '3':
            # Updating instructions
            update_instructions(recipe_name)
            # Save to json file
            auto_save()
            break

        elif userInput == '4':
            # Updating category
            new_category = get_valid_input("Enter the new category of the recipe: ",
                                           lambda x: len(x) > 0 and not x.isdigit())
            if new_category != recipes[recipe_name].category:
                recipes[recipe_name].category = new_category
                print(f"Category for '{recipe_name}' has been changed to '{new_category}'.")
                # Save to json file
                auto_save()
            else:
                print(f"No changes made. The recipe '{recipe_name}' is already in the category '{new_category}'.")
            break

        elif userInput == '5':
            # Updating calories
            update_numeric_attribute(recipe_name, 'calories', "Enter the new calories of the recipe: ")
            # Save to json file
            auto_save()
            break

        elif userInput == '6':
            # Updating carbs
            update_numeric_attribute(recipe_name, 'carbs', "Enter the new carbs of the recipe: ")
            # Save to json file
            auto_save()
            break

        elif userInput == '7':
            # Updating protein
            update_numeric_attribute(recipe_name, 'protein', "Enter the new protein count of the recipe: ")
            # Save to json file
            auto_save()
            break

        elif userInput == '8':
            print("Returning to main menu.\n")
            printMenu()
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


def get_valid_input(prompt, validation_func):
    """Get input from the user and validate it using the provided function."""
    while True:
        user_input = input(prompt).strip()
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")


def update_numeric_attribute(recipe_name, attribute, prompt):
    """Updates a numeric attribute of a recipe."""
    new_value = get_valid_input(prompt, lambda x: x.isdigit() and int(x) >= 0)
    new_value_int = int(new_value)
    if new_value_int != getattr(recipes[recipe_name], attribute):
        setattr(recipes[recipe_name], attribute, new_value_int)
        print(f"{attribute.capitalize()} for '{recipe_name}' has been changed to '{new_value_int}'.")
    else:
        print(f"No changes made. The recipe '{recipe_name}' already has '{new_value_int}' {attribute}.")


def update_ingredients(recipe_name):
    """Handle updating ingredients for a recipe."""
    current_ingredients = recipes[recipe_name].ingredients
    print(f"Current ingredients: {', '.join(current_ingredients)}")

    print("\nChoose an action:")
    print("1. Add new ingredients")
    print("2. Remove ingredient")
    print("3. Replace all ingredients")
    print("4. Go back to previous menu")
    while True:
        ingredient_action = get_valid_input("Enter your choice: ", lambda x: len(x) > 0 and x.isdigit())
        if ingredient_action == '1':
            new_ingredients_input = get_valid_input("Enter the new ingredients separated by commas: ",
                                                    lambda x: len(x) > 0)
            new_ingredients = [ing.strip() for ing in new_ingredients_input.split(',')]

            for ing in new_ingredients:
                if not ing:  # Check if ingredient is empty after stripping
                    print(f"Invalid ingredient '{ing}'. Please enter a valid ingredient.")
                    continue

                if ing not in current_ingredients:
                    recipes[recipe_name].ingredients.append(ing)
                    current_ingredients.add(ing)
                    print(f"Added '{ing}' to the ingredients.")
                else:
                    print(f"{ing} is already in the list of ingredients.")
            break

        elif ingredient_action == '2':
            ingredient_to_remove = get_valid_input("Enter the ingredient to remove: ",
                                                   lambda x: len(x) > 0 and not x.isdigit())
            if ingredient_to_remove in current_ingredients:
                recipes[recipe_name].ingredients = [ing for ing in recipes[recipe_name].ingredients if
                                                    ing != ingredient_to_remove]
                print("")
                print(f"Ingredient {ingredient_to_remove} removed.")
                break
            else:
                print(f"{ingredient_to_remove} is not in the list of ingredients.")
                break

        elif ingredient_action == '3':
            new_ingredients = get_valid_input("Enter the new ingredients separated by commas: ",
                                              lambda x: len(x) > 0 and not x.isdigit())
            new_ingredients = new_ingredients.split(',')
            recipes[recipe_name].ingredients = new_ingredients
            print("")
            print(f"Ingredient: '{new_ingredients}' replaced successfully.")
            break

        elif ingredient_action == '4':
            print("Returning to previous menu.")
            printMenu()

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def update_instructions(recipe_name):
    """Handle updating instructions for a recipe."""
    current_instructions = recipes[recipe_name].instructions
    print(f"Current instructions: {'. '.join(current_instructions)}")

    print("\nChoose an action:")
    print("1. Add additional instructions")
    print("2. Replace all instructions")
    print("3. Go back to previous menu")

    while True:
        instruction_action = get_valid_input("Enter your choice: ", lambda x: len(x) > 0 and x.isdigit())
        if instruction_action == '1':
            new_instructions_input = get_valid_input("Enter the new instructions separated by periods: ",
                                                     lambda x: len(x) > 0)
            new_instructions = [instr.strip() for instr in new_instructions_input.split('.')]

            for instr in new_instructions:
                if not instr:  # Check if instructions is empty after stripping
                    print(f"Invalid instructions '{instr}'. Please enter a valid instructions.")
                    continue

                # If the instruction is valid, add it to the recipe's instructions
                recipes[recipe_name].instructions.append(instr)
                print(f"Added '{instr}' to the instructions.")
            # The break here exits the while loop after processing all new instructions
            break

        elif instruction_action == '2':
            new_instructions = get_valid_input("Enter the new instructions separated by periods: ",
                                               lambda x: len(x) > 0)
            new_instructions = new_instructions.split('.')
            recipes[recipe_name].instructions = new_instructions
            print("")
            print("Added instructions successfully.")
            break

        elif instruction_action == '3':
            print("Returning to previous menu.")
            printMenu()

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


def addRecipe():
    print("Please include the information of the recipe you would like to add:")
    while True:
        name = input("Enter the  name of the recipe: ").strip()
        if len(name) > 0 and not name.isdigit():
            break
        else:
            print("Please enter a valid name for the recipe.")

    while True:
        ingredients = [ing.strip() for ing in
                       input("Enter the ingredients of the recipe (comma-separated): ").split(',')]
        if len(ingredients) > 0 and not all(ing.isdigit() for ing in ingredients):
            break
        else:
            print("Please enter a valid ingredients for the recipe.")

    while True:
        instructions = [ins.strip() for ins in
                        input("Enter the  instructions of the recipe (period-separated): ").split('.')]
        if len(instructions) > 0:
            break
        else:
            print("Please enter a valid instructions for the recipe.")

    while True:
        print("Current categories: breakfast, lunch, dinner, dessert, snack")
        category = input("Enter the category of the recipe: ")
        if len(category) > 0 and not category.isdigit():
            break
        else:
            print("Please enter a valid category for the recipe.")

    while True:
        calories = input("Enter the calories of the recipe: ")
        if len(calories) > 0 and calories.isdigit():
            calories = int(calories)
            break
        else:
            print("Please enter a valid calories for the recipe.")

    while True:
        carbs = input("Enter the carbs of the recipe: ")
        if len(carbs) > 0 and carbs.isdigit():
            carbs = int(carbs)
            break
        else:
            print("Please enter a valid carbs for the recipe.")

    while True:
        protein = input("Enter the protein of the recipe: ")
        if len(protein) > 0 and protein.isdigit():
            protein = int(protein)
            print("")
            break
        else:
            print("Please enter a valid protein for the recipe.")

    # Create a new Recipe object
    newRecipe = RecipeClass.Recipe(name, ingredients, instructions, category, calories, carbs, protein)

    # Add the new recipe to the recipes dictionary
    recipes[newRecipe.name] = newRecipe

    # Save to json file
    auto_save()


def saveAllRecipesTojson(filename):
    saveAllRecipes = {name: vars(recipe) for name, recipe in recipes.items()}
    with open(filename, 'w') as f:
        json.dump(saveAllRecipes, f, indent=4)


def loadAllFromjson(filename):
    global recipes
    with open(filename, 'r') as f:
        recipesData = json.load(f)
        for name, data in recipesData.items():
            recipes[name] = RecipeClass.Recipe(**data)


def auto_save():
    """Automatically saves the current state of recipes to a JSON file."""
    filename = 'recipes.json'
    saveAllRecipesTojson(filename)
    print("All changes have been saved to the file.")


def delRecipe(recipeName):
    if recipeName in recipes:
        recipes.pop(recipeName)
        print(f"Recipe '{recipeName}' deleted successfully.")
        print("")
        # Save to json file
        auto_save()
    else:
        print(f"Recipe '{recipeName}' not found.")
        print("")


def printAllRecipes():
    for key, value in recipes.items():
        print(f"Recipe: {key}")
        print(value.printIngredients())
        print(value.printRecipe())
        print(value.printNutrition())
        print(value.printCategory())
        print("\n")


def printMenu():

    while True:
        print("")
        print("Main Menu")
        print("1: Add Recipe")
        print("2: View All Recipes")
        print("3: Search Recipe")
        print("4: Update Recipe")
        print("5: Delete Recipe")
        print("6: Exit")
        user_choice = input("Enter your choice: ")
        if (user_choice == '1' or user_choice == '2' or user_choice == '3'
                or user_choice == '4' or user_choice == '5' or user_choice == '6'):
            if user_choice == '1':
                # Code to add a recipe
                addRecipe()

            elif user_choice == '2':
                # Code to view all recipes
                printAllRecipes()

            elif user_choice == '3':
                # Code to search for a recipe
                searchRecipe()

            elif user_choice == '4':
                # Code to update a recipe
                recipe_name = input("Enter the name of the recipe to update: ")
                print("")
                if recipe_name in recipes:
                    updateRecipe(recipe_name)
                    print("")
                else:
                    print("Recipe not found. Please try again.")
                    print("")

            elif user_choice == '5':
                # Code to delete a recipe
                recipe_name = input("Enter the name of the recipe to delete: ")
                print("")
                delRecipe(recipe_name)
                print("")

            elif user_choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


def printRecipeDetails(recipe_name):
    recipe = recipes[recipe_name]
    print(f"Recipe: {recipe_name}")
    print(recipe.printIngredients())
    print(recipe.printRecipe())
    print(recipe.printNutrition())
    print(recipe.printCategory())
    print("\n")


def searchRecipe():
    print("How would you like to search for a recipe?")
    print("1: By name")
    print("2: By an ingredient")
    print("3: By category")
    print("4: By calories")
    print("5: Return to main menu")

    search_choice = input("Enter your choice: ")

    if search_choice == '1':
        # Code to search by name
        user_input = input("Enter the name (or part of the name) of the recipe: ").lower().split()
        found_recipes = []

        for recipe_name, recipe in recipes.items():
            recipe_words = recipe_name.lower().split()
            if any(word in recipe_words for word in user_input):
                found_recipes.append(recipe_name)

        if found_recipes:
            for recipe_name in found_recipes:
                print("")
                printRecipeDetails(recipe_name)
        else:
            print("")
            print("No recipes found with the given name.")

    elif search_choice == '2':
        # Code to search by ingredient
        ingredient_name = input("Enter an ingredient to look up a recipe: ").lower()
        found_recipes = []

        for recipe_name, recipe in recipes.items():
            if ingredient_name in [ingredient.lower() for ingredient in recipe.ingredients]:
                found_recipes.append(recipe_name)

        if found_recipes:
            for recipe_name in found_recipes:
                print("")
                printRecipeDetails(recipe_name)
        else:
            print("")
            print(f"No recipes found with ingredient '{ingredient_name}'.")

    elif search_choice == '3':
        # Code to search by category
        print("Current categories: breakfast, lunch, dinner, dessert, snack")
        category_name = input("Enter a category to look up a recipe: ").lower()
        found_recipes = []

        for recipe_name, recipe in recipes.items():
            if recipe.category.lower() == category_name:
                found_recipes.append(recipe_name)

        if found_recipes:
            for recipe_name in found_recipes:
                print("")
                printRecipeDetails(recipe_name)
        else:
            print("")
            print(f"No recipes found in the category '{category_name}'.")

    elif search_choice == '4':
        # Code to search by calories
        calory_count = input("Enter a calory limit to look up recipes at that calory and under: ")
        if calory_count.isdigit():
            calory_count = int(calory_count)
            found_recipes = []

            for recipe_name, recipe in recipes.items():
                if recipe.calories <= calory_count:
                    found_recipes.append(recipe_name)

            if found_recipes:
                for recipe_name in found_recipes:
                    print("")
                    printRecipeDetails(recipe_name)
            else:
                print("")
                print(f"No recipes found at or under '{calory_count}' calories.")
        else:
            print("")
            print("Please enter a valid calorie number to look up recipe.")

    elif search_choice == '5':
        print("")
        print("Returning to main menu.\n")

    else:
        print("Invalid choice. Number has to be between 1 and 5.")
        searchRecipe()
