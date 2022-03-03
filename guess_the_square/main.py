import keyboard
import threading
import random
import os
size = 200
import time


global field
field = [0]*(size*2)
global mover

def printfield():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(size):
        if i%(20)==0:
            print("")
        print(field[i],end="")

    print("")

def randomsquare(path):
    choice=[20,-20,1,-1]
    while True:
        next=random.choice(choice)
        if next in path:
            next = random.choice(choice)
        else:
            path.append(path[len(path) - 1] + next)
            break

    return path



def moving():
    mover=1
    while True:
        if keyboard.read_key()=="w":
            field[200] = -20
        if keyboard.read_key() == "s":
            field[200] = 20
        if keyboard.read_key() == "a":
            field[200] = -1
        if keyboard.read_key() == "d":
            field[200]=1

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
    if keyboard.read_key()=="w":
        return -20
    elif keyboard.read_key() =="s":
        return 20
    elif keyboard.read_key() =="d":
        return 1
    elif keyboard.read_key() =="a":
        return -1


def squareguessing(path):

    square =90
    counter =0
    for step in path:
        n=0
        counter+=1
        if counter !=1:
            while n==0:
                keys =key()
                square= square+keys
                if square == step:
                    field[step]=1
                    printfield()
                    n=1
                else:
                    print(square)
                    endscreen()
    for step in path:
        field[step]=0
    printfield()







if __name__ == '__main__':



    path=[90]
    field[90]=1

    while True:
        path=randomsquare(path)
        print(path)
        lightup(path)
        squareguessing(path)







