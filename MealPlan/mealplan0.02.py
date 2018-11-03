# rewrite of mealplan.
# An attempt at a meal planning app of sorts
# Goals: 1)save and load meals from json file, 2)add meals,
# 3)generate a random meal list, 4)generate matching shopping list

# meals stored in a list of dictionaries with a name and and a list of ingredients


import json                            # or saving and loading meals
import random                          # add that random!!!!
import copy                            # keep those things seperate....
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
            print('Save file %s not found.' % self.mealfile)
        else:
            print('Loaded %d meals.' % len(self.meals))

    def save(self):  # Should save the file
        with open(self.mealfile, 'w') as f_obj:
            json.dump(self.meals, f_obj)
        print('Saved %d meals to file %s' % (len(self.meals), self.mealfile))

    def count(self):    # This slick son-of-a-bitch opens each meal in the list, counts the ingredients
                        # and returns a count of the ingredients and total number of meals!!!
        return len(self.meals), len(self.ing_list()[0]), self.ing_list()[1]

    def ing_list(self, plan=[]):    # returns a dic of all ingredients with number of times used,
                                    # if passed a meal list, will only pull those relevant ingredients
        ing_dic = {}
        ing_count = 0
        if not plan:
            for each in self.meals:
                for x in each['ingredients']:
                    ing_count += 1
                    if x not in ing_dic:
                        ing_dic[x] = 1
                    else:
                        ing_dic[x] += 1
        else:
            for meal in self.meals:
                for y in plan:
                    if meal['name'] == y:
                        for x in meal['ingredients']:
                            ing_count += 1
                            if x not in ing_dic:
                                ing_dic[x] = 1
                            else:
                                ing_dic[x] += 1
        return ing_dic, ing_count

    def print_all(self):
        for meal in self.meals:
            print(meal['name'].title())

    def search(self, mealname):  # look for meal in list, return true and list of ingredients
        isadded = False
        for meal in self.meals:
            if meal['name'] == mealname:
                isadded = True
                ingredients = meal['ingredients']
                return isadded, ingredients
            else:
                isadded = False
        return isadded

    def new(self, wordslist):  # Add a new meal to meals list
        meal = {'name': '', 'ingredients': []}  # dictionary of a meal
        meal['name'] = wordslist[0]
        meal['ingredients'] = wordslist[1:]
        if not self.search(meal['name']):
            self.meals.append(meal)
            return True
        else:
            # print('There is a meal with that name already.')
            return False

    def remove(self, meal):     # remove meal
        try:
            removed = self.meals.pop(meal)
            return '%s found and removed' % removed['name'].title()
        except IndexError:
            return '%s was not found.' % meal.title()


def press_enter():
    input("Please Press Enter to continue.....")


def all_done(these_meals):         # Time to be done
    these_meals.save()
    return 'exit'


def new_meal(these_meals):         # add that new meal!!
    prompt = 'Add a meal by typing a list separated by commas.  The first item in the list will be the meal\n' \
             'and the rest will be the ingredients. You will have a chance to review before ' \
             'saving. Enter "b" to go back.\n: '
    message = input(prompt)
    if message != 'b':
        stripedwords = [x.strip() for x in message.split(",")]
        wordslist = [x.lower() for x in stripedwords]
        reply = 'So you want to add a meal called {} with {} ingredients ' \
                'which are\n{} and {}.\n' \
                'If so enter "y" otherwise enter "n"\n:' \
            .format(wordslist[0].title(),
                    (len(wordslist)-1),
                    ', '.join(wordslist[1:-1]),
                    wordslist[-1]
                    )
        message = input(reply)
        if message == 'y':
            if these_meals.new(wordslist):
                return 'Added %s to the list! Now you have %d meals' % (wordslist[0].title(), these_meals.count()[0])
            else:
                return "Couldn't add meal, it looks like %s is already in the list." % wordslist[0].title()


def all_meals(these_meals):        # list all those fine meals!
    these_meals.print_all()
    press_enter()
    return 'Listed all %d meals.' % these_meals.count()[0]


def search_meals(these_meals):     # Hunting for that perfect dish
    prompt = 'Which meal do you want to try to find?"'
    meal = input(prompt).lower().strip()
    if these_meals.search(meal):
        return 'We found %s in the meal list! It is made with %s' % (meal.title(), ', '.join(these_meals.search(meal)[1]).title())
    else:
        return "We couldn't find %s in the meal list." % meal.title()


def build_plan(these_meals):       # give me a meal plan!
    those_meals = copy.deepcopy(these_meals)
    random.shuffle(those_meals.meals)
    names = []
    for x in those_meals.meals[0:8]:
        names.append(x['name'])
    shop_list = those_meals.ing_list(names)[0]
    print(shop_list)
    new_shop_list = []
    for x, y in shop_list.items():
        string = x.title() + '(' + str(y) + ')'
        new_shop_list.append(string)
    return 'Here is a list of meals for you! %s.  Ingredients you need are %s' % (
        ', '.join(names).title(),
        ', '.join(new_shop_list)
        )


def count_meals(these_meals):
    return 'Counted %d meals with %d unique ingredients and %d total ingredients.' % these_meals.count()


def plan_testing(these_meals):      # var testing stuff
    return 'crap'


def select_function(selection, switcher_list, these_meals):
    # making a list of functions that will be called
    switcher = dict(enumerate(switcher_list))
    # now we pull the function from the switcher
    func = switcher.get(selection)
    # call the function!!!!!!!!!!
    return func(these_meals)


def main_menu(menu_list, status):
    menu = SelectionMenu(menu_list, "Meal Planning with Mary Poppins", prologue_text=status)
    menu.show()
    menu.join()
    selection = menu.selected_option
    return selection


def __main__():
    these_meals = MealList('meals.json')
    switcher_list = [new_meal, all_meals, search_meals, build_plan, count_meals, plan_testing, all_done]
    menu_list = ["New Meal", "All Meals", "Search Meals", "Build that Meal Plan!", "How many meals now?", "Meal Plan Test"]
    status = "Just getting started!"
    while True:
        status = select_function(main_menu(menu_list, status), switcher_list, these_meals)
        if status == 'exit':
            break


__main__()

