
import pygame, sys, time
import file_handler
import re
import os
from pydub import AudioSegment

#Thanks to https://www.geeksforgeeks.org/python/cut-a-mp3-file-in-python/ for making new audio file

class Audio_Controller:

    song_dict = dict()
    MUSIC_FILE = "my_music.txt"
    

    def __init__(self):
        
        self.song_dict = file_handler.file_reader(self.MUSIC_FILE)
        
        for key in self.song_dict:
            
            hasEnd = False
            if self.song_dict[key].getEnd() != None:
                link = ".\\music_files\\" + self.song_dict[key].getLink()
                self.song_dict[key].setEndLink(link[:-4] + "end.mp3")
                hasEnd = True
            if self.song_dict[key].getRestart() != None:
                if hasEnd:
                    link = self.song_dict[key].getEndLink()
                else:
                    link = ".\\music_files\\" + self.song_dict[key].getLink()
                self.song_dict[key].setResLink(link[:-4] + "restart.mp3")
        pygame.mixer.init()

        

    def play_song(self, openList):
        looper = 0
        try:
            selectedSong = self.song_dict[openList[0]]

            pygame.mixer.music.load("./music_files/" + selectedSong.getLink())
        
        except:
            print("No song found with that name. Please load one with -load or check a list of loaded songs with -list")


        for i in range(len(openList)-1):
            if openList[i+1] == "l":
                looper = -1
                if selectedSong.getEndLink() != None:
                    pygame.mixer.music.load(filename=selectedSong.getEndLink())
                if selectedSong.getResLink() != None:
                    looper = 0
                    pygame.mixer.music.queue(filename=selectedSong.getResLink(), loops = -1)
        pygame.mixer.music.play(loops = looper)

        

        

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

            if self.song_dict[usrInputList[0].lower()].getEnd() != None:
                end = self.song_dict[usrInputList[0].lower()].getEnd()
                link = ".\\music_files\\" + self.song_dict[usrInputList[0].lower()].getLink()
                song = AudioSegment.from_file(
                        link, format="mp3")
                #File before end time
                nextSong = song[:(float(end)*1000)]

                # save file
                nextSong.export(link[:-4] + "end.mp3",
                                        format="mp3")
                self.song_dict[usrInputList[0].lower()].setEndLink(link[:-4] + "end.mp3")

            if self.song_dict[usrInputList[0].lower()].getRestart() != None:
                restart = self.song_dict[usrInputList[0].lower()].getRestart()
                if self.song_dict[usrInputList[0].lower()].getEndLink() != None:
                    link = self.song_dict[usrInputList[0].lower()].getEndLink()
                else:
                    link = ".\\music_files\\" + self.song_dict[usrInputList[0].lower()].getLink()
                song = AudioSegment.from_file(
                        link, format="mp3")
                #File after restart time
                nextSong = song[(float(restart)*1000):]

                # save file
                nextSong.export(link[:-4] + "restart.mp3",
                                        format="mp3")
                self.song_dict[usrInputList[0].lower()].setResLink(link[:-4] + "restart.mp3")


        elif usrInputList[0] == "-delete":
            #Error handling here if input is wrong
            if self.song_dict[usrInputList[1].lower()].getResLink() != None:
                os.remove(self.song_dict[usrInputList[1].lower()].getResLink())

            if self.song_dict[usrInputList[1].lower()].getEndLink() != None:
                os.remove(self.song_dict[usrInputList[1].lower()].getEndLink())
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
        
    def getResLink(self):
        if self.infoDict.__contains__("resLink"):
            return self.infoDict["resLink"]
        else:
            return None
    
    def getEndLink(self):
        if self.infoDict.__contains__("endLink"):
            return self.infoDict["endLink"]
        else:
            return None
        
    def getEnd(self):
        if self.infoDict.__contains__("end"):
            return self.infoDict["end"]
        else:
            return None
    
    def setResLink(self, link):
        self.infoDict["resLink"] = link
    
    def setEndLink(self, link):
        self.infoDict["endLink"] = link

    def toString(self):
        myStr = "Link: " + self.infoDict["link"]
        if self.infoDict.__contains__("restart"):
            myStr = myStr + "\n" + "Restart time: " + self.infoDict["restart"]
        if self.infoDict.__contains__("end"):
            myStr = myStr + "\n" + "End time: " + self.infoDict["end"]
        
        return myStr

    def toFile(self):
        myStr = self.infoDict["link"]

        if self.infoDict.__contains__("restart"):
            myStr = myStr + " " + "restart=" + self.infoDict["restart"]
        
        if self.infoDict.__contains__("end"):
            myStr = myStr + " " + "end=" + self.infoDict["end"]
        
        return myStr

