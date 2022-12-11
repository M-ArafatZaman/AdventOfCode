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
    data = parseInput("input.in")

    print(part2(data))

def part1(data: list[Monkey]):
    listMonkeys: list[Monkey] = list(data) # Make a copy
    round = 0
    itemsInspected = [0] * len(data)
    # Iterate through each rounds
    for _ in range(20):
        # Iterate each monkey
        m = 0
        while m < len(listMonkeys):
            monkey = listMonkeys[m]
            # Iterate each item
            while len(monkey.items) > 0:
                # Inspect
                item = monkey.items[0]
                item = monkey.operation(item, int(monkey.operationNum) if monkey.operationNum != "old" else item)
                item = item//3
                if item % int(monkey.divisible) == 0:
                    listMonkeys[monkey.monkeyIfTrue].items.append(item)
                else:
                    listMonkeys[monkey.monkeyIfFalse].items.append(item)
                monkey.items.pop(0)
                # Count inspection
                itemsInspected[m] += 1
            m += 1
        
        # Print for reference
    itemsInspected.sort()
    return itemsInspected[-1] * itemsInspected[-2]

def part2(data: list[Monkey]):
    listMonkeys: list[Monkey] = list(data) # Make a copy
    round = 0
    itemsInspected = [0] * len(data)
    # Calculate the modulo 
    mods = [int(i.divisible) for i in listMonkeys]
    mod = 1
    for i in mods:
        mod *= i
    # Iterate through each rounds
    for _ in range(10000):
        # Iterate each monkey
        m = 0
        while m < len(listMonkeys):
            monkey = listMonkeys[m]
            # Iterate each item
            while len(monkey.items) > 0:
                # Inspect
                item = monkey.items[0]
                item = monkey.operation(item, int(monkey.operationNum) if monkey.operationNum != "old" else item)
                item = item % mod
                if item % int(monkey.divisible) == 0:
                    listMonkeys[monkey.monkeyIfTrue].items.append(item)
                else:
                    listMonkeys[monkey.monkeyIfFalse].items.append(item)
                monkey.items.pop(0)
                # Count inspection
                itemsInspected[m] += 1
            m += 1

    itemsInspected.sort()
    return itemsInspected[-1] * itemsInspected[-2]

if __name__ == "__main__":
    solve()