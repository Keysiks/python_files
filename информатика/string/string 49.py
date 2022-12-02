'''s = input()
total, flag = '', False
j, k = 0, 0
for i in range(s.rfind(' ') + 1):
    if s[i] == ' ':
        total += ' '
        if s[i + 1] != ' ':
            j = i + 1
    else:
        if s[i + 1] == ' ':
            a = s[j:i + 1]
            for i in range(len(a) - 1):
                if a[i] == a[-1]:
                    total += '.'
                else:
                    total += a[i]
            total += a[-1]
for el in s[s.rfind(' ') + 1:len(s) - 1]:
    total += '.' if el == s[-1] else el
total += s[-1]
print(total)
'''

s = input()
space = [0 for i in range(len(s.split()))]
k = 0
flag = True
for i in range(len(s) - 1):
    if s[i] == ' ':
        space[k] += 1
    if s[i + 1] != ' ' and s[i] == ' ':
        k += 1
lst = s.split()
for i in range(len(lst)):
    lst[i] = lst[i].replace(lst[i][-1], '.', lst[i].count(lst[i][-1]) - 1)
for i in range(len(lst)):
    print(lst[i] + space[i] * ' ', end='')