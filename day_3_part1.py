# https://adventofcode.com/2022/day/3

def getPriority(char):
    if ord(char) >= ord('a'):
        # Is lowercase
        return ord(char) - ord('a') + 1
    
    # Is uppercase
    return ord(char) - ord("A") + 27


def main():
    with open("day_3.txt", "r") as dataFile:
    
        total = 0

        line = dataFile.readline()
        while line != "":
            line = line.strip()

            first = line[:int(len(line)/2)]
            second = line[int(len(line)/2):]
        
            f_set = set(list(first))
            s_set = set(list(second))

            intersect = f_set.intersection(s_set)

            for i in intersect:
                total += getPriority(i)

            line = dataFile.readline()

        print(total)

main()
