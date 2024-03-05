def analyze_data(data):
    match data:
        case (x, y):
            return f"Tupla z elementami {x} i {y}"
        case [x, y, z]:
            return f"Lista z elementami {x}, {y}, i {z}"
        case _:
            return "Nieznany typ"

print(analyze_data((1, 2)))
print(analyze_data([1, 2, 3]))