n = int(input())
final = ''
branches = []
position = 'L'
for i in range(n):
    l, r = (int(i) for i in input().split())
    branches.append([l, r])
branches = branches[::-1]
for i in range(n):
    if branches[i][0] < branches[i][1]:
        if position == 'L':
            final += 'S'
        else:
            position = 'L'
            final += 'LS'
    elif branches[i][0] > branches[i][1]:
        if position == 'L':
            position = 'R'
            final += 'RS'
        else:
            final += 'S'
    else:
        final += 'S'

print(final)