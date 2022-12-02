# числа фибонначи
n = int(input())
dp = [-1] * (n + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])

# лесенка
n = int(input())
st = [int(i) for i in input().split()]
dp = [0] * n
dp[0], dp[1] = st[0], max(st[1] + st[0], st[1])
for i in range(2, len(st)):
    dp[i] = max(dp[i - 1], dp[i - 2]) + st[i]
print(dp[-1])

# мячик на лесенка
n = int(input())
if n in (1, 2):
    print(n)
    exit()
stairs = [0] * (n + 1)
stairs[0], stairs[1], stairs[2] = 1, 1, 2
for i in range(3, n + 1):
    stairs[i] = stairs[i - 1] + stairs[i - 2] + stairs[i - 3]

print(stairs[-1])

"""калькулятор"""

n = int(input())
lst = [0] * (n + 1)
for i in range(2, n + 1):
    m = lst[i - 1]
    if i % 3 == 0:
        m = min(m, lst[i // 3])
    if i % 2 == 0:
        m = min(m, lst[i // 2])
    lst[i] = m + 1
print(lst[n])

"""без трех единиц"""
n = int(input())
f = [0] * 40
f[1] = 2
f[2] = 4
f[3] = 7

i = 4
while i <= n:
    f[i] = (f[i - 1] + f[i - 2] + f[i - 3])
    i += 1

print(f[n])

"""гвоздики"""

def maxx(i):
    if i > n - 3:
        return 0
    if m[i] == 0:
        m[i] = lst[i + 1] - lst[i] + max(maxx(i + 2), maxx(i + 3))
    return m[i]


n = int(input())
lst = sorted(list(map(int, input().split())))
m = [0 for i in range(n)]
print(lst[-1] - lst[0] - max(maxx(1), maxx(2)))
