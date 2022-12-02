# print(*sorted(input().split()))


s = input()
a = []
p = 0
for i in range(len(s)):
    if i != len(s) - 1:
        if s[i] != ' ' and s[i + 1] == ' ':
            a.append(s[p:i + 1])
        if s[i] == ' ' and s[i + 1] != ' ':
            p = i + 1
    else:
        a.append(s[s.rfind(' ') + 1:])
n = len(a)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(*a)
