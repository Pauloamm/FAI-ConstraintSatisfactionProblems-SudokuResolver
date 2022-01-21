import numpy as np

gridSize = 9
squareSize = 3
test1 =[ [3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

test2 =[ [0, 0, 4, 0, 0, 0, 0, 6, 7],
         [3, 0, 0, 4, 7, 0, 0, 0, 5],
         [1, 5, 0, 8, 2, 0, 0, 0, 3],
         [0, 0, 6, 0, 0, 0, 0, 3, 1],
         [8, 0, 2, 1, 0, 5, 6, 0, 4],
         [4, 1, 0, 0, 0, 0, 9, 0, 0],
         [7, 0, 0, 0, 8, 0, 0, 4, 6],
         [6, 0, 0, 0, 1, 2, 0, 0, 0],
         [9, 3, 0, 0, 0, 0, 7, 1, 0]];

hardSudoku =[ [0, 0, 2, 0, 5, 1, 0, 0, 9],
         [0, 0, 0, 0, 0, 8, 0, 0, 0],
         [6, 0, 0, 0, 0, 0, 2, 0, 0],
         [0, 0, 0, 6, 0, 0, 0, 0, 3],
         [7, 0, 0, 0, 3, 5, 0, 1, 0],
         [0, 0, 5, 8, 0, 0, 0, 0, 0],
         [0, 4, 0, 0, 0, 0, 0, 7, 0],
         [0, 0, 0, 3, 0, 0, 0, 0, 0],
         [0, 0, 6, 0, 9, 2, 0, 0, 1]];

numberDomain = [1,2,3,4,5,6,7,8,9]


def CheckSquareForNumber(xCoord,yCoord,numberToCheck,grid):

    currentSquareToCheckX = int(xCoord/squareSize)
    currentSquareToCheckY = int(yCoord/squareSize)

    squareXLowerLimit = currentSquareToCheckX*squareSize
    squareXUpperLimit = currentSquareToCheckX*squareSize + squareSize

    squareYLowerLimit = currentSquareToCheckY * squareSize
    squareYUpperLimit = currentSquareToCheckY * squareSize + squareSize


    for xInSquare in range(squareXLowerLimit,squareXUpperLimit):
        for yInSquare in range(squareYLowerLimit,squareYUpperLimit):
            if grid[yInSquare][xInSquare] == numberToCheck: return False
    return True

def CheckColumn(xCoord,numberToCheck,grid):
    for row in grid:
        if row[xCoord] == numberToCheck: return False
    return True

def CheckRow(yCoord,numberToCheck,grid):

        for columnValueInLine in grid[yCoord]:
            if columnValueInLine == numberToCheck: return False
        return True

def CanPlaceNumber(xCoord,yCoord,numberToCheck,grid):
    return CheckSquareForNumber(xCoord,yCoord,numberToCheck,grid) and\
                        CheckColumn(xCoord,numberToCheck,grid) and\
                        CheckRow(yCoord,numberToCheck,grid)

def SolveSudoku(grid):

    for y in range(0,gridSize):
        for x in range(0,gridSize):

            if grid[y][x] == 0:

                listOfPossibilities = []
                for possibility in numberDomain:
                    if(CanPlaceNumber(x,y,possibility,grid)):
                        listOfPossibilities.append(possibility)

                for possibleNumber in listOfPossibilities:

                    grid[y][x] = possibleNumber
                    if SolveSudoku(grid): return True


                #Dead end with no possible numbers
                grid[y][x] = 0
                return False
    return True #No more zeros means its completed

if __name__ == '__main__':
    SolveSudoku(hardSudoku)
    print(np.matrix(hardSudoku))




