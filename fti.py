import keyboard
import random
import os
import visuals
import time
SIZE = 242
COLUMNS=22
STARTING_POSITION=120
ATTEMPTS=3
global field 
global attempts_and_score
global block
field = [0]*SIZE
attempts_and_score=[0]*3
block=[0,1,2,-COLUMNS+2,-COLUMNS+1,-COLUMNS,-COLUMNS*2+2,-COLUMNS*2+1,-COLUMNS*2]

def printfield():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(SIZE):
        if i%(COLUMNS)==0:
            print("")
        if field[i]==0:
            print("[ ]",end="")
        else:
            print("[",field[i],end=" ]")

    print("")


def endscreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    visuals.score_p()
    visuals.num_con(attempts_and_score[1])
    with open("Highscore_fti.txt","r") as highscore:
        h_score=highscore.read()
    if int(h_score) < (attempts_and_score[1]):
        with open("Highscore.txt", "w") as highscore:
            highscore.write(str(attempts_and_score[1]))
        visuals.hscore_p()
        visuals.num_con(attempts_and_score[1])
    else:
        visuals.hscore_p()
        visuals.num_con(int(h_score))
    attempts_and_score[2]=0



def face(position):
    r=random.choice([1,-1,COLUMNS,-COLUMNS])   #directions
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
        target=random.randint(0,SIZE-2)
        if (target+1)%22 !=0 and target%22 !=0 and target-COLUMNS*2>0:#looking for errors of boarders
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
                return COLUMNS
            if key=="w":
                return -COLUMNS
            if key=="enter":
                win=winning(target,searcher)
                if win==True:
                    return 100
                else:
                    return 0
def winning(target,searcher):
    if searcher in [m+target for m in block]:
        visuals.found_p()
        attempts_and_score[0]=ATTEMPTS
        attempts_and_score[1]+=1    #highscore
        return True

    else:
        visuals.X_p()
        if attempts_and_score[0]==0:
            endscreen()
        attempts_and_score[0]-=1
        return False

def start():
    position=STARTING_POSITION
    begining=True
    searcher=STARTING_POSITION
    attempts_and_score[0]=ATTEMPTS-1
    attempts_and_score[1]=0
    attempts_and_score[2]=1
    while attempts_and_score[2]!=0:
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

