import keyboard
import threading
import random
import os
import numbers
import time
SIZE = 242
ROWS=22
STARTING_POSITION=120
ATTEMPTS=3
global keyhit
global field
field = [0]*(SIZE+3)   #because of some extra variables
field[SIZE+1]=ATTEMPTS
global mover
global block
block=[0,1,2,-ROWS+2,-ROWS+1,-ROWS,-ROWS*2+2,-ROWS*2+1,-ROWS*2]

def printfield():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(SIZE):
        if i%(ROWS)==0:
            print("")
        if field[i]==0:
            print("[ ]",end="")
        else:
            print("[",field[i],end=" ]")

    print("")

def score_p():
    for x in range(198):
        if x%22==0:
            print("")
        print("[",numbers.score[x],"]",end="")
    print("")
def hscore_p():
    for x in range(198):
        if x%22==0:
            print("")
        print("[",numbers.hscore[x],"]",end="")
    print("")

def num_con(score):

    numdict={0:numbers.zero,1:numbers.one, 2:numbers.two, 3:numbers.three, 4:numbers.four, 5:numbers.five,
             6:numbers.six, 7:numbers.seven, 8:numbers.eight, 9:numbers.nine}

    digit_three= score//100
    digit_two = (score - digit_three)//10
    digit_one= score-digit_three-digit_two

    digit_one=numdict[digit_one]
    digit_two=numdict[digit_two]
    digit_three=numdict[digit_three]
    output=[0]*244

    for x in range(198):
        if digit_one[x]==1:
            output[x+16]="X"
        if digit_two[x]==1:
            output[x+8]="X"
        if digit_three[x]==1:
            output[x]="X"
        if x%22==0:
            print("")
        print("[",output[x],"]",end="")


    print("")

def endscreen(length):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Score:", (length + 1))
    with open("Highscore.txt","r") as highscore:
        score=highscore.read()
    if int(score) < (length + 1):
        with open("Highscore.txt", "w") as highscore:
            length=length+1
            highscore.write(str(length))
            print("Highscore", length)
    else:
        print("Highscore",score)

    quit()

def face(position):
    r=random.choice([1,-1,ROWS,-ROWS])   #directions
    n=0
    while n <=3:
        for x in block:
            field[position+x+r*n]=1
        printfield()
        time.sleep(0.5)
        for x in range(SIZE):
            field[x]=0
        n+=1

def targetposition():
    while True:
        target=random.randint(0,SIZE-1)
        if (target+1)%22 !=0 and target%22 !=0 and target-ROWS*2>0:#looking for errors of boarders
            return target

def searching(searcher,target):
    field[searcher]=2
    printfield()
    while True:
        key=keyboard.read_key()
        if key in ["a","d","s","w","enter"]:
            field[searcher]=0
            if key=="a":
                return -1
            if key=="d":
                return 1
            if key =="s":
                return ROWS
            if key=="w":
                return -ROWS
            if key=="enter":
                win=winning(target,searcher)
                if win==True:
                    return 100
                else:
                    return 0
def winning(target,searcher):
    if searcher in [n+target for n in block]:
        print("won")
        field[SIZE+1]=ATTEMPTS
        field[SIZE+2]+=1    #highscore
        return True

    else:
        print("lost")
        if field[SIZE+1]==0:
            print(f"Your highscore is: {field[SIZE+2]}")
            quit()
        field[SIZE+1]-=1
        return False

def start():
    position=STARTING_POSITION
    begining=True
    searcher=STARTING_POSITION
    while True:
        if begining == True:
            face(position)
            printfield()
            begining=False
            target=targetposition()

        x=searching(searcher,target)
        if x==100:
            begining=True
        else:
            searcher+=x
        time.sleep(0.2)    #there to fix a bug, otherwise every key gets interpreted as pressed twice

