import math
from collections import deque

# https://adventofcode.com/2022/day/12
def parseInput(fName="input.in"):
    rdata: list[str] = open(fName, "r").read().splitlines()
    data: list[list[str]] = [list(i) for i in rdata]

    start, end = [-1, -1], [-1,-1]
    # Find start and end, and convert to height map
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == "S":
                start = [r,c]
                data[r][c] = 0
            elif data[r][c] == "E":
                end = [r, c]
                data[r][c] = ord('z') - ord('a') + 1
            else:
                data[r][c] = ord(data[r][c]) - ord('a')

    return start, end, data

def solve():
    start, end, grid = parseInput("sample.in")
    visited: list[list[bool]] = [[False for i in j] for j in grid]
    # print(start)
    # print(end)
    # [print(i) for i in grid]
    # [print(i) for i in dp]
    # print("Need to learn graph theory :(")
    print(bfs(visited, start[0], start[1], end[0], end[1], grid))
    


def bfs(visited, r, c, er, ec, grid):
    DR = [0, 1, 0, -1]
    DC = [1, 0, -1, 0]

    if visited[r][c]: return
    visited[r][c] = True

    # tuple[row, column, steps]
    queue: deque[tuple[int, int, int]] = deque()
    queue.append([r, c, 0])
    steps = 0
    foundMatch = False
    while len(queue) > 0:
        currNode = queue.popleft()
        
        for i in range(4):
            dr = currNode[0] + DR[i]
            dc = currNode[1] + DC[i]

            if dr < 0 or dc < 0 or dr >= len(grid) or dc >= len(grid[0]) or \
                (grid[dr][dc] - grid[currNode[0]][currNode[1]]) > 1:
                continue
            elif not visited[dr][dc]:
                visited[dr][dc] = True
                queue.append([dr, dc, currNode[2]+1 ])
                
                if dr == er and dc == ec: 
                    foundMatch = True
                    break
        
        if foundMatch: break
    a = [i[2] for i in queue]
    a.sort()
    print(a)
    return queue[0][2] if len(queue) > 0 else -1

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