# ZADANIE 4
# Przekazanie funkcji jako argument
print("--ZADANIE 4--")
def fun1(t1):
    print(t1)

def fun2(fun, arg1=""):
    fun(arg1)

fun2(fun1, "Działa")