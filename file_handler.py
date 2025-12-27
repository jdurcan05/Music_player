import Audio_Controller

def file_writer(myFile, inputList):
    inString = ""
    for i in inputList:
        inString = inString + i + " "
    inString = inString[:len(inString)-1]
    # print(inString)
    inString = inString + "\n"
    with open(myFile,"a") as f:
        f.write(inString)
        

def file_reader(myFile):
    pre_list = dict()
    with open(myFile) as f:
        for line in f:
            parser = line.split()
            #Set the key up 
            key = parser[0].lower()
            pre_list[key] = []
            #Put everything in the key, link first
            for i in range(len(parser)-1):
                pre_list[key].append(parser[i+1])
            pre_list[key] = Audio_Controller.Song(pre_list[parser[0].lower()])

    return pre_list

def rewrite_file(myFile, myDict):
    with open(myFile, "w") as f:
        for key in myDict:
            inString = key + " "
            inString = inString + myDict[key].toFile()
            f.write(inString)
            f.write("\n")


