
def getData(fName):
    with open(fName, "r") as dataFile:
        data = [ i.strip() for i in dataFile.readlines() ]

    return data

def part1():
    data = getData("TD.in")

def part2():
    data = getData("TD.in")


if __name__ == "__main__":
    part1()
    part2()