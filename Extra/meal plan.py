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


def is_meal_new(meal) -> bool:
    # when given a meal it will check to see if the meal is in the exciting list
    if meal not in meals:
        return True


meals.append(new_meal())

print(meals)
