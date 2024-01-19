try:
    import RecipeFunctions
except ModuleNotFoundError:
    print("Module to import not found")


# Main loop
def main():
    try:
        # Load initial recipes from the JSON file at the start of the program
        initial_recipes_file = 'initial_recipes.json'  # Replace with your JSON file name if necessary
        RecipeFunctions.loadAllFromjson(initial_recipes_file)
        RecipeFunctions.auto_save()
    except FileNotFoundError:
        print("ERROR file not found.")

    RecipeFunctions.printMenu()


if __name__ == "__main__":
  main()