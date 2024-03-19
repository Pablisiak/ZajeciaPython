def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
first_10_fib = [next(fib) for _ in range(10)]
print(first_10_fib)
