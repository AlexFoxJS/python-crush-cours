# numbers = list(range(0, 18, 2))
# squares = []
#
# for num in numbers:
#     squares.append(num ** 2)

# Скокращенный вариант записи по средством - "генератора списков"
squares = [num ** 2 for num in range(0, 18, 2)]


print(squares)

print('Min value - ' + str(min(squares)))
print('Max value - ' + str(max(squares)))
print('Sum - ' + str(sum(squares)))