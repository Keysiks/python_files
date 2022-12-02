n = int(input())
lst = [[0]]
for i in range(1, n):
    h = [0]
    h += lst[i - 1]
    sp = list(map(lambda x: abs(x - 1), lst[i - 1]))
    h = sp[::-1] + h
    lst.append(h)
print("".join(map(str, lst[-1])))