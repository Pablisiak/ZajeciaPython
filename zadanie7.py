from itertools import groupby
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
grouped_numbers = {k: list(v) for k, v in groupby(numbers, key=lambda x: x % 2)}
print(grouped_numbers)
