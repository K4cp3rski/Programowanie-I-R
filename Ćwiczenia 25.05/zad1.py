from functools import reduce
# Kod 1
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
over_75 = list(filter(lambda x: x > 75, scores))
print(over_75)

# Kod 2
numbers = [3, 4, 6, 9, 34, 12]
result = reduce(lambda x, y: x + y, numbers, 10)
print(result)

# Kod 3
my_pets = ['alfred', 'tabitha', 'william', 'arla']
print(list(map(lambda x: str.upper(x), my_pets)))#