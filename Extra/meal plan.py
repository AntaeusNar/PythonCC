# attempt at a meal planning app of sorts with the ability to generate a weekly meal plan and
# ingredients /shopping lists.
# we will need a list of all of the meals, ingrediants of each meal, a main list of all ingrediants, a list of the days
# of the week
# functions for inputing new meals, buiding meal plans, and building the shopping list
# from typing import Any, Tuple, List
# days of the week
# days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# dictionary for all the ingredients with the ingredients as the key
# and the number of meal recipes using the ingredients as the value
# ingredients = {}
# individual meals will be a dictionary with a name and then the ingredients to allow for adding more things later
# meal = {'name' : '',
#         'ingredients' : ['', '']
#        }

import json


def new_meal() -> dict:
    meal = {'name': '', 'ingredients': []}
    prompt = 'Add a meal by typing a list separated by commas.  The first item in the list will be the meal\n' \
             'and the rest will be the ingredients. You will have a chance to review before ' \
             'saving. Enter q to go back.\n: '
    message = input(prompt)
    if message != 'q':
        stripedwords = [x.strip() for x in message.split(",")]
        words = [x.lower() for x in stripedwords]
        meal['name'] = words[0]
        meal['ingredients'] = words[1:]
        if len(meal['ingredients']) > 1:
            reply = 'So you want to add a meal called {} with {} ingredients ' \
                    'which are\n{} and {}.\n' \
                    'If so enter "y" otherwise enter "n"\n:' \
                .format(meal['name'].title(),
                        len(meal['ingredients']),
                        ', '.join(meal['ingredients'][:-1]),
                        meal['ingredients'][-1]
                        )
            message = input(reply)
            if message == 'y':
                return meal
        else:
            print('Not a very complex meal is it? Not many ingredients that one.')


def load_meals():   # used to load meals from json file
    filename = 'meals.json'
    try:
        with open(filename) as f_obj:
            meals = json.load(f_obj)
    except FileNotFoundError:
        print('No saved meals found.')
        return None
    else:
        print('Loaded {} meals'.format(len(meals)))
        for meal in meals:
            print(meal['name'].title())
        return meals


def save_meals(meals):   # used to save meals to json file
    filename = 'meals.json'
    with open(filename, 'w') as f_obj:
        json.dump(meals, f_obj)


def __main__():
    mastermeals = []
    maybemeals = load_meals()
    if type(maybemeals) == list:
        mastermeals = maybemeals
    mastermeals.append(new_meal())
    save_meals(mastermeals)


__main__()
