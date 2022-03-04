import keyboard
import threading
import random
import os
size = 200

import time


global field
field = [0]*(size*2)
global shippos
shippos=[102,103]


def printfield():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(size):
        if i%(20)==0:
            print("")
        print(field[i],end="")

    print("")



def endscreen():
    print("Sie haben verloren")
    quit()
def lightup(path):
    for step in path:
        field[step]=1
    printfield()
    time.sleep(5)
    for step in path:
        field[step]=0
    field[90] = 1
    printfield()

def key():
    if keyboard.is_pressed("w"):
        return -20
    elif keyboard.is_pressed("s"):
        return 20
    elif keyboard.is_pressed("d"):
        return 1
    elif keyboard.is_pressed("a"):
        return -1
    else:
        return 0




def worms():
    counter = 0
    level=1
    path1=[195,175,155,75,55,35,15]
    path1_=[135,115,95]
    path2 = [195, 175, 155, 135, 55, 35, 15]
    path2_=[115,95,75]
    path3 = [195, 175, 95, 75, 55, 35, 15]
    path3_=[155,135,115]
    path4 = [195, 175, 155, 135, 115, 35, 15]
    path4_=[95,75,55]
    level=1

    def shipcontrol(path):
        if shippos[0] in path or shippos[1] in path:
            endscreen()


    while True:
        for lev in range(level):
            if counter==0:
                for block in path1:
                    field[block-lev*3]=1
                for block in path1_:
                    field[block-lev*3] = 0
                shipcontrol(path1)

            elif counter==1:
                for block in path2:
                    field[block-lev*3]=1
                for block in path2_:
                    field[block-lev*3] = 0
                shipcontrol(path2)
            elif counter == 2:
                for block in path3:
                    field[block-lev*3] = 1
                for block in path3_:
                    field[block-lev*3] = 0
                shipcontrol(path3)
            elif counter == 3:
                for block in path4:
                    field[block-lev*3] = 1
                for block in path4_:
                    field[block-lev*3] = 0
                shipcontrol(path4)
                counter=-1
        counter+=1
        for i in range(10):
            if i*20+19 in shippos:
                level+=1
        printfield()
        time.sleep(3)



def control(newpos):
    if field[newpos[0]]==1 or field[newpos[1]]==1:
        endscreen()

def spaceship(keys,oldposition):
    field[oldposition[0]] = 0
    field[oldposition[1]] = 0
    newpos=[oldposition[0]+keys,oldposition[1]+keys]
    control(newpos)
    field[oldposition[0]+keys]=1
    field[oldposition[1]+keys]=1
    oldposition=[oldposition[0]+keys,oldposition[1]+keys]
    printfield()
    return oldposition


if __name__ == '__main__':

    threading.Thread(target=worms).start()
    #[102,103]
    keys=0
    while True:
        keys=key()
        shippos=spaceship(keys,shippos)
        time.sleep(0.1)








