x, n, y, m = (int(i) for i in input().split())
if (x + 1) * n > m * (y + 1):
    print(2)
else:
    print(1)
