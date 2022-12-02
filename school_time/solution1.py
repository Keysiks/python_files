n, h = map(int, input().split())
end_sum = 0
friends = list(map(int, input().split()))
for i in friends:
    if i <= h:
        end_sum += 1
    else:
        end_sum+= 2
print(end_sum)
