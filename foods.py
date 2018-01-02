# Копирование списков
my_foods = ['pizza', 'falafel', 'carrot cake']
other_foods = my_foods[:]

# # Такое копирование не пройдет, "other_foods" будет отслеживать изменения в списке "my_foods"
# other_foods = my_foods

print(my_foods)
print(other_foods)

my_foods.append('meet')
other_foods.append('banana')

print(my_foods)
print(other_foods)