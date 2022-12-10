
def parseInput(fName="input.in"):
    rdata = open(fName, "r").read().splitlines()

    return rdata

def solve():
    data = parseInput("sample.in")


if __name__ == "__main__":
    solve()