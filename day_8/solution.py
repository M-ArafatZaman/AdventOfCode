from typing import List

T_GRID = List[List[int]]

def parseInput(fName="input.in"):
    rdata: List[str] = open(fName, "r").read().splitlines()
    grid: T_GRID = [list(map(int, i)) for i in rdata]
    return grid

def solve():
    grid: T_GRID = parseInput("input.in")
    print("PART 1 => ", part1(grid))
    print("PART 2 => ", part2(grid))

# Matrix transformation functions
def transpose(matrix: T_GRID) -> T_GRID:
    return [list(i) for i in [*zip(*matrix)]]

def flipY(matrix: T_GRID) -> T_GRID:
    return [r[::-1] for r in matrix]

# This function calculates the maximum height of a tree from left to right
def getPrefix(grid: T_GRID) -> T_GRID:
    prefix: T_GRID = []
    for r in range(len(grid)):
        tmp = []
        for c in range(len(grid[r])):
            if c == 0: tmp.append(grid[r][c])
            else:   tmp.append(max(grid[r][c], tmp[c-1]))
        prefix.append(tmp)
    return prefix

def part1(grid: T_GRID):
    visible: T_GRID = len(grid) * 2 + len(grid) * 2 - 4
    # Use rotation and matrix properties to calculate max height from every direction
    prefixLeft: T_GRID = getPrefix(grid)
    prefixRight: T_GRID = flipY(getPrefix(flipY(grid)))
    grid_T: T_GRID = transpose(grid)
    prefixUp: T_GRID = transpose(getPrefix(grid_T))
    prefixDown: T_GRID = transpose(flipY(getPrefix(flipY(grid_T))))
    # From every direction, compare with the prev max height.
    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[r])-1):
            if grid[r][c] > prefixLeft[r][c-1] or grid[r][c] > prefixRight[r][c+1] or grid[r][c] > prefixUp[r-1][c] or grid[r][c] > prefixDown[r+1][c]:
                visible += 1
    
    return visible

# Creates a grid that shows how many trees are visible from left to right
def getScenicGrid(grid: T_GRID) -> T_GRID:
    nwGrd: T_GRID = []
    for r in range(len(grid)):
        tmp = []
        for c in range(len(grid[r])):
            i = c
            visibility = 1
            while i > 0 and grid[r][c] > grid[r][i-1]:
                visibility += 1
                i -= 1
                if i == 0: visibility -= 1 # Edge trees have no visible trees
            tmp.append(visibility if c != 0 else 0)
        nwGrd.append(tmp)
    return nwGrd

def part2(grid: T_GRID):
    # Use rotation and matrix properties to calculate scenic grid from every direction
    scenicLeft: T_GRID = getScenicGrid(grid)
    scenicRight: T_GRID = flipY(getScenicGrid(flipY(grid)))
    grid_T: T_GRID = transpose(grid)
    scenicUp: T_GRID = transpose(getScenicGrid(grid_T))
    scenicDown: T_GRID = transpose(flipY(getScenicGrid(flipY(grid_T))))
    # Calculate scenic score for every tree, and get the max
    scenicScore: T_GRID = []
    for r in range(len(grid)):
        row = []
        for c in range(len(grid[r])):
            row.append(scenicLeft[r][c] * scenicRight[r][c] * scenicUp[r][c] * scenicDown[r][c])
        scenicScore.append(row)
    return max([max(r) for r in scenicScore])
            

if __name__ == "__main__":
    solve()

