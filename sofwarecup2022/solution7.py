password = list(input())
h = 0
final = ''
for i in range(len(password)):
    h += ord(password[i]) - ord('a') + 1

if list(set(password)) == ['a'] or list(set(password)) == ['z'] or len(password) == 1:
    print(h)
    exit()
if len(list(set(password))) == 1:
    password[0] = chr(ord(password[0]) + 1)
    password[-1] = chr(ord(password[-1]) - 1)
    print(h)
    print(''.join(password))
    exit()

if password[0] == password[1]:
    password[0], password[-1] = password[-1], password[0]
    print(h)
    print(''.join(password))
    exit()
for i in range(1, len(password), 2):
    password[i], password[i - 1] = password[i - 1], password[i]
print(h)
print(''.join(password))
