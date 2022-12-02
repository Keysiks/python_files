'''
s = input()
for el in s:
    if el.isalpha() or el == ' ':
        s = s.replace(el, '')
print(len(s))
'''


s = input()
new_s = ''
for el in s:
    if el not in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю' and el != ' ':
        new_s += el

print(len(new_s))