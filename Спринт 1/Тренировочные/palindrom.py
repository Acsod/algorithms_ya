# Палиндром
# Помогите Васе понять, будет ли фраза палиндромом. Учитываются только буквы и цифры,
# заглавные и строчные буквы считаются одинаковыми.
# Решение должно работать за O(N), где N — длина строки на входе.


import re 


def is_palindrome(line: str) -> bool:
    text = ''.join(re.findall(r'[a-zA-Z0-9]', line.lower()))
    return text == text[::-1]


print(is_palindrome(input().strip()))
