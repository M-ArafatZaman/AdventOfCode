# https://adventofcode.com/2022/day/3

def getPriority(char):
    if ord(char) >= ord('a'):
        # Is lowercase
        return ord(char) - ord('a') + 1
    
    # Is uppercase
    return ord(char) - ord("A") + 27


def main():
    with open("data.in", "r") as dataFile:
    
        total = 0

        line = dataFile.readline()
        while line != "":
            line = line.strip()
            line2 = dataFile.readline().strip()
            line3 = dataFile.readline().strip()

            first = set(list(line))
            second = set(list(line2))
            third = set(list(line3))

            intersect = first.intersection(second, third)

            for i in intersect:
                total += getPriority(i)

            line = dataFile.readline()

        print(total)

main()
