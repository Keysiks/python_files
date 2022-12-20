import math
n = int(input())


def find_num(k):
    if k == 1:
        return 1
    n = 2 * (k + 3) ** 0.5
    return n


print(find_num(1))
amount = 0
for i in range(n):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        amount += find_num(j)
    print(amount % 1000000007)
    amount = 0
