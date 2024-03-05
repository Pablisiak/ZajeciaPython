def liczby(lista):
    return [x for x in lista if x % 2 == 0]


print(liczby([1,  2, 3, 4, 5, 6, 7, 8]))


def poleprostokata(a, b):
    obl = lambda a, b: a * b
    pole = obl(a, b)
    return pole


print(poleprostokata(10, 13))
