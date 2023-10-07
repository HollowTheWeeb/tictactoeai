class BaseAI:

def check_two_and_place(self, gameboard, marktocheck, marktoplace):
    for i in range(3):
        markcount = 0
        _count = 0
        last_ = 0

        for j in range(3):
            if gameboard[i][j] == marktocheck:
                markcount += 1
            elif gameboard[i][j] == '_':
                _count += 1
                last_ = j

        if markcount == 2 and _count == 1:
            print(f"{marktocheck} wins in row {i + 1}, column {last_ + 1}")
            gameboard[i][last_] = marktoplace
            return True

    for j in range(3):
        markcount = 0
        _count = 0
        last_ = 0

        for i in range(3):
            if gameboard[i][j] == marktocheck:
                markcount += 1
            elif gameboard[i][j] == '_':
                _count += 1
                last_ = i

        if markcount == 2 and _count == 1:
            print(f"{marktocheck} wins in column {j + 1}, row {last_ + 1}")
            gameboard[j][last_] = marktoplace
            return True

    markcount = 0
    _count = 0
    last_i = 0

    for i in range(3):
        if gameboard[i][i] == marktocheck:
            markcount += 1
        elif gameboard[i][i] == '_':
            _count += 1
            last_i = i

    if markcount == 2 and _count == 1:
        print(f"{marktocheck} wins in the main diagonal, row {last_i + 1}, column {last_i + 1}")
        gameboard[last_i][last_i] = marktoplace
        return True

    markcount = 0
    _count = 0
    last_i = 0

    for i in range(3):
        if gameboard[i][2 - i] == marktocheck:
            markcount += 1
        elif gameboard[i][2 - i] == '_':
            _count += 1
            last_i = i

    if markcount == 2 and _count == 1:
        print(f"{marktocheck} wins in the anti diagonal, row {last_i + 1}, column {3 - last_i}")
        gameboard[last_i][2 - last_i] = marktoplace
        return True

    return False
