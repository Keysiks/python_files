# print('.'.join(input().split()))

s = input()
total = ''
flag = False
for i in s:
    if i == ' ':
        if flag is False:
            total += '.'
            flag = True
    else:
        total += i
        flag = False
print(total)