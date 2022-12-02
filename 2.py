with open("2.txt", "r") as dataFile:
    
    line = dataFile.readline()

    score = 0
    playScore = {
        "X": 1, # A | Rock
        "Y": 2, # B | Paper
        "Z": 3  # C | Scissors
    }
    WIN = 6
    LOSE = 0
    DRAW = 3
    while line != "":
        line = line.strip()
        opp, me = line.split(" ")

        score += playScore[me]

        if me == "X" and opp == "C":
            score += WIN 
        
        elif me == "X" and opp == "A":
            score += DRAW 
        
        elif me == "Y" and opp == "A":
            score += WIN 
        elif me == "Y" and opp == "B":
            score += DRAW

        elif me == "Z" and opp == "B":
            score += WIN 
        elif me == "Z" and opp == "C":
            score += DRAW 

        line = dataFile.readline()

    print(score)            
        