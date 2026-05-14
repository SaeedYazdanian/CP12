#read the matrix        5 minutes
#check every row        7 minutes
#check every column     10 minutes
#check every 3x3 box    15 minutes

#first code to read a 9x9 matrix
grid = []
for i in range(9):
    row = [int(x) for x in input().split()]
    grid.append(row)
print(grid)
#checking every row
good = True
for r in range(9):
    if len(set(grid[r])) < 9:
        good = False
#code to check if column 0 is all unique
temp = []
for r in range(9):
    temp.append(grid[r][0])
if len(set(temp)) < 9:
    good = False

#repeat the code above for every column








