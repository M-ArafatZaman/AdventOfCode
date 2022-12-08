
def parseInput(fName="input.in"):
    rdata = open(fName, "r").read().splitlines()
    grid = [list(map(int, i)) for i in rdata]
    return grid

def solve():
    grid = parseInput("input.in")
    part1(grid)

def transpose(matrix):
    return [list(i) for i in [*zip(*matrix)]]

def getPrefix(grid): # Using a variant of prefix sum algorithm
    prefix = []
    for r in range(len(grid)):
        tmp = []
        for c in range(len(grid)):
            if c == 0: tmp.append(grid[r][c])
            else:   tmp.append(max(grid[r][c], tmp[c-1]))
        prefix.append(tmp)
    return prefix

def printG(g):
    [print(i) for i in g]

def part1(grid):
    visible = len(grid) * 2 + len(grid) * 2 - 4
    prefixLeft = getPrefix(grid)
    prefixRight = [r[::-1] for r in getPrefix([r[::-1] for r in grid])]
    grid_T = transpose(grid)
    prefixUp = getPrefix(grid_T)
    prefixDown = [r[::-1] for r in getPrefix([r[::-1] for r in grid_T])]
    prefixUp = transpose(prefixUp)
    prefixDown = transpose(prefixDown)

    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[r])-1):
            if grid[r][c] > prefixLeft[r][c-1] or grid[r][c] > prefixRight[r][c+1] or grid[r][c] > prefixUp[r-1][c] or grid[r][c] > prefixDown[r+1][c]:
                visible += 1
    
    print(visible)



if __name__ == "__main__":
    solve()

