# ---- README -----
"""
cal = calories per 100g     

need to find a way of creating List_ingreds and List_amounts.
        maybe combining them into an array and inserting the whole array may be a better option.

weightage of different factors to make priority fn accurate/useful 
        can pot add a slider in the app to change this setting

rr, cc, pp ::: rating coeff, calperserving coeff, priceperserving  coeff
 """

# ---- IMPORTING LIBRARIES -----
import tkinter as tk
from tkinter import Label, Entry, Button, Canvas

# ---- GLOBAL VARIABLES -----
Stock = [] 
Cookbook = [] 

rr = 1.0
cc = 1.0
pp = 1.0

# GUI SECTION:
Title1: str = "Welcome to your digital  "
Title2: str = "cookbook!"
Subtitle1: str = "New Recipe Name: "
# ---- FUNCTIONS -----
def new_recipe():
    recipename_input = Recipe_Name.get()
    mealtype_input = Mealtype_Input.get()

    recipename = Recipe(recipename_input, 0, mealtype_input )


# ---- CLASSES DEFINED -----

class Food():
    def __init__(self, name: str, cal: float):
        self.name = name
        self.cal = cal
    
    def append_to_list(self, Food, List):
        List.append(Food)

    def remove_from_list(self, Food, List):
        List.remove(Food)

    def hello_world(self):
        print("Surabhi")


class Ingred(Food):
    def __init__(self, name: str, cal: float, amount: float, price = float):
        super().__init__(name, cal)
        self.append_to_list(self, Stock)
        self.price = price
    
    def remove_ingred(self):
        self.remove_from_list(self, Stock)
        

class Recipe(Food):
    def __init__(self, name: str, mealtype: str, rating: float, servings: int, priority: float, cal = 0.0):
        super().__init__(name, cal)
        self.priority = 0  # this may be an issue, if every object ends up having priority 0.
        self.mealtype = mealtype
        self.rating = rating
        self.servings = servings
        self.calperserving = 0.0
        self.priceperserving = 0.0
        self.ingredients = []
        #  adds recipe to Cookbook
        self.append_to_list(self, Cookbook)
       
       
    def create_recipe(self, List_ingreds: list, List_amounts: list):
        self.ingredients.insert(0, List_ingreds)
        self.ingredients.insert(1, List_amounts)

        #  calculates priceperserving and calperserving
        for aa in range(len(self.ingredients)):
            self.calperserving += (self.ingredients[0][aa].cal/100 * self.ingredients[1][aa])
            self.priceperserving += (self.ingredients[0][aa].price/100 * self.ingredients[1][aa])
        self.calperserving = self.calperserving/self.servings
        self.priceperserving = self.priceperserving/self.servings
        

    def update_rating(self, ratingnew: int):
        if ratingnew in range (0, 10):
            self.rating = ratingnew
        else:
            print("Re-enter the rating, between 0 and 10 " + "\n")
            cc = int(input())
            return self.update_rating(cc)

    def calculate_priority(self):  
        self.priority = (rr * self.rating) + (cc * self.calperserving) + (pp * self.priceperserving)


# ---- GUI_TKINTER -----

window = tk.Tk()  # open window in tkinter
window.geometry("900x900")  # window initial size
window.resizable(0,0)  # fixed window size
window.eval('tk::PlaceWindow %s NW' % window.winfo_toplevel())  # window initial position
window.configure(background = "black")


Label (window, text= Title1, bg="black", fg="white", font = "CenturySchoolbook 64 italic").grid(row=0, column=0)
Label (window, text= Title2, bg="black", fg="white", font = "CenturySchoolbook 64 italic").grid(row=1, column=0)
Canvas (window, bg = "black", bd = "1", height = "1", width = "800").grid(row=2, column=0)
Label (window, text= Subtitle1, bg="black", fg="white", font = "CenturySchoolbook 20 bold").grid(row=3, column=0)
Recipe_Name = str()
Mealtype_Input = str()
Entry (textvariable = Recipe_Name , width = "30").grid(row = 4, column = 0)
Entry (textvariable = Mealtype_Input, width = "30").grid(row = 4, column = 0)
Confirm_name = Button(window, text = "Ok", width = 10, height = 1, command = new_recipe).grid(row = 5, column = 0)

window.mainloop() # keep window open 




# ---- COMMAND LINE -----


ketchup = Ingred("Ketchup", 50, 200, 3.99)
banana = Ingred("Banana", 200, 200, 1.39)


BananaKetchup = Recipe("Banana and Ketchup Sabzi", "Breakfast", 0, 2, 0)
BK = [banana, ketchup]
BKAMOUNTS =  [100, 20]  ## need to replace this list creation via input, also no input for amount.
BananaKetchup.create_recipe(BK, BKAMOUNTS)
BananaKetchup.update_rating(9)
