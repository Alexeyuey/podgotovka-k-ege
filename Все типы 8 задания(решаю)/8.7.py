from itertools import *

c = 0

def have_two_adjacent_odd_digits_in_base13(s):
    for i in range(len(s) - 1):
        digit1 = int(s[i], 12)
        digit2 = int(s[i + 1], 12)
        if :
            return True
    return False

for x in product(('0123456789ABC'), repeat=7):
    s = ''.join(x)

# не сделал сложно чет
# Сколько 7 разрядных двенадцатеричных чисел существует, в которых разряды, делящиеся без остатка на 3, и разряды, не делящиеся без остатка на 3, чередуются?