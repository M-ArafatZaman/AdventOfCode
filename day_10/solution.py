
def parseInput(fName="input.in"):
    rdata  = open(fName, "r").read().splitlines()
    return [i.split(" ") for i in rdata]

"""
Use a 2nd order decorator as a base for the execution cycle 
"""
def executionCycle(dataset: list[list[str]]):
    # func is executed after every cycle
    def loader(func):
        def wrapper(*args, **kwargs):
            x = 1
            cycles = 0
            inAddExecution = False
            i = 0
            while i < len(dataset):
                cycles += 1
                if inAddExecution:
                    i -= 1
                    x += int(dataset[i][1])
                    inAddExecution = False
                elif dataset[i][0] == "addx":
                    inAddExecution = True

                # X register is the first parameter, the current cycle is the second parameter
                func(x, cycles, *args, **kwargs)
                i += 1

        return wrapper
    return loader

def solve():
    data = parseInput("input.in")
    
    ## ========= Part 1 =========
    signals = []
    @executionCycle(data)
    def part1(x, cycles):
        if (cycles == 20) or (cycles > 20 and (cycles + 20) % 40 == 0):
            signals.append(cycles * x)
    part1()
    print("PART 1 ->", sum(signals))

    ## ========= Part 2 ==========
    WIDTH, HEIGHT = 40, 6
    crt = [["-" for c in range(WIDTH)] for r in range(HEIGHT)]
    @executionCycle(data)
    def part2(x, cycles):
        # Draw Pixel
        pos_x = cycles % 40
        pos_y = cycles // 40
        pixel = " "
        if pos_x >= (x-1) and pos_x <= (x+1): pixel = "\u2588"
        try:
            crt[pos_y][pos_x] = pixel  
        except:
            pass 
    part2()
    print("PART 2 ->")
    [print("".join(r)) for r in crt]

if __name__ == "__main__":
    solve()