
def parseInput(fName="input.in"):
    """
    Function to parse input files
    """
    with open(fName, "r") as dataFile:
        data = dataFile.read().splitlines()
    return data[0]

def isStrUnique(string):
    return len(set(string)) == len(string)

def solve(part=1):
    if part == 1: BUFFER_LEN = 4
    else: BUFFER_LEN = 14

    stream = parseInput("input.in")
    buffer = ""
    # Iterate through the buffer stream
    for i in range(len(stream)):
        buffer += stream[i]
        # Check if all chars are unique
        if len(buffer) == BUFFER_LEN and isStrUnique(buffer):
            return i+1
        # Remove prev characters that exceed the buffer limit
        if len(buffer) >= BUFFER_LEN:
            buffer = buffer[len(buffer)-BUFFER_LEN+1:]

def main():
    print("Part 1 =>", solve(1))
    print("Part 2 =>", solve(2))


if __name__ == "__main__":
    main()