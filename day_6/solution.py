
def parseInput(fName="input.in"):
    """
    Function to parse input files
    """
    with open(fName, "r") as dataFile:
        data = dataFile.read().splitlines()

    return data[0]

def stringIsUnique(string):
    return len(set(list(string))) == len(string)

def part1():
    stream = parseInput("input.in")
    buffer = ""
    for i in range(len(stream)):
        buffer += stream[i]
        
        # Check
        if len(buffer) == 4 and stringIsUnique(buffer):
            print(i+1)
            break 
        
        while len(buffer) >= 4:
            buffer = buffer[1:]

def main():
    part1()


if __name__ == "__main__":
    main()