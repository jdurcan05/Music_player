

import pygame, sys, time
import file_handler
import re
# from pydub import AudioSegment

class Audio_Controller:

    song_dict = dict()
    MUSIC_FILE = "my_music.txt"
    

    def __init__(self):
        
        self.song_dict = file_handler.file_reader(self.MUSIC_FILE)
        
        pygame.mixer.init()

        

    def play_song(self, openList):
        looper = 0
        try:
            selectedSong = self.song_dict[openList[0]]
            for i in range(len(openList)-1):
                if openList[i+1] == "l":
                    looper = -1

            pygame.mixer.music.load("./music_files/" + selectedSong.getLink())
            pygame.mixer.music.play(loops=looper)

        except:
            print("No song found with that name. Please load one with -load or check a list of loaded songs with -list")

        

    def simple_command(self, usrInput):

        if usrInput[0] == 'x':
            length = 1000
            if len(usrInput) > 1:
                length = 1000*int(usrInput[1])
            pygame.mixer.music.fadeout(length)
        elif usrInput[0] == "exit":
            sys.exit()
        elif len(usrInput[0]) == 3:
            self.play_song(usrInput)
        else: 
            print("Unrecognized command; please type help for a list of implimented commands")

    

    def complex_command(self, usrInputList):

        if usrInputList[0] == "-load":
            #Error handling here if file not found
            self.song_dict[usrInputList[1].lower()] = Song(usrInputList[2:])

            #gets rid of load command
            for i in range(len(usrInputList)):
                if i != 0:
                    usrInputList[i-1] = usrInputList[i]
            del(usrInputList[len(usrInputList)-1])

            file_handler.file_writer(self.MUSIC_FILE, usrInputList)
            # if self.song_dict[usrInputList[1].lower()].getRestart!= None:
                

        elif usrInputList[0] == "-delete":
            #Error handling here if input is wrong
            del(self.song_dict[usrInputList[1].lower()])
            file_handler.rewrite_file(self.MUSIC_FILE, self.song_dict)

        elif usrInputList[0] == "-list":
            for key in self.song_dict:
                print (key.upper() + ": " + self.song_dict[key].getLink())
        
        elif usrInputList[0] == "-info":
            #Every new feature of song class must go here
            #Maybe a song tostring method would be a better way to handle this
            try:
                access_song = self.song_dict[usrInputList[1]]
            except:
                print("No song of that title found; type -list for a list of loaded songs")
                return
            print("Key: " + usrInputList[1].upper())
            print(access_song.toString())



        else: 
            print("Unrecognized command; please type help for a list of implimented commands")




class Song:

    
    
    def __init__(self, infoList):
        self.infoDict = dict()
        self.infoDict["link"] = infoList[0]
        for i in infoList[1:]:
            smallList = re.split("=", i)
            self.infoDict[smallList[0]] = smallList[1]

    
    def getLink(self):
        return self.infoDict["link"]

    def getRestart(self):
        if self.infoDict.__contains__("restart"):
            return self.infoDict["restart"]
        else:
            return None
        
    def toString(self):
        myStr = "Link: " + self.infoDict["link"]
        if self.infoDict.__contains__("restart"):
            myStr = myStr + "\n" + "Restart time: " + self.infoDict["restart"]
        
        return myStr

    def toFile(self):
        myStr = self.infoDict["link"]

        if self.infoDict.__contains__("restart"):
            myStr = myStr + " " + "restart=" + self.infoDict["restart"]
        
        return myStr

