check_is_palindrome = lambda s: s.lower().replace(" ", "") == s[::-1].lower().replace(" ", "")
print(check_is_palindrome("zakaz"))
