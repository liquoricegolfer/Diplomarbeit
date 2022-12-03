import keyboard
import random
import os
import time
import numbers
SIZE = 242
ROWS = 22
STARTING_POSITION = 120
global field
field = [0]*(SIZE*2)
global mover

def printfield():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(SIZE):
        if i%ROWS==0:
            print("")
        if field[i]==1:
            print("[X]",end="")
        else:
            print("[ ]",end="")

    print("")

def randomsquare(path):
    way=[ROWS,-ROWS,1,-1]
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


def choice(previous_choice,path,pos,score):
    while True:
        key=keyboard.read_key()
        if key in ["a","d","s","w"]:
            if key=="a":
                if pos-1 in path and pos-1 != previous_choice:
                    return pos-1
                else:                   #bug fix
                    endscreen(score)
                    return False
            if key=="d":
                if pos + 1 in path and pos + 1 != previous_choice:
                    return pos + 1
                else:                   #bug fix
                    endscreen(score)
            if key =="s":
                if pos + ROWS in path and pos + ROWS != previous_choice:
                    return pos + ROWS
                else:                   #bug fix
                    endscreen(score)
                    return False
            if key=="w":
                if pos - ROWS in path and pos - ROWS != previous_choice:
                    return pos - ROWS
                else:
                    endscreen(score)
                    return False



def score_p():
    for x in range(198):
        if x%22==0:
            print("")
        if numbers.score[x]==1:
            print("[X]",end="")
        else:
            print("[ ]",end="")
    print("")
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







def endscreen(score):
    os.system('cls' if os.name == 'nt' else 'clear')
    score_p()
    time.sleep(1)
    num_con(int(score-1))
    time.sleep(2)
    with open("highscore_gts.txt","r") as highscore:
        score_old=highscore.read()
    if int(score_old) < score-1:
        with open("highscore_gts.txt", "w") as highscore:
            highscore.write(str(score-1))
            print("sdfdsfdsf")
        hscore_p()
        time.sleep(1)
        num_con(score-1)
        time.sleep(2)
    else:
        hscore_p()
        time.sleep(1)
        num_con(int(score_old))
        time.sleep(2)








def start():
    path = []
    path.append(STARTING_POSITION)
    score = 0
    pos=True
    while pos!=False:           #as long as the endscreen did'nt happen yet
        score+=1
        path = randomsquare(path)
        path_to_field(path,True,score)
        pos = STARTING_POSITION
        n=1
        previous_pos = STARTING_POSITION

        while n<=score and pos!=False:
            path_to_field(path,False,n)
            printfield()
            temporary_pos=pos
            pos=choice(previous_pos,path,pos,score)
            previous_pos=temporary_pos
            print(n)
            n+=1
            time.sleep(0.2)                         #because it sometimes registers a keypress twice

