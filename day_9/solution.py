from collections import defaultdict

# Type definitions
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x},{self.y})"
        
PATHS = dict[int, list[str]]
COORDS = list[Point]

def parseInput(fName="input.in") -> list[tuple[str, int]]:
    rdata: list[str] = open(fName, "r").read().splitlines()
    data: list[list[str]] = [i.split(" ") for i in rdata]
    return [(i[0], int(i[1])) for i in data]

def solve():
    data = parseInput("input.in")

    # Starting points
    paths: PATHS = defaultdict(list)
    coords: COORDS = []
    [coords.append(Point(0,0)) for _ in range(10)]
    [paths[i].append(f'{j.x},{j.y}') for i, j in enumerate(coords)]
    
    for move in data:
        currSteps = 1
        while currSteps <= move[1]:
            traceMove(move[0], 1, paths, coords)
            currSteps += 1
    
    print("Part 1 ->", len(paths[1]))
    print("Part 2 ->", len(paths[9]))

def isInVicinity(A: Point, B: Point):
    return (abs(A.x - B.x) <= 1 and abs(A.y - B.y) <= 1)

def traceMove(direction, steps, paths: PATHS, coords: COORDS):
    sign = 1
    if direction == "L" or direction == "D": sign = -1
    if direction == "U" or direction == "D": coords[0].y += sign * steps
    if direction == "R" or direction == "L": coords[0].x += sign * steps
    paths[0].append(f"{coords[0].x},{coords[0].y}")
    
    # Trace for each points after the first one
    for i in range(1, len(coords)):
        _tail = coords[i]
        _head = coords[i-1]
        while not isInVicinity(_head, _tail):
            # Move x direction
            if abs(_head.x - _tail.x) >= 1:
                _tail.x += 1 if (_head.x-_tail.x) >= 1 else -1

            # Move y direction
            if abs(_head.y - _tail.y) >= 1:
                _tail.y += 1 if (_head.y-_tail.y) >= 1 else -1

            key = f'{_tail.x},{_tail.y}'
            if key not in paths[i]:
                paths[i].append(key)

if __name__ == "__main__":
    solve()
