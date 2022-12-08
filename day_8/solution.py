from typing import List, TypeVar

T_GRID = TypeVar("T_GRID", List[List[int]])

def parseInput(fName="input.in"):
    rdata: List[str] = open(fName, "r").read().splitlines()
    grid: T_GRID = [list(map(int, i)) for i in rdata]
    return grid

def solve():
    grid: T_GRID = parseInput("sample.in")
    part1(grid)
    part2(grid)

def transpose(matrix: T_GRID) -> T_GRID:
    return [list(i) for i in [*zip(*matrix)]]

def getPrefix(grid: T_GRID, inverse=False): # Using a variant of prefix sum algorithm
    prefix: T_GRID = []
    for r in range(len(grid)):
        tmp = []
        for c in range(len(grid)):
            if c == 0: tmp.append(grid[r][c])
            else:   tmp.append(max(grid[r][c], tmp[c-1]) if not inverse else min(grid[r][c], tmp[c-1]))
        prefix.append(tmp)
    return prefix

def printG(g):
    [print(i) for i in g]

def part1(grid: T_GRID):
    visible = len(grid) * 2 + len(grid) * 2 - 4
    prefixLeft = getPrefix(grid)
    prefixRight = [r[::-1] for r in getPrefix([r[::-1] for r in grid])]
    grid_T = transpose(grid)
    prefixUp = transpose(getPrefix(grid_T))
    prefixDown = transpose([r[::-1] for r in getPrefix([r[::-1] for r in grid_T])])

    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[r])-1):
            if grid[r][c] > prefixLeft[r][c-1] or grid[r][c] > prefixRight[r][c+1] or grid[r][c] > prefixUp[r-1][c] or grid[r][c] > prefixDown[r+1][c]:
                visible += 1
    
    print(visible)

# Creates a scenic grid from a given direction
def getScenicGrid(grid: T_GRID):
    nwGrd = []
    for r in range(len(grid)):
        tmp = []
        highest = -99
        highestDist = -1
        for c in range(len(grid)):
            highestDist += 1
            if grid[r][c] > highest:
                #highestDist = grid[r].index(highest)
                highest = grid[r][c]
                tmp.append(highestDist)
                highestDist = 0
            elif grid[r][c] <= grid[r][c-1]:
                highestDist = 1
                tmp.append(highestDist)
            else:
                tmp.append(highestDist)

        nwGrd.append(tmp)
    return nwGrd

def part2(grid):
    scenicLeft = getScenicGrid(grid)
    scenicRight = [r[::-1] for r in getScenicGrid([r[::-1] for r in grid])]
    grid_T = transpose(grid)
    scenicUp = transpose(getScenicGrid(grid_T))
    scenicDown = transpose([r[::-1] for r in getScenicGrid([r[::-1] for r in grid_T])])

    printG(grid)
    print()
    printG(scenicLeft)



if __name__ == "__main__":
    solve()

