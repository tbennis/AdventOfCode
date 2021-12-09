import numpy as np

def findMaxCoor(coorList):
    maxX = 0
    maxY = 0
    for coorPair in coorList:
        for coor in coorPair:
            coor = coor.split(',')
            if int(coor[0]) > maxX:
                maxX = int(coor[0])
            if int(coor[1]) > maxY: 
                maxY = int(coor[1])
    return [maxX, maxY]

def updateGrid(grid, coorPair):
    coors = [coorPair[0].split(','), coorPair[1].split(',')]
    if coors[0][0] == coors[1][0]:
        end = max([int(coors[0][1]), int(coors[1][1])])
        start = min([int(coors[0][1]), int(coors[1][1])])
        for i in range(start, end+1):
            grid[int(i, coors[0][0])] += 1
    else:
        end = max([int(coors[0][0]), int(coors[1][0])])
        start = min([int(coors[0][0]), int(coors[1][0])])
        for i in range(start, end+1):
            grid[int(coors[0][1]), i] += 1
    return grid

with open('TestInput5.txt') as f:
    input = f.read()
inputList = input.splitlines()
coorList = [[coor.split(' -> ')[0], coor.split(' -> ')[1]] for coor in inputList]
coorList = coorList[0:2]
grid = np.zeros((findMaxCoor(coorList)[1]+1, findMaxCoor(coorList)[0]+1))
for coorPair in coorList:
    grid = updateGrid(grid, coorPair)
print(grid)
grid[grid <= 1] = 0
grid[grid >= 2] = 1
