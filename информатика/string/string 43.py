'''lst, c = input().split(), 0
for el in lst:
    if 'А' in el:
        c += 1
print(c)
'''

ph, c = input(), 0
j, k = 0, 0
for i in range(len(ph)):
    if ph[i] == ' ' and ph[i + 1] != ' ':
        k = i + 1
        if 'А' in ph[j:k]:
            c += 1
        j = k
print(c)
