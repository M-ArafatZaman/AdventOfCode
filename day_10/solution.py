
def parseInput(fName="input.in"):
    rdata  = open(fName, "r").read().splitlines()
    return [i.split(" ") for i in rdata]

def solve():
    data = parseInput("input.in")
    part2(data)

def part2(data):
    x = 1
    cycles = 0
    WIDTH, HEIGHT = 40, 6
    crt = [['-' for c in range(WIDTH)] for r in range(HEIGHT)] 
    currRow = 0
    i = 0 
    inAddExcecution = False
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

        # Draw Pixel
        pos_x = cycles % 40
        pos_y = cycles // 40
        pixel = "."
        if pos_x >= (x-1) and pos_x <= (x+1): pixel = "#"
        try:
            crt[pos_y][pos_x] = pixel  
        except:
            pass

        if (cycles > 0 and cycles % 40 == 0):
            currRow += 1
        
        i+= 1

    [print(''.join(i)) for i in crt]
    

def part1(data):
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
            print(cycles, x)
            signals.append(cycles * x)

        i += 1

    print(sum(signals))


if __name__ == "__main__":
    solve()