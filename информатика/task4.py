switched = []
n, c, p = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    switched.append((x, y))
x_net, y_net = map(int, input().split())
road = 0
s_x, s_y = x_net, y_net
for i in range(n):
    minn = 1000000
    index = 0
    for j in range(len(switched)):
        a = (abs(s_x - switched[j][0]) ** 2 + abs(s_y - switched[j][1]) ** 2) ** 0.5
        if a < minn and a != 0:
            index = j
            minn = a
    road += minn
    s_x, s_y = switched[index][0], switched[index][1]
if c * road <= p:
    print("YES", round(c * road, 2))
else:
    print("NO", round(c * road, 2))
