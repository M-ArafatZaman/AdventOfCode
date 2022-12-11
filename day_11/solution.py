import re

ARITHMETIC_OPERATION = {
    "+": lambda old, n: old + n,
    "*": lambda old, n: old * n,
}
class Monkey:
    def __init__(self, 
        number=0,
        items=[],
        operation=ARITHMETIC_OPERATION["+"],
        operationNum=0,
        divisible=1,
        monkeyIfTrue=None,
        monkeyIfFalse=None
    ):
        self.number = number
        self.items = items
        self.operation = operation
        self.operationNum = operationNum
        self.divisible = divisible
        self.monkeyIfTrue = monkeyIfTrue
        self.monkeyIfFalse = monkeyIfFalse

def parseInput(fName="input.in") -> list[Monkey]:
    rdata = open(fName, "r").read()
    listRawData = re.compile(r"Monkey [0-9]:\n").split(rdata)
    monkeys: list[Monkey] = []
    # Iterate through each monkey, and then each monkey parameters
    for data in listRawData:
        if data == "": continue
        number, items, operation, operationNum, divisible, monkeyIfTrue, monkeyIfFalse = len(monkeys), [], "+", 0, 1, None, None
        for parameters in data.splitlines():
            if parameters == "": continue
            parameters = parameters.strip()
            # Xtract each parameters
            if parameters.startswith("Starting items"):
                items = items + list(map(int, parameters.split(":")[1].strip().split(",")))
            elif parameters.startswith("Operation"):
                old, operation, operationNum = parameters.split("=")[1].strip().split(" ")
            elif parameters.startswith("Test"):
                divisible = int(parameters.split(" ")[-1])
            elif parameters.startswith("If true"):
                monkeyIfTrue = int(parameters.split(" ")[-1])
            elif parameters.startswith("If false"):
                monkeyIfFalse = int(parameters.split(" ")[-1])
        
        currMonkey = Monkey(number, items, ARITHMETIC_OPERATION[operation], operationNum, divisible, monkeyIfTrue, monkeyIfFalse)
        monkeys.append(currMonkey)

    return monkeys 

def solve():
    data = parseInput("sample.in")

    part1(data)

def part1(data: list[Monkey]):
    listMonkeys = list(data) # Make a copy
    


def part2():
    pass

if __name__ == "__main__":
    solve()