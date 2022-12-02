n = int(input())
list_x1, list_y1, list_z1, list_x2, list_y2, list_z2 = [], [], [], [], [], []

for i in range(n):
    x1, y1, z1, x2, y2, z2 = (int(i) for i in input().split())
    list_x1.append(x1)
    list_x2.append(x2)
    list_y1.append(y1)
    list_y2.append(y2)
    list_z1.append(z1)
    list_z2.append(z2)


new_cords = [max(list_x1), max(list_y1), max(list_z1), min(list_x2), min(list_y2), min(list_z2)]
if new_cords[0] >= new_cords[3] or new_cords[1] >= new_cords[4] or new_cords[2] >= new_cords[5]:
    print('PROHIBITED')
else:
    print(*new_cords)




