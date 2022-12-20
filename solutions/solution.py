n = int(input())
arr = list(map(int, input().split()))
if len(set(arr)) == 1:
    print(1)
    exit()


def min_value(num):
    res = ""
    lst = list(num)
    for i in range(len(num)):
        res += min(lst)
        lst.remove(res[i])
    return int(res)


arr1 = []
f = True
maxx = 0
counter = 0
for i in range(n):
    arr1.append(min_value(str(arr[i])))
for i in range(1, n):
    if arr1[i] > arr1[i - 1]:
        counter += 1
        if maxx < counter:
            maxx = counter
    else:
        counter = 0
print(maxx + 1)