from functools import reduce

numbers = [6,7,8,9,10]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print(sum_of_numbers)