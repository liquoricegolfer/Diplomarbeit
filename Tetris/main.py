import random
from pynput.keyboard import Key, Listener
import threading
import time

moving ="m"

def move(key):
    if key == Key.right:
        moving = "r"
        return "r"
    elif key == Key.left:
        return "l"
    elif key == Key.up:
        return "u"
    elif key == Key.down:
        return "d"
    elif key == Key.space:
        return "x"


def print_board(*board):
    board_new = list(board)
    for i in range(100):
        if i%10 == 0:
            print("")
        print(board_new[i], end="")

def thread():
    pass


class blocks:
    def __init__(self,start):
        self.start = start
    def L(self):
        self.being1= self.start
        self.being2 = self.start+10
        self.being3 = self.start+11
        self.being4 = self.start+12

    def Q(self):
        self.being1 = self.start
        self.being2 = self.start + 1
        self.being3 = self.start + 10
        self.being4 = self.start + 11
    def Z(self):
        self.being1 = self.start +1
        self.being2 = self.start + 2
        self.being3 = self.start + 10
        start.being4 = self.start + 11

    def K(self):
        self.being1 = self.start +1
        self.being2 = self.start + 10
        self.being3 = self.start + 11
        self.being4 = self.start + 12

    def I(self):
        self.being1 = self.start +1
        self.being2 = self.start + 2
        self.being3 = self.start + 3
        self.being4 = self.start + 3

def random_block():
    block = ['L','Q','Z','K','I']
    block_random = block[random.randint(0,4)]
    return block_random








def thread_(name):


    while True:
        with Listener(on_press=move) as listener:
            listener.join()








if __name__ == '__main__':
    board = [0] * 200
    x = threading.Thread(target=thread_, args=(1,))
    x.start()

    while True:
        time.sleep(1)
        print_board(*board)

