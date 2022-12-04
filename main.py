import keyboard
import visuals
import os
import time
import fti
import gts
import chess
import snake


game_list=[]
game_list.append(visuals.snake)
game_list.append(visuals.gts)
game_list.append(visuals.fti)
game_list.append(visuals.chess)
index=0

visuals.time_p()
while True:
    if time.localtime().tm_sec<=1:
        visuals.time_p()

    if keyboard.is_pressed("enter"):
        break


while True:
    if index==-1:
        index=3
    elif index==4:
        index=0
    os.system('cls' if os.name == 'nt' else 'clear')
    for x in range(242):
        if x%22==0:
            print("")
        if game_list[index][x]==1:
            print("[X]",end="")
        else:
            print("[ ]", end="")
    time.sleep(0.2)                     #because it can happen that one keystroke is being counted as two
    while True:
        key=keyboard.read_key()
        if key in ["a","d","enter"]:
            if key=="a":
                index-=1
                break
            elif key=="d":

                index+=1
                break
            elif key=="enter":
                if index==0:
                    snake.start()
                    break
                elif index==1:
                    gts.start()
                    break
                elif index==2:
                    fti.start()
                    break
                elif index==3:
                    chess.start()
                    break
