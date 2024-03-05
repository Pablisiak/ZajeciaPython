words = ["hello", "world", "Paweł", "super", "śmiga", "kocham", "pythona"]
long_words = list(filter(lambda word: len(word) > 5, words))

print(long_words)