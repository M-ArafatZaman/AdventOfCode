
def main():
    with open("data.in", "r") as dataFile:
        
        count = 0

        for line in dataFile.readlines():
            line = line.strip()

            pair1, pair2 = line.split(",")

            # Pair 1
            pair1_start = int(pair1.split("-")[0])
            pair1_end = int(pair1.split("-")[1])

            # Pair 2
            pair2_start = int(pair2.split("-")[0])
            pair2_end = int(pair2.split("-")[1])

            if pair1_start >= pair2_start and pair1_end <= pair2_end:
                count += 1
            
            elif pair2_start >= pair1_start and pair2_end <= pair1_end:
                count += 1
            
            elif pair1_start >= pair2_start and pair1_start <= pair2_end:
                count += 1

            elif pair1_end >= pair2_start and pair1_end <= pair2_end:
                count += 1

        print(count)

main()