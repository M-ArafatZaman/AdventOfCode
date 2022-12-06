
def parseInput(fName="input.in"):
    """
    Function to parse input files
    """
    with open(fName, "r") as dataFile:
        data = dataFile.read().splitlines()

    print(data)


def main():
    parseInput("sample.in")


if __name__ == "__main__":
    main()