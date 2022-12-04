def generateBAS(fName: str):
    """
    This function generates an applesoft basic data file which can be 
    used to solve the AOC challenge in applesoft basic.
    """

    with open(fName, "r") as dataFile:

        lines: int = 0
        bas_data = []

        # Store each line in an array
        for line in dataFile.readlines():
            lines += 1
            line = line.strip()

            if line.isnumeric() or (line.replace(".", "").isnumeric() and line.count(".") == 1):
                if int(line) - float(line) == 0:
                    bas_data.append(int(line))
                else:
                    bas_data.append(float(line))

            else:
                bas_data.append(str(line))

        # Convert each line to the DATA line
        # Ensure that data line does not surpass 239 chars
        bas_data_str = "2001 DATA "
        currCharCount = len(bas_data_str)
        currLine = 1
        for i in bas_data:
            if type(i) == str:
                data = f'"{i}",' 
            else:
                data = str(i)+"," 
            
            currCharCount += len(data)

            if currCharCount >= 200:
                bas_data_str = bas_data_str[:len(bas_data_str)-1]
                bas_data_str += "\n"
                currLine += 1
                newLine = f"{2000+currLine} DATA "
                bas_data_str += newLine
                bas_data_str += data
                currCharCount = len(newLine)
            else:
                bas_data_str += data

        bas_data_str = bas_data_str[:len(bas_data_str)-1]            

        bas = f"""10 CLEAR : HOME
20 LET lines = {lines}
30 REM: Write your program here...





2000 REM: Your input data starts here
""" + bas_data_str

        with open("app.bas", "w") as outputFile:
            outputFile.write(bas)

        
generateBAS("test.txt")