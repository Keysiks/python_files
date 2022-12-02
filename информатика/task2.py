n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
str_max = []
for i in range(n):
    str_max.append(max(matrix[i]))
print(min(str_max), end=" ")
row_max = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(matrix[j][i])
    row_max.append(min(row))
print(max(row_max))

