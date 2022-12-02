# print(len(sorted(input().split(), reverse=True, key=len)[-1]))

s, minn = input(), 10000
j, k = 0, 0
c = 0
for i in range(len(s)):
    if s[i] == ' ' and s[i + 1] != ' ':
        k = i + 1
        for el in s[j:k]:
            if el == ' ':
                c += 1
        if len(s[j:k]) - c < minn:
            minn = len(s[j:k]) - c
        c = 0
        j = k
print(minn)
