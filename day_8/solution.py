from typing import List, TypeVar

T_GRID = TypeVar("T_GRID", bound=List[List[int]])

def parseInput(fName="input.in"):
    rdata: List[str] = open(fName, "r").read().splitlines()
    grid: T_GRID = [list(map(int, i)) for i in rdata]
    return grid

def solve():
    grid: T_GRID = parseInput("input.in")
    #part1(grid)
    print("PART 2 => ", part2(grid))

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
    
    return visible

# Creates a scenic grid from a given direction
def getScenicGrid(grid: T_GRID):
    nwGrd: T_GRID = []
    for r in range(len(grid)):
        tmp = []
        for c in range(len(grid[r])):
            i = c
            visibility = 1
            while i > 0 and grid[r][c] > grid[r][i-1]:
                visibility += 1
                i -= 1
                if i == 0: visibility -= 1
            tmp.append(visibility if c != 0 else 0)
        nwGrd.append(tmp)
    return nwGrd

def part2(grid: T_GRID):
    scenicLeft = getScenicGrid(grid)
    scenicRight = [r[::-1] for r in getScenicGrid([r[::-1] for r in grid])]
    grid_T = transpose(grid)
    scenicUp = transpose(getScenicGrid(grid_T))
    scenicDown = transpose([r[::-1] for r in getScenicGrid([r[::-1] for r in grid_T])])

    scenicScore: T_GRID = []
    for r in range(len(grid)):
        row = []
        for c in range(len(grid[r])):
            row.append(scenicLeft[r][c] * scenicRight[r][c] * scenicUp[r][c] * scenicDown[r][c])
        scenicScore.append(row)
    return max([max(r) for r in scenicScore])
            

if __name__ == "__main__":
    solve()

