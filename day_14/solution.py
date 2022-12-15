
def parseInput(fName="input.in"):
    rdata = open(fName, "r").read().splitlines()

    grid: list[list[str]] = [["+"]]
    # "+" is 500, 0

    # Construct grid dynamically
    for path in rdata:
        coords = [tuple(map(int ,i.strip().split(","))) for i in path.split("->")]
        
        for x, y in coords:
            SOURCE_X = 500
            SOURCE_X_INDEX = grid[0].index("+")

            # Adjust Rows
            if (y > len(grid)):
                for _ in range(y - len(grid) + 1):
                    grid.append([" " for c in range(len(grid[0]))])

            # Adjust columns
            mappedXIndexToGrid = (SOURCE_X_INDEX + (x - SOURCE_X))
            if (x < SOURCE_X and mappedXIndexToGrid < 0):
                # Prepend for all rows
                for row in grid:
                    for _ in range(SOURCE_X - x):
                        row.insert(0, " ")
                
            elif (x > SOURCE_X and mappedXIndexToGrid >= len(grid[0])):
                # Append for all rows
                for row in grid:
                    for _ in range(x - SOURCE_X):
                        row.append(" ")

    # Draw path
    for path in rdata:
        coords = [tuple(map(int ,i.strip().split(","))) for i in path.split("->")]

        SOURCE_X = 500
        SOURCE_X_INDEX = grid[0].index("+") 
        MAP_X_TO_INDEX = lambda c: (SOURCE_X_INDEX + (c - SOURCE_X))

        for i in range(1, len(coords)):
            x1, y1 = coords[i-1]
            x2, y2 = coords[i]
            x1 = MAP_X_TO_INDEX(x1)
            x2 = MAP_X_TO_INDEX(x2)

            if x1 == x2:
                # Vertical Line
                for row in range(min(y1, y2), max(y1, y2)+1):
                    grid[row][x1] = "#"

            elif y1 == y2:
                # Horizontal Line
                for col in range(min(x1, x2), max(x1, x2)+1):
                    try:
                        grid[y1][col] = "#"
                    except:
                        pass

    return rdata

def solve():
    data = parseInput("sample.in")
    

def part1():
    pass 

def part2():
    pass

if __name__ == "__main__":
    solve()
