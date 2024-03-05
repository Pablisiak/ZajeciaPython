lista = ["ananas", "agrest", "banan", "mleko", "fryteczki", "aaaaaaaaaAAAAAAAAAAAAAAA"]


def filtrowanie(x):
    if x[0] == "a":
        return True
    else:
        return False


przefiltrowane = filter(filtrowanie, lista)

for x in przefiltrowane:
    print(x)


def kwadraty(x):
    return x*x


liczby = [1, 2, 3, 4]
wynik = map(kwadraty, liczby)
print(list(wynik))
