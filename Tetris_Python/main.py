import keyboard
import threading
import random
import os
size = 200
import time


global field
field = [0]*(size*2)

global position
position=[0]*4


def printfield():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(size):
        if i%(10)==0:
            print("")
        print(field[i],end="")

    print("")



def moving():
    mover=1
    while True:

        if keyboard.is_pressed("s"):
            move(position)
        elif keyboard.is_pressed("a"):
            oldposition = list(position)
            for i in range(4):

                position[i]-=1
            fieldupdate(position,oldposition)
            printfield()
        elif keyboard.is_pressed("d"):
            oldposition = list(position)
            for i in range(4):
                position[i] += 1

            oldposition=fieldupdate(position, oldposition)
            printfield()


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
        print("Highscoe",score)

    quit()

def positionupdate(position,length):

    if length>0:
        field[position[length]]=0
        for i in reversed(range(length)):
            position[i+1] = position[i]
    else:
        field[position[0]]=0
    if field[position[0]+field[200]]==1:
        endscreen(length)
    else:
        position[0]=position[0]+field[200]

    #for number in range(length+1):
        #position[number]=position[number]
    for number in reversed(range(length+1)):
        x=field[200]
        field[200+number]=field[200+number+1]
        field[200]=x
    return position

def bordercontrol(position,length):
    for i in range(10):
        if position[0] <0 or position[0] >199:
            endscreen(length)


        elif field[200]==1:
            for next in range(1,10):
                if position[0]==20*next:
                    endscreen(length)
        elif field[200]==-1:
            for next in range(1,10,2):
                if position[0]==10*next+9:
                    endscreen(length)



def blocks(block,position):

    if block== "Katsushiro":
        position=[3,4,5,6]
    elif blocks == "Gorobei":
        position=[3,13,14,15]
    elif block == "Heihachi":
        position = [13, 14, 15,5]
    elif block == "Kyuzo":
        position = [3, 4, 13, 14]
    elif block == "Shichiroji":
        position = [13, 4, 14, 5]
    elif block == "Kikuchiyo":
        position = [13, 4, 14, 15]
    elif block == "Kambi":
        position = [3, 4, 14, 15]
    return position

def randomblock():
    blocks=["Katsushiro","Gorobei","Heihachi","Kyuzo","Shichiroji","Kikuchiyo","Kambi"]
    block = random.choice(blocks)
    return block
def move(position):
    for i in range(4):
        position[i]+=10

    return position
def fieldupdate(position,oldposition):
    for pos in position:
        field[pos]=1
        if (pos-10)not in position and pos>9:
            field[pos-10]=0
    for pos in oldposition:
        if pos not in position:
            field[pos]=0

    oldposition = list(position)

    return oldposition

def lastline(fixedblocks):
    lastline=all(number in fixedblocks for number in range(190,199))
    if lastline==True:
        for i in range(190,191):
            fixedblocks.remove(i)
            field[i]=0
        for i in range(len(fixedblocks)):
            fixedblocks[i]+=10
            field[fixedblocks[i]]=1

    else:
        pass


if __name__ == '__main__':


    threading.Thread(target=moving).start()
    oldposition=[0,0,0,0]
    fixedblocks=[]
    while True:
        block=randomblock()
        position=blocks(block,position)
        finished=0
        while True:
            oldposition=fieldupdate(position,oldposition)
            printfield()
            time.sleep(0.1)
            for final in range(4):
                if position[final]>=190:
                    finished=1
                    oldposition=[0,0,0,0]
                elif (position[final]+10) in fixedblocks:
                    finished = 1
                    oldposition = [0, 0, 0, 0]

            lastline(fixedblocks)
            if finished==1:
                for i in range(4):
                    fixedblocks.append(position[i])
                print(fixedblocks)
                break
            move(position)













