with open("data.in", "r") as dataFile:
    
    line = dataFile.readline()

    first = -1
    second = -2
    third = -3
    curr = 0

    while line != "":
        line = line.strip()

        if line == "":
            if curr > first:
                third = second
                second = first
                first = curr
            elif curr > second and curr < first:
                third = second
                second = curr
            elif curr > third and curr < second:
                third = curr

            curr = 0
        else:
            curr += int(line)
        
        line = dataFile.readline()

    if curr > first:
        third = second
        second = first
        first = curr
    elif curr > second and curr < first:
        third = second
        second = curr
    elif curr > third and curr < second:
        third = curr

    print(first + second + third)
