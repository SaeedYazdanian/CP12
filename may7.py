import random
#another way of creating a 4 by 5 matrix filled with random numbers
mat = []
for r in range(4):
    row = []
    for c in range(5):
        row.append(random.randint(1,9))
    mat.append(row)

for r in range(len(mat)):
    print(*mat[r])
