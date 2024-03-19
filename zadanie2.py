from itertools import combinations


def all_combinations(elements):
    return list(combinations(elements, 2))


list1 = [6, 7, 8, 9]
print(all_combinations(list1))
