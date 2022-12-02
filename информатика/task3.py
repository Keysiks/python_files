from math import sin, acos
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
r, s1 = int(input()), int(input())


def find_area(x1, y1, x2, y2, r):
    d = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
    if d >= 2 * r:
        return 2 * 3.1415926 * r * r
    elif d == 0:
        return r * r * 3.1415926

    else:
        f1 = 2 * acos((- d * d) / (2 * r * d))
        f2 = 2 * acos((- d * d) / (2 * r * d))
        s1 = (r * (f1 - sin(f1)))
        s2 = (r * (f2 - sin(f2)))
        return s1 + s2


res = find_area(x1, y1, x2, y2, r)
strs = str(round(res, 3)).split(".")[1]
s = ""
if len(strs) < 3:
    s += "0" * (3 - len(strs))
if res > s1:
    print("YES", round(res, 3), end="")
else:
    print("NO", round(res, 3), end="")
print(s)
