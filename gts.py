import keyboard
import random
import os
import time
import visuals
import board
import neopixel
import RPi.GPIO as GPIO
GPIO.setup(15,GPIO.OUT)
GPIO.output(15,GPIO.HIGH)

SIZE = 242
COLUMNS = 22
STARTING_POSITION = 120
global field
field = [0]*SIZE

leds = neopixel.NeoPixel(board.D18, SIZE)

def printfield():
    for i in range(SIZE):
        if field[i] == 0:
            leds[i] = (0,0,0)
        else:
            leds[i] = (255,0,0)

def randomsquare(path):
    way=[COLUMNS,-COLUMNS,1,-1]
    while True:
        r=random.choice(way)
        pos=r+path[-1]
        if field[pos]!=1 and 0<=pos<SIZE:
            path.append(pos)
            return path

def path_to_field(path,new,n):
    if new==True:                   #if the path gets longer
        for p in path:
            field[p]=1
        printfield()
        time.sleep(1)
        for x in range(SIZE):
            field[x]=0
    else:                           #in game
        for x in range(n):
            field[path[x]]=1
            printfield()


def move(previous_pos,path,pos,score):
    while True:
        key=keyboard.read_key()
        if key in ["a","d","s","w"]:
            if key=="a":
                if pos-1 in path and pos-1 != previous_pos:
                    return pos-1
                else:                   #bug fix
                    endscreen(score)
                    return False
            if key=="d":
                if pos + 1 in path and pos + 1 != previous_pos:
                    return pos + 1
                else:                   #bug fix
                    endscreen(score)
            if key =="s":
                if pos + COLUMNS in path and pos + COLUMNS != previous_pos:
                    return pos + COLUMNS
                else:                   #bug fix
                    endscreen(score)
                    return False
            if key=="w":
                if pos - COLUMNS in path and pos - COLUMNS != previous_pos:
                    return pos - COLUMNS
                else:
                    endscreen(score)
                    return False



def endscreen(score):
    os.system('cls' if os.name == 'nt' else 'clear')
    visuals.score_p()
    visuals.num_con(int(score-1))
    with open("highscore_gts.txt","r") as highscore:
        score_old=highscore.read()
    if int(score_old) < score-1:
        with open("highscore_gts.txt", "w") as highscore:
            highscore.write(str(score-1))
            print("sdfdsfdsf")
        visuals.hscore_p()
        visuals.num_con(score-1)
    else:
        visuals.hscore_p()
        visuals.num_con(int(score_old))


def start():
    path = [STARTING_POSITION]
    score = 0
    pos=STARTING_POSITION
    while pos!=False:           #as long as the endscreen did'nt happen yet
        score+=1
        path = randomsquare(path)
        path_to_field(path,True,score)
        pos = STARTING_POSITION
        n=1
        previous_pos = STARTING_POSITION

        while n<=score and pos!=False:
            path_to_field(path,False,n)
            temporary_pos=pos
            pos=move(previous_pos,path,pos,score)
            previous_pos=temporary_pos
            n+=1
            time.sleep(0.2)


