# Списки вложений
aliens = []

for aliens_number in range(30):
    new_alien = {'color': 'red', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print('')

for alien in aliens[0:3]:

    if alien['color'] == 'red':
        alien['color'] = 'pink'
        alien['points'] = 10
        alien['speed'] = 'middle'

        for alien_red in aliens[0:1]:
            if alien_red['color'] == 'pink':
                alien_red['color'] = 'deepink'
                alien_red['speed'] = 'fast'
                alien_red['points'] = 15

# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
    print(alien)

print("Total number of aliens: " + str(len(aliens)))

print('')
