import sys
import matplotlib.pyplot as plt
from collections import deque

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

    generateNonBeaconPositions(sensors, beacons, 2000000)

# Calculate the manhattan distance between two numbers
def manhattanDistance(a: complex, b: complex) -> int:
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))

# BFS expand
def bfs_expand(nonPos: set[complex], starting_pos: complex, dist: int):
    DI = [0,1,0,-1]
    DJ = [1,0,-1,0]
    nonPos.add(starting_pos)

    visited: set[complex] = set()

    queue: deque[complex] = deque()
    queue.append(starting_pos)
    while len(queue) > 0:
        currPos: complex = queue.popleft()
        visited.add(currPos)
        
        for i in range(4):
            nextPos = (currPos.real + DI[i]) + ((currPos.imag + DJ[i]) * 1j)
            
            if nextPos not in visited and manhattanDistance(nextPos, starting_pos) <= dist:
                queue.append(nextPos)
                visited.add(nextPos)
                nonPos.add(nextPos)
        

# Generate the non beacon positions at Y = POS
def generateNonBeaconPositions(sensors: list[tuple[int, int]], beacons: list[tuple[int, int]], Y: int):
    nonPos: set[complex] = set()

    # Iterate through each sensors and calculate the manhattan distance
    for i in range(len(sensors)):
        sen, bea = [i[0]+i[1]*1j for i in  (sensors[i], beacons[i])]
        dist = manhattanDistance(sen, bea)

        # If the sensor range crosses the target Y-axis
        # Use BFS to expand the NON pos positions with the sensor pos X at Y-axis as the starting point
        if abs(Y - sen.imag) <= dist:
            yRadius = int(dist - abs(Y - sen.imag))
            for x in range(int(sen.real - yRadius), int(sen.real + yRadius) + 1):
                if (x + Y*1j) not in nonPos:
                    nonPos.add( x + Y*1j ) 
    
    # Remove all beacon and sensor positions
    for i in range(len(sensors)):
        sen, bea = [i[0]+i[1]*1j for i in  (sensors[i], beacons[i])]

        if sen in nonPos:
            nonPos.remove(sen)
        if bea in nonPos:
            nonPos.remove(bea)

    x = [i.real for i in nonPos]
    y = [i.imag for i in nonPos]

    print(len(nonPos))


def part2():
    return

if __name__ == "__main__":
    solve() 