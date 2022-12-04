with open("data.in", "r") as dataFile:
    
    line = dataFile.readline()

    score = 0
    # A | Rock      - 1
    # B | Paper     - 2
    # C | Scissors  - 3
    counterStrate = {
        "win": {
            "A": 2,
            "B": 3,
            "C": 1
        },
        "lose": {
            "A": 3,
            "B": 1,
            "C": 2
        },
        "draw": {
            "A": 1,
            "B": 2,
            "C": 3
        }
    }
    WIN = 6
    LOSE = 0
    DRAW = 3
    while line != "":
        line = line.strip()
        opp, me = line.split(" ")

        if me == "X": # Lose
            score += counterStrate["lose"][opp] + LOSE
        elif me == "Y": # Draw
            score += counterStrate["draw"][opp] + DRAW
        elif me == "Z": # Win
            score += counterStrate["win"][opp] + WIN
        
        line = dataFile.readline()

    print(score)            
        