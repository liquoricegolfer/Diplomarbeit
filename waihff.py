import keyboard
import threading
import random
import os
import visuals
import time

SIZE = 242
COLUMNS=22
STARTING_POINT=120
global field
global mover
global end
field = [0]*SIZE
mover=[0]
end=[0]


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

def food(position):
    foodposition = random.randint(0, SIZE-1)
    while foodposition in position:
        foodposition = random.randint(0, SIZE-1)
    field[foodposition]=2


def moving():
    while True:
        key=keyboard.read_key()
        if key in ["a","d","s","w"]:
            if key=="w":
                mover[0] = -22
            if key == "s":
                mover[0] = 22
            if key == "a":
                mover[0] = -1
            if key == "d":
                mover[0]=1
def endscreen(length):
    os.system('cls' if os.name == 'nt' else 'clear')
    end[0]=1
    visuals.score_p()
    visuals.num_con(length+1)
    with open("highscore_snake.txt","r") as highscore:
        score=highscore.read()
    if int(score) < (length + 1):
        with open("highscore_snake.txt", "w") as highscore:
            length=length+1
            highscore.write(str(length))
            visuals.hscore_p()
            visuals.num_con(length+1)
    else:
        visuals.hscore_p()
        visuals.num_con(int(score))


def positionupdate(position,length):
    if length>0:
        field[position[length]]=0
        for i in reversed(range(length)):
            position[i+1] = position[i]
    else:
        field[position[0]]=0
    try:
        if field[position[0]+mover[0]]==1:
            endscreen(length)
            return False
    except:
        endscreen(length)
    else:
        position[0]=position[0]+mover[0]

    return position

def bordercontrol(position,length):
    if position[0] < 0 or position[0] > SIZE - 1:
        endscreen(length)
        return False

    elif mover[0]==1:
        for next in range(1,COLUMNS):
            if position[0]==22*next:
                endscreen(length)
                return False

    elif mover[0]==-1:
        for next in range(1,COLUMNS,2):
            if position[0]==COLUMNS*next+COLUMNS-1:
                endscreen(length)
                return False

def start():
    threading.Thread(target=moving).start()
    for i in range(SIZE):
        field[i]=0
    position = [STARTING_POINT]
    beginning=True
    length=0
    going=True
    end[0]=0
    while True:
        if beginning==True:
            food(position)
            beginning=False

        going=bordercontrol(position,length)
        printfield()
        time.sleep(0.3)
        position=positionupdate(position,length)
        if end[0]==1:
            break
        if field[position[0]]==2:
            length+=1
            lastpos=position[length-1]
            position.append(lastpos)
            food(position)

        for pos in position:
            field[pos]=1