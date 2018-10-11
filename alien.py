alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_pos'] = 0
alien_0['y_pos'] = 25

print(alien_0)

print("The alien is " + alien_0['color'] +".")

alien_0['speed'] = 'medium'
print("Original x & y positions: " + str(alien_0['x_pos']) + ', ' + str(alien_0['y_pos']))

for key, value in alien_0.items():
    print('\nKey: ' + key)
    print("Value: " + value)