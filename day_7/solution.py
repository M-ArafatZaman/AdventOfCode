# Directory class structure
class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subdirs = []
        self.files = []

def loadDirectory():
    data = open("input.in", "r").read().splitlines()
    
    rootDir = Directory("/")
    # Iterate through each line, keep track of current directory, and check for file sizes
    # CurrDir stores the current level directory
    currDir = None
    for l in data:
        line = l.split()
        if line[0] == "$": # Tis a command chief
            # Change dir 
            if line[1] == "cd":
                
                if line[2] == "/":
                    currDir = rootDir
                elif line[2] == "..":
                    currDir = currDir.parent
                else:
                    # Change to the newly created subdir
                    subDir = Directory(line[2], currDir)
                    currDir.subdirs.append(subDir)
                    currDir = subDir

        # If its a number its a file size, so store it in curr dir 
        elif line[0].isnumeric():
            currDir.files.append(int(line[0])) # Store the file size

    return rootDir

def part1(dirSizes):
    return sum([i for i in dirSizes if i <= 100000])

def part2(dirSizes):
    dirSizes.sort()
    rootDirSize = dirSizes[-1] # Root dir size is appended at the last
    NEEDED = rootDirSize + 30000000 - 70000000
    for i in dirSizes:
        if i > NEEDED:
            return i

def solve():
    rootDir = loadDirectory()
    dirSizes = []

    # Iterate through each dirs and subdirs and count the size
    def countDirSize(dir: Directory):
        size = sum(dir.files) + sum([countDirSize(i) for i in dir.subdirs])
        dirSizes.append(size)
        return size

    countDirSize(rootDir)

    print("Part 1 =>", part1(dirSizes))
    print("Part 2 =>", part2(dirSizes))

if __name__ == "__main__":
    solve()