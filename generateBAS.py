def generateBAS(fName: str):
    """
    This function generates an applesoft basic data file which can be 
    used to solve the AOC challenge in applesoft basic.
    """

    with open(fName, "r") as dataFile:

        lines: int = 0
        bas_data = ""

        for line in dataFile.readlines():
            lines += 1
            line = line.strip()

            bas_data += f"{str(2000+lines)} "
            if line.isnumeric() or (line.replace(".", "").isnumeric() and line.count(".") == 1):
                bas_data += f"DATA {line}\n"
            else:
                bas_data += f'DATA "{line}"\n'
            

        bas = f"""10 CLEAR : HOME
20 LET lines = {lines}
30 REM: Write your program here...





2000 REM: You input data starts here
""" + bas_data

        with open("app.bas", "w") as outputFile:
            outputFile.write(bas)

        
generateBAS("test.txt")