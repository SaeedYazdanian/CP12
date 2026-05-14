#read the matrix        5 minutes
#check every row        7 minutes
#check every column     10 minutes
#check every 3x3 box    15 minutes

#first code to read a 9x9 matrix
grid = []
for i in range(9):
    row = [int(x) for x in input().split()]
    grid.append(row)
#second code to read a 9x9 matrix
grid = [[int(x) for x in input().split()] for i in range(9)]

print(grid[0])
print(len(set(grid[0])))