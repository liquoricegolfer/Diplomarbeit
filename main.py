import keyboard
import visuals
import os
import time
import fti
import gts
import chess
import waihff
import board
import neopixel
import RPi.GPIO as GPIO
GPIO.setup(15,GPIO.OUT)
GPIO.output(15,GPIO.HIGH)

SIZE= 242
leds = neopixel.NeoPixel(board.D18, SIZE)

def show_time():
    visuals.time_p()
    while True:
        if time.localtime().tm_sec<=1:
            visuals.time_p()

        if keyboard.is_pressed("enter"):
            break


def game_selection(index,game_list):
    while True:
        if index==-1:
            index=3
        elif index==4:
            index=0
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(11):
            if i % 2 != 0:
                for o in reversed(range(22)):
                    if game_list[o] == 0:
                        leds[o] = (0, 0, 0)
                    else:
                        leds[o] = (255, 0, 0)
            else:
                for o in range(22):
                    if game_list[o] == 0:
                        leds[o] = (0, 0, 0)
                    else:
                        leds[o] = (255, 0, 0)
        time.sleep(0.2)                     #because it can happen that one keystroke is being counted as two
        while True:
            key=keyboard.read_key()
            if key in ["a","d","enter","backspace"]:
                if key=="a":
                    index-=1
                    break
                elif key=="d":
                    index+=1
                    break
                elif key=="backspace":
                    return
                elif key=="enter":
                    if index==0:
                        waihff.start()
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

game_list=[]
game_list.append(visuals.waihff)
game_list.append(visuals.gts)
game_list.append(visuals.fti)
game_list.append(visuals.chess)
while True:
    show_time()
    index = 0
    game_selection(index,game_list)
