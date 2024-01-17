from itertools import product

c = 0

def have_two_adjacent_odd_digits_in_base13(s):
    for i in range(len(s) - 1):
        digit1 = int(s[i], 13)
        digit2 = int(s[i + 1], 13)
        if digit1 % 2 == 1 and digit2 % 2 == 1:
            return True
    return False

for x in product(('0123456789ABC'), repeat=6):
    s = ''.join(x)
    if s[0] != '0' and s.count('5') <= 1 and not have_two_adjacent_odd_digits_in_base13(s):
        c += 1

print(c)

# Сколько существует тринадцатеричных шестизначных чисел, не содержащих в своей записи более одной цифры 5,
# в которых никакие две нечётные цифры не стоят рядом?
# ответ верный + написал функцию для проверки проверки одинаковых цифр рядом