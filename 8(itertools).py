from itertools import *

w = (p for p in permutations ('КАПКАН"))
if ''.join(p).count('AA')+''.join(p).count('КК'):
    print(len(w))  