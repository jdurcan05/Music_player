import pygame, sys, time

#Nor working
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

#Big help lad: https://www.youtube.com/watch?v=xdkY6yhEccA&t=938s

pygame.mixer.init()


while True:
    usrInput = input("Command: ")
    usrInput = usrInput.lower()

    if usrInput == "lcs":
        pygame.mixer.music.load("./music_files/lace_silksong.mp3")
        pygame.mixer.music.play()
    elif usrInput == "bxf":
        pygame.mixer.music.load("./music_files/DR_box15.mp3")
        pygame.mixer.music.play()
    elif usrInput == "x":
        pygame.mixer.music.stop()
    elif usrInput == "exit program":
        sys.exit()
    

