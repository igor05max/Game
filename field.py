from pprint import pprint
from random import choice


def dist(x, y, x2, y2):
    return (((x - x2) ** 2) + ((y - y2) ** 2)) ** 0.5


def field_constructor():
    field = [
        [1 for _ in range(14)],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1 for _ in range(14)]
    ]
    x_exit, y_exit = choice([i for i in range(1, 9)]), 14
    x, y = 6, 1
    d = dist(x, y, x_exit, y_exit)
    field[x][y] = 9
    true = False
    tt = 0
    while (x, y) != (x_exit, y_exit - 1):
        tt += 1
        if tt > 300:
            pprint(field)
            print("\n", x_exit, y_exit, "\n")
            field = [
                [1 for _ in range(15)],
                [2, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 2],
                [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
                [1 for _ in range(14)]
            ]
            return field
        set_t = set()
        for t in (x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1):
            if field[t[0]][t[1]] == 0:
                if not true:
                    set_t.add(t)
                else:
                    d2 = dist(t[0], t[1], x_exit, y_exit)
                    if d >= d2:
                        d = d2
                        set_t.add(t)
        if set_t:
            x, y = set_t.pop()
        else:
            x_, y_ = choice([(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)])
            if field[x_][y_] in (0, 9):
                x, y = x_, y_
        field[x][y] = 9
        true = False if true else True

    for i, elem in enumerate(field):
        for j, el in enumerate(elem):
            if el == 0:
                if choice((1, 0)):
                    field[i][j] = 1
                    continue
            if el == 9:
                field[i][j] = 0
    field[x_exit][y_exit] = 2
    print("TRUE")
    return field


# field = field_constructor()
field = [
                [1 for _ in range(15)],
                [2, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 2],
                [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
                [1 for _ in range(14)]
            ]

field_ = {}
for i, elem in enumerate(field):
    for j, el in enumerate(elem):
        if el != '.':
            if el == 1:
                field_[(i * 100, j * 100)] = '1'
            elif el == 2:
                field_[(i * 100, j * 100)] = '2'
mass = []
for i, elem in enumerate(field):
    for j, el in enumerate(elem):
        if el == 1:
            mass.append((i // 100 * 100, j // 100 * 100))

