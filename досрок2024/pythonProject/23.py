def f(x, y):
    if x < y or x == 12 or x == 15:
        return 0
    if x == y:
        return 1
    moves = [f(x - 1, y)]
    if x % 3 == 0:
        moves.append(f(x // 3, y))
    if x % 2 == 0:
        moves.append(f(x // 2, y))
    return sum(moves)

print(f(19, 1))
