import math

# https://adventofcode.com/2022/day/12
def parseInput(fName="input.in"):
    rdata: list[str] = open(fName, "r").read().splitlines()
    data: list[list[str]] = [list(i) for i in rdata]

    start, end = [-1, -1], [-1,-1]
    # Find start and end, and convert to height map
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "S":
                start = [x,y]
                data[y][x] = 0
            elif data[y][x] == "E":
                end = [x, y]
                data[y][x] = ord('z') - ord('a')
            else:
                data[y][x] = ord(data[y][x]) - ord('a')

    return start, end, data

def solve():
    start, end, grid = parseInput("input.in")
    dp: list[list[int]] = [[None for i in j] for j in grid]
    dp[end[1]][end[0]] = 0
    # print(start)
    # print(end)
    # # [print(i) for i in grid]
    # # [print(i) for i in dp]
    print("Need to learn graph theory :(")


def calculateSmallestStep(dp, x, y, ex, ey, grid):
    if dp[x][y]: return dp[x][y]

    if x == ex and y == ey:
        return 0 

    dist = math.sqrt( math.pow(ex-x, 2) + math.pow(ey-y, 2) )
    if dist <= 1 and ((x == ex) ^ (y == ey)):
        if (grid[ey][ex] - grid[y][x]) <= 1:
            dp[x][y] = 1
            return dp[x][y]
    else:
        dx = ex-x
        dy = ey-y
        check_x, check_y = None, None
        if dx > 0: check_x = x + 1
        elif dx < 0: check_y = x - 1
        if dy > 0: check_y = y + 1
        elif dy < 0: check_y = y - 1

        dp_x = calculateSmallestStep(dp, check_x, y, ex, ey, grid) if check_x else (len(grid)*len(grid[0])*2)
        dp_y = calculateSmallestStep(dp, x, check_y, ex, ey, grid) if check_y else (len(grid)*len(grid[0])*2)

        dp[x][y] = min(dp_x, dp_y) + 1
        return dp[x][y]
        
def isOneStep(x, y, ex, ey, grid):
    dist = math.sqrt( math.pow(ex-x, 2) + math.pow(ey-y, 2) )
    if dist <= 1 and ((x == ex) ^ (y == ey)):
        return (grid[ey][ex] - grid[y][x]) <= 1
    return False

def part1():
    pass 

def part2():
    pass

if __name__ == "__main__":
    solve()