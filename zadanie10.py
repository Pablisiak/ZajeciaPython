def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))

file_path = 'zadanie10-large_file.txt'
lines_gen = read_large_file(file_path)
for line in lines_gen:
    print(line)
