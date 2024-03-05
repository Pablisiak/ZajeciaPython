def update_tuple(original_tuple, value, index):
    temp_list = list(original_tuple)
    temp_list[index] = value
    return tuple(temp_list)

my_tuple = (4,5,6)
updated_tuple = update_tuple(my_tuple, 7, 0)

print(updated_tuple)