def square_number(number):
    return number ** 2

def add_five(number):
    return number + 5

def apply_functions_to_list(numbers, *functions):
    result = []
    for number in numbers:
        transformed_number = number
        for function in functions:
            transformed_number = function(transformed_number)
        result.append(transformed_number)
    return result


numbers = [1, 2, 3, 4, 5]


functions_to_apply = [square_number, add_five]

transformed_numbers = apply_functions_to_list(numbers, *functions_to_apply)

print(transformed_numbers)
