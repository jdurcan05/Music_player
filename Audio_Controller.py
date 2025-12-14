import pygame, sys, time
import file_handler
import re

class Audio_Controller:

    song_dict = dict()
    MUSIC_FILE = "my_music.txt"

    def __init__(self):
        
        self.song_dict = file_handler.file_reader(self.MUSIC_FILE)

        pygame.mixer.init()
        

    def play_song(self, openList):
        looper = 0
        selectedSong = self.song_dict[openList[0]]
        for i in range(len(openList)-1):
            if openList[i+1] == "l":
                looper = -1

        pygame.mixer.music.load("./music_files/" + selectedSong.getLink())
        test = selectedSong.getRestart()
        pygame.mixer.music.play(loops=looper)

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

    

    def complex_command(self, usrInputList):

        if usrInputList[0] == "-load":
            self.song_dict[usrInputList[1].lower()] = Song(usrInputList[2:])

            #gets rid of load command
            for i in range(len(usrInputList)):
                if i != 0:
                    usrInputList[i-1] = usrInputList[i]
            del(usrInputList[len(usrInputList)-1])

            file_handler.file_writer(self.MUSIC_FILE, usrInputList)

        if usrInputList[0] == "-delete":
            del(self.song_dict[usrInputList[1].lower()])
            file_handler.rewrite_file(self.MUSIC_FILE, self.song_dict)


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

