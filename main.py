import pygame, sys, time
import file_handler

#Nor working
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

#Big help lad: https://www.youtube.com/watch?v=xdkY6yhEccA&t=938s

MUSIC_FILE = "my_music.txt"

def simple_command(usrInput):

    if len(usrInput) == 3:
        pygame.mixer.music.load("./music_files/" + song_dict[usrInput])
        pygame.mixer.music.play()

    elif usrInput == "x":
        pygame.mixer.music.stop()

    elif usrInput == "exit program":
        sys.exit()

def complex_command(usrInputList):

    if usrInputList[0] == "-load":
        song_dict[usrInputList[1].lower()] = usrInputList[2]

        #gets rid of load command
        for i in range(len(usrInputList)):
            if i != 0:
                usrInputList[i-1] = usrInputList[i]
        del(usrInputList[len(usrInputList)-1])

        file_handler.file_writer(MUSIC_FILE, usrInputList)

    if usrInputList[0] == "-delete":
        del(song_dict[usrInputList[1].lower()])
        file_handler.rewrite_file(MUSIC_FILE, song_dict)


song_dict = file_handler.file_reader(MUSIC_FILE)

pygame.mixer.init()

while True:
    usrInput = input("Command: ")

    if usrInput[0] == "-":
        usrInput = usrInput.split()
        complex_command(usrInput)
    else:
        usrInput = usrInput.lower()
        simple_command(usrInput)
    

