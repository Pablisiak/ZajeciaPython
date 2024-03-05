from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

max_number = reduce(lambda x, y: x if x > y else y, numbers)
print("Największa liczba:", max_number)

def calculate_average(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    return total / len(numbers)

average = calculate_average(numbers)
print("Średnia:", average)