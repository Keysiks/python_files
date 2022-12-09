for i in range(10 ** 9):
    for j in range(10 ** 9):
        if sum([i, j]) % 3 == 0:
            print(i, j)