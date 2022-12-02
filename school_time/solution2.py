a = int(input())
s = sorted(set(list(input().lower())))

check = list("abcdefghijklmnopqrstuvwxyz")
if check == s:
    print("YES")
else:
    print("NO")
