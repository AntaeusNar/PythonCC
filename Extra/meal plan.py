# attempt at a meal planning app of sorts with the ability to generate a weekly meal plan and
# ingredients /shopping lists.

# we will need a list of all of the meals, ingrediants of each meal, a main list of all ingrediants, a list of the days
# of the week

# functions for inputing new meals, buiding meal plans, and building the shopping list
from typing import Any, Tuple, List

# days of the week
# days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# list for all the meals
meals = []

# dictonary for all the ingredients with the ingredants as the key and the number of meal recipes using the ingredants
# as the value
# ingredients = {}

# individual meals will be a dictonay with a name and then the ingredients to allow for adding more things later
# meal = {'name' : '',
#         'ingredients' : ['', '']
#        }



def add_meal():
    meal = {'name': '', 'ingredients': []}
    prompt = 'Add a meal by typing a list seperated by commas.  The first item in the list will be the meal ' \
             'and the rest will be the ingredients. You will have a chance to review before ' \
             'saving. Enter q to go back.\n: '
    message = input(prompt)
    if message != 'q':
        stripedwords = [x.strip() for x in message.split(",")]
        words = [x.lower() for x in stripedwords]
        meal['name'] = words[0]
        meal['ingredients'] = words[1:]
        reply = 'So you want to add a meal called {} with {} ingredients \n' \
                'and these ingredients are {}.\n' \
                'If so enter "y" otherwise enter "n"'\
                .format(meal['name'].upper(), len(meal['ingredients']), ', '.join(meal['ingredients']))
        print(reply)


add_meal()

