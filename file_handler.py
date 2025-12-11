def file_writer(myFile, inputList):
    inString = ""
    for i in inputList:
        inString = inString + i + " "
    inString = inString[:len(inString)-1]
    print(inString)
    with open(myFile,"a") as f:
        f.write(inString)
        

def file_reader(myFile):
    linker = dict()
    with open(myFile) as f:
        for line in f:
            parser = line.split()
            linker[parser[0].lower()] = parser[1]
    return linker

def rewrite_file(myFile, myDict):
    with open(myFile, "w") as f:
        for key in myDict:
            inString = key + " " + myDict[key]
            f.write(inString)
            f.write("\n")


