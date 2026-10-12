#matrix addition
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
c = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(a[i][j]+b[i][j])
    c.append(row)
print(c)
for i in c:
    for j in i:
        print(j,end=" ")
print(c)
