# rewrite of mealplan.
# An attempt at a meal planning app of sorts
# Goals: 1)save and load meals from json file, 2)add meals,
# 3)generate a random meal list, 4)generate matching shopping list

# meals stored in a list of dictionaries with a name and and a list of ingredients


import json                            # or saving and loading meals
from consolemenu import SelectionMenu  # menu


class MealList:  # Generate a meal list class holding the methods etc for making stuff happen

    def __init__(self, mealfile):  # create the listing
        self.meals = []
        self.mealfile = mealfile
        self.load()

    def load(self):  # Should try to load the file
        try:
            with open(self.mealfile) as f_obj:
                self.meals = json.load(f_obj)
        except FileNotFoundError:
            print('No saved meals found.')
        else:
            print('Loaded %d meals.' % len(self.meals))

    def save(self):  # Should save the file
        with open(self.mealfile, 'w') as f_obj:
            json.dump(self.meals, f_obj)

    def search(self, mealname):  # look for meal in list, return true and list of ingredients
        for meal in self.meals:
            if meal['name'] == mealname:
                isadded = True
                ingredients = meal['ingredients']
                return isadded, ingredients
        isadded = False
        return isadded

    def new(self, wordslist):  # Add a new meal to meals list
        meal = {'name': '', 'ingredients': []}  # dictionary of a meal
        meal['name'] = wordslist[0]
        meal['ingredients'] = wordslist[1:]
        if self.search(meal['name']):
            self.meals.append(meal)


def main_menu(menu_list):
    selection = SelectionMenu.get_selection(menu_list, "Meal Planning with Mary Poppins!")
    return selection


def all_done():         # Time to be done
    return 'exit'


def new_meal():         # add that new meal!!
    return 'fun'


def all_meals():        # list all those fine meals!
    return 'all'


def search_meals():     # Hunting for that perfect dish
    return 'code'


def build_plan():       # give me a meal plan!
    return 'fish'


def select_function(selection, switcher_list):
    # making a list of functions that will be called
    switcher = dict(enumerate(switcher_list))
    # now we pull the function from the switcher
    func = switcher.get(selection)
    # call the function!!!!!!!!!!
    return func()


def __main__():
    switcher_list = [new_meal, all_meals, search_meals, build_plan, all_done]
    menu_list = ["New Meal", "All Meals", "Search Meals", "Build that Meal Plan!"]
    while True:
        if select_function(main_menu(menu_list), switcher_list) == 'exit':
            break


__main__()

