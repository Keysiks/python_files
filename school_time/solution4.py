n, m = map(int, input().split())
names = list(map(int, input().split()))
count = 0
last = 0
for i in range(n):
    count += names[i]
    print(count // m - last, end=" ")
    last += count // m - last
