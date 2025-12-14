import Audio_Controller as AC

#Nor working
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

#Big help lad: https://www.youtube.com/watch?v=xdkY6yhEccA&t=938s

songer = AC.Audio_Controller()

while True:
    usrInput = input("Command: ")

    if usrInput[0] == "-":
        usrInput = usrInput.split()
        songer.complex_command(usrInput)
    else:
        #This is here because I can't think of use case when it shouldnt be
        usrInput = usrInput.lower()
        usrInput = usrInput.split()
        songer.simple_command(usrInput)
    

