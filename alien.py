# Словари
alien_0 = {
    'color': 'green',
    'points': 5
}

# print(alien_0)
# print('\nAlien skin color: ' + str(alien_0['color']))
# print('Alien danger points: ' + str(alien_0['points']) + '\n')

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
del alien_0['x_position'], alien_0['y_position']
print(alien_0)
