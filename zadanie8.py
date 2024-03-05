# ZADANIE 6
# Korzystając z filter() wyodrębnij z danej listy słowa zaczynające się na "a"
# Użyj map() do przekształcenia listy liczb w listę ich kwadratów
print("--ZADANIE 6--")
lista = ["ananas","agrest","banan","mleko","fryteczki","aaaaaaaaaAAAAAAAAAAAAAAA"]
def Filtrowanie(x):
    if x[0] == "a":
        return True
    else:
        return False
przefiltrowane = filter(Filtrowanie, lista)

for x in przefiltrowane:
    print(x)

def kwadraty(x):
    return x*x

liczby = [1,2,3,4]
wynik = map(kwadraty, liczby)
print(list(wynik))
