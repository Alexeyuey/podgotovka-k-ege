from itertools import *

c = 0
for x in product(('ДСРЩЭ'), repeat=4):
    s = ''.join(x)
    c += 1
    if s == 'ЩДЩД':
        print(c)
        break

# ответ верный = 391, на будущее: нужно обязательно учитывать список данный в задании
#
# Все 4-буквенные слова, составленные из букв Щ, Э, Д, С, Р, записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
#
# ДДДД
# ДДДР
# ДДДС
# ДДДЩ
# ДДДЭ
# ДДРД
# ...
# Под каким номером стоит слово ЩДЩД?