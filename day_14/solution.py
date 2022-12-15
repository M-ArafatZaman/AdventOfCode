import copy

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
                    grid[y1][col] = "#"
                    
    return grid

def solve():
    grid: list[list[str]] = parseInput("input.in")
    
    print("PART 1 ->", simulateSands(copy.deepcopy(grid)))
    print("PART 2 ->", part2(copy.deepcopy(grid)))

def simulateSands(grid: list[list[str]]):
    sands = 0
    SOURCE_INDEX = grid[0].index("+")
    
    while True:
        if grid[1][SOURCE_INDEX] == "o" and grid[1][SOURCE_INDEX-1] == "o" and grid[1][SOURCE_INDEX+1] == "o":
            sands += 1
            break

        # (row, col)
        sand_coord = [0, SOURCE_INDEX]

        infiniteLoop = False
        
        while True:
            sand_row = sand_coord[0]
            sand_col = sand_coord[1]
            moved = False
            # Check if we can move downward
            if (sand_row+1 < len(grid)):
                # Move downward
                if  grid[sand_row+1][sand_col] == " ":
                    grid[sand_row][sand_col] = " "
                    grid[sand_row+1][sand_col] = "o"
                    sand_coord = [sand_row+1, sand_col]
                    moved = True
                # Move left downward
                elif sand_col - 1 >= 0 and grid[sand_row+1][sand_col-1] == " ":
                    grid[sand_row][sand_col] = " "
                    grid[sand_row+1][sand_col-1] = "o"
                    sand_coord = [sand_row+1, sand_col-1]
                    moved = True
                # Move right downward
                elif sand_col + 1 < len(grid[0]) and grid[sand_row+1][sand_col+1] == " ":
                    grid[sand_row][sand_col] = " "
                    grid[sand_row+1][sand_col+1] = "o"
                    sand_coord = [sand_row+1, sand_col+1]
                    moved = True
            
            # Check if it WILL be an infinite loop
            if sand_row == len(grid)-1 or \
               (sand_col == 0 and (grid[sand_row+1][sand_col] != " " or grid[sand_row+1][sand_col+1] != " ")) or \
               (sand_col == len(grid[0])-1 and (grid[sand_row+1][sand_col] != " " or grid[sand_row+1][sand_col-1] != " ")):
                infiniteLoop = True
                break
            
            if not moved: break

        # Check if sands are in an infiniteloop, simulation is done
        if infiniteLoop: break
        sands += 1

    return sands

def part2(grid: list[list[str]]):
    # Add 2 rows
    grid.append([' ' for c in grid[0]])
    grid.append(['#' for c in grid[0]])

    # Adjust cols
    SOURCE_INDEX = grid[0].index("+")
    REQUIRED_RADIUS = len(grid)-1
    # Prepend
    if SOURCE_INDEX - REQUIRED_RADIUS < 0:
        for row in grid:
            for _ in range(REQUIRED_RADIUS - SOURCE_INDEX + 2):
                row.insert(0, " ")
    # Append with new source position after prepend
    SOURCE_INDEX = grid[0].index("+")
    END_INDEX = len(grid[0])
    if SOURCE_INDEX + REQUIRED_RADIUS > END_INDEX:
        for row in grid:
            for _ in range((SOURCE_INDEX + REQUIRED_RADIUS) - END_INDEX + 2):
                row.append(" ")
    
    # Draw floor
    grid[len(grid)-1] = ["#" for _ in grid[0]]

    return simulateSands(grid)

if __name__ == "__main__":
    solve()
