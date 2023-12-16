a = 'слон'
c = 0
for x in a:
    for y in a:
        for z in a:
            for w in a:
                for i in a:
                    s = x + y + z + w + i
                    if (s.count('0') == 3) or (s.count('0') == 2) or (s.count('0') == 1) or (s.count('0') == 0):
                        c += 1
print(c)