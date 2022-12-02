n = int(input())
packets = list(map(int, input().split()))
answer = 0
for i in range(n):
    if (sum(packets) - packets[i]) % 2 == 0:
        answer += 1
print(answer)