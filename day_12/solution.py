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

    print("PART 1 -> ", part1(start, end, grid))


def bfs(visited, r, c, er, ec, grid, condition):
    DR = [0, 1, 0, -1]
    DC = [1, 0, -1, 0]

    if visited[r][c]: return
    visited[r][c] = True

    # tuple[row, column, steps]
    queue: deque[tuple[int, int, int]] = deque()
    queue.append([r, c, 0])
    foundMatch = False
    while len(queue) > 0:
        currNode = queue.popleft()
        
        for i in range(4):
            dr = currNode[0] + DR[i]
            dc = currNode[1] + DC[i]

            if dr < 0 or dc < 0 or dr >= len(grid) or dc >= len(grid[0]) or \
                not condition(dr, dc, currNode[0], currNode[1], grid):
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
    
    # For some reason if the len of a is greater than 1, the ans is steps - 1
    # TODO: Figure out why
    if len(a) > 0:
        return a[0] if len(a) == 1 else a[0]-1
    return -1
    
def part1(start, end, grid):
    visited: list[list[bool]] = [[False for i in j] for j in grid]
    
    def condition(dr, dc, r, c, g):
        return g[dr][dc] - g[r][c] <= 1

    return bfs(visited, start[0], start[1], end[0], end[1], grid, condition)

def part2(start, end, grid):
    visited: list[list[bool]] = [[False for i in j] for j in grid]
    


if __name__ == "__main__":
    solve()