def check():

    r1 = ['_', '_', 'O']

    for i in range(3):
        if r1[i] == "X":
            return False
        if r1[i] == "_":
            return True

print(check())
