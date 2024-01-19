import json


class Recipe:
    def __init__(self, name, ingredients, instructions, category, calories, carbs, protein):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category
        self.calories = calories
        self.carbs = carbs
        self.protein = protein

    def printRecipe(self):
        return f"Instructions: {self.instructions}"

    def printIngredients(self):
        return f"Ingredients: {self.ingredients}"

    def printNutrition(self):
        return f"Calories: {self.calories}\nCarbs: {self.carbs}\nProtein: {self.protein}"

    def printCategory(self):
        return f"Category: {self.category}"

    def save2json(self, filename):
        recipeDict = {'name': self.name, 'ingredients': self.ingredients, 'instructions': self.instructions,
                      'category': self.category, 'calories': self.calories, 'carbs': self.carbs,
                      'protein': self.protein}
        with open(filename, 'w') as f:
            f.write(json.dumps(recipeDict, indent=4))

    def loadFromjson(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
            self.name = data['name']
            self.ingredients = data['ingredients']
            self.instructions = data['instructions']
            self.category = data['category']
            self.calories = data['calories']
            self.carbs = data['carbs']
            self.protein = data['protein']
