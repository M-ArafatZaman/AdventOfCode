from collections import defaultdict

def parseInput(fName="input.in") -> list[tuple[str, int]]:
    rdata: list[str] = open(fName, "r").read().splitlines()
    data: list[list[str]] = [i.split(" ") for i in rdata]
    return [(i[0], int(i[1])) for i in data]

def solve():
    data = parseInput("input.in")
    #data = parseInput("input.in")

    paths = defaultdict(int)
    # Starting points
    H_x, H_y, T_x, T_y = 0,0,0,0
    paths[f'{T_x},{T_y}'] = 1
    for move in data:
        H_x, H_y, T_x, T_y = traceMove(paths, move[0], move[1], H_x, H_y, T_x, T_y)
    
    print(len(paths.items()))
    

def isInVicinity(H_x, H_y, T_x, T_y):
    return (abs(H_x - T_x) <= 1 and abs(H_y - T_y) <= 1)

def traceMove(paths, direction, steps, H_x, H_y, T_x, T_y):
    sign = 1
    if direction == "L" or direction == "D": sign = -1

    if direction == "U" or direction == "D": H_y += sign * steps
    if direction == "R" or direction == "L": H_x += sign * steps
    
    # Start tracing
    while not isInVicinity(H_x, H_y, T_x, T_y):
        # Move x direction
        if abs(H_x-T_x) >= 1:
            T_x += 1 if (H_x-T_x) >= 1 else -1

        # Move y direction
        if abs(H_y-T_y) >= 1:
            T_y += 1 if (H_y-T_y) >= 1 else -1

        paths[f"{T_x},{T_y}"] += 1


    return H_x, H_y, T_x, T_y





if __name__ == "__main__":
    solve()
