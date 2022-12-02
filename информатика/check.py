maxx = 0
for i in range(10**10):
    f = True
    for j in range(1, len(str(i))):
        if int(str(i)[j - 1]) * int(str(i)[j]) < 5:
             f = False
    if sum(list(map(int, list(str(i))))) == 20 and f:
        maxx = i
print(maxx)