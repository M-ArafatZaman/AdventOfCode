with open("data.in", "r") as dataFile:
    
    line = dataFile.readline()

    highest = -1
    curr = 0

    while line != "":
        line = line.strip()

        if line == "":
            if curr > highest:
                highest = curr

            curr = 0
        else:
            curr += int(line)
        
        line = dataFile.readline()

    if curr > highest:
        highest = curr

    print(highest)