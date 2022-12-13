from copy import deepcopy
import functools

def parseInput(fName="input.in"):
    rdata = open(fName, "r").readlines()
    rdata = [i.strip() for i in rdata]
    return [eval(i) for i in rdata if i != ""]

def solve():
    data = parseInput("input.in")
    
    print("PART 1 ->", part1(deepcopy(data)))
    print("PART 2 ->", part2(deepcopy(data)))

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
# True means they are right order
# False means they are NOT in the right order
# None means that they are equal
def compareData(left, right) -> bool:
    left = deepcopy(left)
    right = deepcopy(right)
    if type(left) == int and type(right) == int: 
        if left < right: return True
        if left > right: return False
        return None
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

    # Both the lists are equal
    return None

# This function is used as a key comparator for the sort function
def compareDataComparator(left, right):
    resp = compareData(left, right)
    if resp == True:
        return -1
    elif resp == False:
        return 1
    else:
        return 0

def part2(data: list):
    A = [[2]]
    B = [[6]]
    data.append(A)
    data.append(B)
    data.sort(key=functools.cmp_to_key(compareDataComparator))
    
    return (data.index(A) + 1) * (data.index(B) + 1)

if __name__ == "__main__":
    solve()