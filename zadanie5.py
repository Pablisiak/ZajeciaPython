# ZADANIE 5
# Napisz funkcję, która przyjmuje listę liczb i zwraca listę zawierającą tylko liczby parzyste. Użyj lamba do stworzenia funkcji obliczającej pole prostokąta na podstawie długości jego boków
print("--ZADANIE 5--")
def liczby(lista):
    return [x for x in lista if x % 2 == 0]

print(liczby([1, 2, 3, 4, 5, 6, 7, 8]))

def poleprostokata(a,b):
    obl = lambda a, b: a * b
    pole = obl(a,b)
    return pole

print(poleprostokata(10,13))