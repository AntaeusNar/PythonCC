
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car != 'subaru':
        print(car)
    else:
        print(car.title())

if 'bmw' in cars:
    place = cars.index('bmw')
    print("Honey, I am home in my shiny " + cars[place].upper() + "!!!")
if 'telsa' not in cars:
    print("We are all going to die")
else:
    print("you know, you might be doing life wrong")