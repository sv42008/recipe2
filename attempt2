# ---- README -----
"""
cal = calories per 100g     
 """

# ---- IMPORTING LIBRARIES -----



# ---- GLOBAL VARIABLES -----
list_Ingred = []
list_Recipe = []


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
    def __init__(self, name: str, cal: int, mealtype = str, priority = 0, ):
        super().__init__(name, cal)
        self.priority = 0
        self.mealtype = mealtype
        self.append_to_list(self, list_Recipe)
        self.ingredients = []

    def create_recipe(self, List):
        for t in range(len(List)):
            self.ingredients.append(List[t])
        for Ingred in self.ingredients:
            print(Ingred.name)

    def update_priority()
        x = 
        self.priority = x


# ---- FUNCTIONS -----



# ---- COMMAND LINE -----
# breakfast_cookbook = Cookbook("Breakfast")
# lunch_cookbook = Cookbook("Lunch")
# dinner_cookbook = Cookbook("Dinner")



ketchup = Ingred("Ketchup", 50, 200)
banana = Ingred("Banana", 200, 200)
# ketchup.append_to(list_Ingred)
# banana.append_to(list_Ingred)

for Ingred in list_Ingred:
    print (Ingred.name)

banana.remove_ingred()

for Ingred in list_Ingred:
    print (Ingred.name)

BananaKetchup = Recipe("Banana and Ketchup Sabzi", 230, "Breakfast")
BK = [banana, ketchup]  ## need to replace this list creation via input
BananaKetchup.create_recipe(BK)
