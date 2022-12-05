import re
from typing import List

def getData(fName):
    """
    @return crates object, instructions list
    """
    with open(fName, "r") as dataFile:
        data = [ i for i in dataFile.readlines() ]
    
    # Crates stored in cols
    crates = {}

    # Load crates
    i = 0
    t_cols = 0
    while "[" in data[i]: # (HACKY) Is a crate

        _crates = re.findall("[A-Z]", data[i])
        # Get each index in string and calculate col
        for cr in _crates:
            cr_i = data[i].index(cr)
            col = getCol(cr_i)

            if col > t_cols:
                t_cols = col # Keep a record of total columns

            # Load but prepend since we are scanning from top to bottom
            col_crates: List[str] = crates.get(str(col), [])
            col_crates = [cr] + col_crates 
            crates[str(col)] = col_crates

            # Remove the crate from the dataline
            data[i] = data[i][:cr_i] + " " + data[i][cr_i+1:]

        i += 1

    i += 2

    instructions: List[List[int]] = []

    while i < len(data):
        # "move 2 from 1 to 7"
        
        #no, frm, to = re.findall("[1-9]", data[i])
        
        # Extract the parameters
        matches = []
        strBuf = ""        
        j = 0 # 0 means no, 1 means frm, 2 means to
        while j < len(data[i]):
            if data[i][j].isnumeric():
                strBuf += data[i][j]
            elif len(strBuf) > 0:
                # Clear buffer
                matches.append(int(strBuf))
                strBuf = ""

            j += 1

        # Clear buffer again
        if len(strBuf) > 0:
            matches.append(int(strBuf))
            strBuf = ""

        instructions.append(matches)

        i+=1

    return crates, instructions

def getCol(i):
    # Arithmetic series to calculate cols
    return ((i - 1)//4) + 1

def printCrates(dct):

    for i in range(1, len(dct.keys())+1):
        print(i , "==", dct[str(i)])

def part1():
    crates, instructions = getData("data.in")

    for i in instructions:

        no, frm, to = i 
        frm = str(frm)
        to = str(to)

        # Move
        for __c in range(no):
            crt = crates[frm].pop()
            crates[to].append(crt)

    ans = ""

    for k in range(1, len(crates.keys())+1):
        ans += crates[str(k)][len(crates[str(k)])-1]

    print(ans)


def part2():
    crates, instructions = getData("data.in")

    for i in instructions:

        no, frm, to = i 
        frm = str(frm)
        to = str(to)

        # Standard copy and paste will do
        removed = crates[frm][len(crates[frm])-no:]
        crates[frm] = crates[frm][:len(crates[frm])-no]
        crates[to] += removed

    ans = ""

    for k in range(1, len(crates.keys())+1):
        ans += crates[str(k)][len(crates[str(k)])-1]

    print(ans)


if __name__ == "__main__":
    print("Part 1 -> ")
    part1()
    print("Part 2 -> ")
    part2()