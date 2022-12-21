import sys

def parseInput(fName="input.in"):
    rdata = open(fName, "r").read().splitlines()
    sensors: list[tuple[int, int]] = []
    beacons: list[tuple[int, int]] = []

    for line in rdata:
        data = line.split("=")
        sx = data[1].split(",")[0]
        sy = data[2].split(":")[0]
        bx = data[3].split(",")[0]
        by = data[4].split(":")[0]

        sensors.append((int(sx), int(sy)))
        beacons.append((int(bx), int(by)))

    return sensors, beacons

def solve():
    file = "sample.in"
    if len(sys.argv) >= 2:
        file = sys.argv[1] + ".in"
    sensors, beacons = parseInput(file)

    isSample = True if file == "sample.in" else False

    print("PART 1 ->", part1(sensors, beacons, isSample))
    print("PART 2 ->", part2(sensors, beacons, isSample))

# Calculate the manhattan distance between two numbers
def manhattanDistance(a: complex, b: complex) -> int:
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))

# Generate the non beacon Intervals at Y = POS
def generateNonBeaconIntervals(sensors: list[tuple[int, int]], beacons: list[tuple[int, int]], Y: int):
    intervals: list[tuple[int, int]] = []

    # Iterate through each sensors and calculate the manhattan distance
    for i in range(len(sensors)):
        sen, bea = [i[0]+i[1]*1j for i in  (sensors[i], beacons[i])]
        dist = manhattanDistance(sen, bea)

        # If the sensor range crosses the target Y-axis
        # Append the interval at which where no beacon pos is possible
        if abs(Y - sen.imag) <= dist:
            yRadius = int(dist - abs(Y - sen.imag))
            intervals.append([sen.real-yRadius, sen.real+yRadius])

    intervals.sort()

    mergedIntervals: list[tuple[int, int]] = []
    mergedIntervals.append(intervals[0])
    
    # Merge intervals
    for i in range(1, len(intervals)):
        prev = mergedIntervals[-1]
        curr = intervals[i]

        # If the current lower bound is less than the previous upper bound, merge
        if curr[0] <= prev[1]:
            mergedIntervals[len(mergedIntervals)-1][1] = max(prev[1], curr[1])
        else:
            mergedIntervals.append(curr)

    # Return interval
    return mergedIntervals

def part1(sensors: list[tuple[int, int]], beacons: list[tuple[int, int]], sample=False):
    Y = 10 if sample else 2000000
    
    interval = generateNonBeaconIntervals(sensors, beacons, Y)
    
    pos: set[complex] = set()

    # Create positions
    for i in interval:
        for x in range(int(i[0]), int(i[1])+1):
            pos.add( x + Y*1j )
    # Remove beacons
    for i in beacons:
        if i[1] == Y and (i[0] + i[1]*1j) in pos:
            pos.remove( i[0] + i[1]*1j)

    return len(pos)

# Function to get tuning frequency
def getTuningFrequency(intervals: list[tuple[int, int]], y: int) -> int:
    # Determine GAP x
    gap_x = (intervals[1][0] + intervals[0][1])//2

    return (gap_x*4000000) + y

def part2(sensors: list[tuple[int, int]], beacons: list[tuple[int, int]], sample=False):
    LIMIT = 20 if sample else 4000000

    for y in range(LIMIT+1):
        intervals = generateNonBeaconIntervals(sensors, beacons, y)
        if len(intervals) > 1:
            return getTuningFrequency(intervals, y)

        print("Current: ", y, end="\r")

    return 0

if __name__ == "__main__":
    solve() 