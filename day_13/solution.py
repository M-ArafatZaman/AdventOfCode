from copy import deepcopy

def parseInput(fName="input.in"):
    rdata = open(fName, "r").readlines()
    rdata = [i.strip() for i in rdata]
    return [eval(i) for i in rdata if i != ""]


def solve():
    data = parseInput("input.in")
    
    print(part1(deepcopy(data)))

def part1(data):
    total = 0
    i = 0
    while i < len(data):
        left = data[i]
        right = data[i+1]
        i += 2
        check = compareData(deepcopy(left), deepcopy(right))
        if check: 
            total += i // 2
    return total

# Is valid packet
def compareData(left, right) -> bool:
    if type(left) == int and type(right) == int: 
        if left < right: return True
        if left > right: return False
        return None
    #if type(left) == list and type(right) == list and len(left) > len(right): return False
    if type(left) == list and type(right) != list: right = [right]
    if type(left) != list and type(right) == list: left = [left]
    # Both are lists
    inOrder = None
    while len(left) > 0 and len(right) > 0 and (inOrder == None):
        l = left.pop(0)
        r = right.pop(0)
        inOrder = compareData(deepcopy(l), deepcopy(r))

    if inOrder != None:
        return inOrder
    elif len(left) == 0 and len(right) > 0:
        return True
    elif len(left) > 0 and len(right) == 0:
        return False
    
    return None

def part2():
    pass 

if __name__ == "__main__":
    solve()