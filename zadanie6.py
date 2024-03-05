def square(x):
    return x * x

numbers = [6,7,8,9,10]
squared_numbers = list(map(square, numbers))

print(squared_numbers)