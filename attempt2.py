# ---- README -----
"""
cal = calories per 100g     

need to find a way of creating List_ingreds and List_amounts.
        maybe combining them into an array and inserting the whole array may be a better option.
 """

# ---- IMPORTING LIBRARIES -----
from array import *


# ---- GLOBAL VARIABLES -----
list_Ingred = [] # stock
list_Recipe = [] # cookbook


# ---- GUI_TKINTER -----



# ---- CLASSES DEFINED -----

class Food():
    def __init__(self, name: str, cal: int,):
        self.name = name
        self.cal = cal
    
    def append_to_list(self, Food, List):
        List.append(Food)

    def remove_from_list(self, Food, List):
        List.remove(Food)

class Ingred(Food):
    def __init__(self, name: str, cal: int, amount: float):
        super().__init__(name, cal)
        self.append_to_list(self, list_Ingred)
    
    def remove_ingred(self):
        self.remove_from_list(self, list_Ingred)
        

class Recipe(Food):
    def __init__(self, name: str, cal: int, mealtype: str, rating: int, servings: int, priority: int):
        super().__init__(name, cal)
        self.priority = 0  # this may be an issue, if every object ends up having priority 0.
        self.mealtype = mealtype
        self.rating = rating
        self.servings = servings
        self.calperserving = 0.0
        self.append_to_list(self, list_Recipe)
        self.ingredients = []
         
       
    def create_recipe(self, List_ingreds: list, List_amounts: list):
        self.ingredients.insert(0, List_ingreds)
        self.ingredients.insert(1, List_amounts)

         #  loop to add total calories in recipe
        for aa in range(len(self.ingredients)):
            self.calperserving += (self.ingredients[0][aa].cal/100 * self.ingredients[1][aa])
        self.calperserving = self.calperserving/self.servings

    def update_rating(self, ratingnew : int):
        self.rating = ratingnew
        

# ---- FUNCTIONS -----



# ---- COMMAND LINE -----

ketchup = Ingred("Ketchup", 50, 200)
banana = Ingred("Banana", 200, 200)


BananaKetchup = Recipe("Banana and Ketchup Sabzi", 230, "Breakfast", 0, 2, 0)
BK = [banana, ketchup]
BKAMOUNTS =  [100, 20]  ## need to replace this list creation via input, also no input for amount.
BananaKetchup.create_recipe(BK, BKAMOUNTS)
BananaKetchup.update_rating(2)
