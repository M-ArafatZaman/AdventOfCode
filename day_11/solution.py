import re
import copy

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

def main():
    data = parseInput("input.in")

    # Deep copy is used because objects and lists are mutable
    # Part 1 changes data if not deep copied
    print("PART 1 ->", solve(copy.deepcopy(data), 1))
    print("PART 2 ->", solve(copy.deepcopy(data), 2))

def solve(listMonkeys: list[Monkey], part=1):
    ROUNDS = 20 if part == 1 else 10000
    # Calculate the MODULO for part 2
    mods = [int(i.divisible) for i in listMonkeys]
    mod = 1
    for i in mods:
        mod *= i
    itemsInspected = [0] * len(listMonkeys)
    # Iterate through each rounds
    for _ in range(ROUNDS):
        # Iterate each monkey
        m = 0
        while m < len(listMonkeys):
            monkey = listMonkeys[m]
            # Iterate each item
            while len(monkey.items) > 0:
                # Inspect
                item = monkey.items[0]
                item = monkey.operation(item, int(monkey.operationNum) if monkey.operationNum != "old" else item)
                # For part 1, item level is managed by dividing by 3
                # For part 2, item level is MODULE of the product of all "divisible" check operations
                item = item//3 if part == 1 else item % mod
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

if __name__ == "__main__":
    main()