import keyboard
import threading
import random
import os
import numbers
SIZE = 242
ROWS=11
COLS=22
STARTING_POINT=120
import time


global field
field = [0]*(SIZE*2)
global mover

def printfield():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(SIZE):
        if i%(22)==0:
            print("")
        if field[i]==0:
            print("[ ]", end="")
        else:
            print("[X", end="]")


    print("")

def fruits(position):
    fruitposition = random.randint(0, SIZE-1)
    while fruitposition in position:
        fruitposition = random.randint(0, SIZE-1)
    field[fruitposition]="X"


def moving():
    while True:
        key=keyboard.read_key()
        if key in ["a","d","s","w"]:
            if key=="w":
                field[SIZE] = -22
            if key == "s":
                field[SIZE] = 22
            if key == "a":
                field[SIZE] = -1
            if key == "d":
                field[SIZE]=1
def endscreen(length):
    os.system('cls' if os.name == 'nt' else 'clear')
    score_p()
    num_con(length+1)
    with open("highscore_snake.txt","r") as highscore:
        score=highscore.read()
    if int(score) < (length + 1):
        with open("highscore_snake.txt", "w") as highscore:
            length=length+1
            highscore.write(str(length))
            hscore_p()
            num_con(length+1)
    else:
        hscore_p()
        num_con(length + 1)


def positionupdate(position,length):

    if length>0:
        field[position[length]]=0
        for i in reversed(range(length)):
            position[i+1] = position[i]
    else:
        field[position[0]]=0
    if field[position[0]+field[SIZE]]==1:
        endscreen(length)
        return False
    else:
        position[0]=position[0]+field[SIZE]

    #for number in range(length+1):
        #position[number]=position[number]
    for number in reversed(range(length+1)):
        x=field[SIZE]
        field[SIZE+number]=field[SIZE+number+1]
        field[SIZE]=x
    return position

def bordercontrol(position,length):
    for i in range(ROWS):
        if position[0] <0 or position[0] >SIZE-1:
            endscreen(length)


        elif field[SIZE]==1:
            for next in range(1,ROWS):
                if position[0]==22*next:
                    endscreen(length)
        elif field[SIZE]==-1:
            for next in range(1,ROWS,2):
                if position[0]==ROWS*next+ROWS-1:
                    endscreen(length)



def score_p():
    for x in range(198):
        if x%22==0:
            print("")
        if numbers.score[x]==1:
            print("[X]",end="")
        else:
            print("[ ]",end="")
    print("")
    time.sleep(1)
def hscore_p():
    os.system('cls' if os.name == 'nt' else 'clear')
    for x in range(198):
        if x % 22 == 0:
            print("")
        if numbers.hscore[x] == 1:
            print("[X]", end="")
        else:
            print("[ ]", end="")
    print("")
    time.sleep(1)



def num_con(score):

    numdict={0:numbers.zero,1:numbers.one, 2:numbers.two, 3:numbers.three, 4:numbers.four, 5:numbers.five,
             6:numbers.six, 7:numbers.seven, 8:numbers.eight, 9:numbers.nine}

    digit_three= score//100
    digit_two = (score - digit_three)//10
    digit_one= score-digit_three*100-digit_two*10

    digit_one=numdict[digit_one]
    digit_two=numdict[digit_two]
    digit_three=numdict[digit_three]
    output=[0]*244

    os.system('cls' if os.name == 'nt' else 'clear')
    for x in range(198):
        if digit_one[x]==1:
            output[x+16]=1
        if digit_two[x]==1:
            output[x+8]=1
        if digit_three[x]==1:
            output[x]=1
        if x%22==0:
            print("")
        if  output[x]==1:
            print("[X]",end="")
        else:
            print("[ ]",end="")


    print("")
    time.sleep(2)


def start():

    threading.Thread(target=moving).start()
    position = []
    position.append(STARTING_POINT)
    start=1
    length=0
    allpositions = []
    counter=1
    going=True
    while going!=False:
        if start==1 or hit==1:
            fruits(position)
            start=0
            hit=0
        going=bordercontrol(position,length)
        printfield()


        time.sleep(0.3)
        position=positionupdate(position,length)

        if field[position[0]]=="X":
            length+=1
            lastpos=position[length-1]
            position.append(lastpos)
            fruits(position)


        for pos in position:

            field[pos]=1













