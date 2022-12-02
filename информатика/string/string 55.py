'''s = input()
for el in s:
    if not el.isalpha() and el != ' ':
        s = s.replace(el, '')
print(max(s.split(), key=len))
'''

s = input()
new_s = ''
p = 0
maxx = ''
for el in s:
    if el in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю' or el == ' ':
        new_s += el
a = []
s = new_s
for i in range(len(s)):
    if i != len(s) - 1:
        if s[i] != ' ' and s[i + 1] == ' ':
            a.append(s[p:i + 1])
        if s[i] == ' ' and s[i + 1] != ' ':
            p = i + 1
    else:
        a.append(s[s.rfind(' ') + 1:])
for el in a:
    if len(el) > len(maxx):
        maxx = el
print(maxx)