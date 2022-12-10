
def parseInput(fName="input.in"):
    rdata  = open(fName, "r").read().splitlines()
    return [i.split(" ") for i in rdata]

def solve():
    data = parseInput("input.in")
    x = 1
    cycles = 0
    signals = []
    inAddExcecution = False
    i = 0
    while i < len(data):
        if inAddExcecution:
            cycles += 1
            i -= 1
            x += int(data[i][1])
            inAddExcecution = False
        elif data[i][0] == "addx":
            inAddExcecution = True
            cycles += 1
        elif data[i][0] == "noop":
            cycles += 1

        if cycles == 20 or (cycles > 20 and (cycles + 20) % 40 == 0):
            #signals += cycles * x
            print(cycles, x)
            signals.append(cycles * x)

        i += 1

    print(sum(signals))
    



if __name__ == "__main__":
    solve()