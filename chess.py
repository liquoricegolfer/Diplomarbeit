import keyboard
import time
import os
import board
import neopixel
import RPi.GPIO as GPIO
GPIO.setup(15,GPIO.OUT)
GPIO.output(15,GPIO.HIGH)

SIZE = 242
COLUMNS=22
global board
global board_choice
board=[0]*64
global Pawn_w,Pawn_b,Pawn_start_w,Pawn_start_b, Rook_w, Rook_b,Knight_w, Knight_b, Bishop_w,Bishop_b, Queen_w, Queen_b, King_w, King_b,white_pieces,black_pieces, mate_and_quit

leds = neopixel.NeoPixel(board.D18, SIZE)

mate_and_quit=[0,0]
Pawn_w = [1, 9, 17, 25, 33, 41, 49, 57]
Pawn_b = [x + 5 for x in Pawn_w]
Rook_w = [0, 56]
Rook_b = [7, 63]
Knight_w = [8, 48]
Knight_b = [15, 55]
Bishop_w = [16, 40]
Bishop_b = [23, 47]
Queen_w, Queen_b, King_w, King_b = [24], [31], [32], [39]           #Queens are lists because there can be more than one
Pawn_start_w=list(Pawn_w)
Pawn_start_b=list(Pawn_b)
white_pieces=[]
black_pieces=[]

def printfield(b):
    os.system('cls' if os.name == 'nt' else 'clear')
    x=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
       0, 0, 0, 0, 0, 0, 0, b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, b[8], b[9], b[10], b[11], b[12], b[13], b[14], b[15], 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, b[16], b[17], b[18], b[19], b[20], b[21], b[22], b[23], 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, b[24], b[25], b[26], b[27], b[28], b[29], b[30], b[31], 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, b[32], b[33], b[34], b[35], b[36], b[37], b[38], b[39], 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, b[40], b[41], b[42], b[43], b[44], b[45], b[46], b[47], 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, b[48], b[49], b[50], b[51], b[52], b[53], b[54], b[55], 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, b[56], b[57], b[58], b[59], b[60], b[61], b[62], b[63], 0, 0, 0, 0, 0, 0, 0,
       ]
    for i in range(SIZE):
        if x[i] == 0:
            leds[i] = (0, 0, 0)
        else:
            leds[i] = (255, 0, 0)

def board_update():
    white_pieces.clear()
    black_pieces.clear()

    for n in range(64):
        board[n]=0

    for piece in Pawn_w:
        board[piece]="1"
        white_pieces.append(piece)
    for piece in Pawn_b:
        board[piece]="2"
        black_pieces.append(piece)
    for piece in Rook_w:
        board[piece]="5"
        white_pieces.append(piece)
    for piece in Rook_b:
        board[piece]="6"
        black_pieces.append(piece)
    for piece in Knight_w:
        board[piece]="3"
        white_pieces.append(piece)
    for piece in Knight_b:
        board[piece]="4"
        black_pieces.append(piece)
    for piece in Bishop_w:
        board[piece]="7"
        white_pieces.append(piece)
    for piece in Bishop_b:
        board[piece]="8"
        black_pieces.append(piece)
    for piece in Queen_w:
        board[piece] = "Q"
        white_pieces.append(piece)
    for piece in Queen_b:
        board[piece] = "W"
        black_pieces.append(piece)
    board[King_w[0]] = "K"
    white_pieces.append(King_w[0])
    board[King_b[0]] = "K"
    white_pieces.append(King_b[0])



def move_choice(n):
    position=COLUMNS
    selected=[]
    correct=False
    while True:
        time.sleep(0.2)
        key = keyboard.read_key()
        if key in ["a", "d", "s", "w","enter","backspace"]:
            if key == "a" and position>0 and position%8!=0:
                position=square_selection(position-1)
            if key == "d" and position<63 and position%8!=7:
                position=square_selection(position+1)
            if key == "s" and position<56:
                position=square_selection(position+8)
            if key == "w" and position>8:
                position=square_selection(position-8)
            if key == "enter":
                selected.append(position)
                if len(selected)==2:
                    correct=check(selected,n)
                    if correct==True:
                        board_update()
                        break
                    selected = []
            if key=="backspace":
                mate_and_quit[1]=1
                break

def square_selection(position):
    board_choice=list(board)
    board_choice[position]="X"
    printfield(board_choice)
    return position


def Pawn(selected,pawn,pawn_start,factor,n):
    if selected[1]==selected[0]+factor and board[selected[1]]==0:
        try: n=pawn.index(selected[0])
        except: return False
        pawn[n] = selected[1]
        return True
    elif selected[1] == selected[0] + 2*factor and selected[0] in pawn_start and board[selected[1]]==0:
        x = pawn.index(selected[0])
        pawn[x] = selected[1]
        return True
    elif (selected[1]==selected[0]+9*factor or selected[1]==selected[0]-7*factor):
        if n%2!=0:
            if Capture(Pawn_w, selected, n) == True:
                return True
            else:
                return False
        else:
            if Capture(Pawn_b,selected,n)==True:
                return True                     #is there something on this square? Have we captured it?
            else:
                return False
    else:
        return False

def Rook(rook,selected,n):
    legal_move=False
    if (-7<=(selected[1]-selected[0])<=7) and selected[1]//10==selected[0]//10: #is it a straight row and are they in the same row?

        for x in range(selected[0]+1,selected[1]):        #is there a piece in the path?
            if board[x] != 0:

                return False
            legal_move=True

    elif (selected[1]-selected[0])%8==0:

        y=(selected[1]-selected[0])//8  +1

        for x in range(1,y): #is there a piece in the path?
            if board[selected[0]+x*8]!=0:

                return False
            legal_move=True

    if n%2!=0:
        if Capture(Rook_w,selected,n)==True:
            return True
    elif n%2==0:
        if Capture(Rook_b, selected, n) == True:
            return True
    if legal_move==True:
        x = rook.index(selected[0])
        crook=rook.copy()
        rook[x] = selected[1]
        if Check_and_Mate(1)==False:
            return True
        else:
            rook=crook.copy()
        return True
    return False


def Bishop(bishop, selected,n):
    legal_move=False
    if (selected[1] - selected[0]) % 7 == 0:

        s=selected[0]
        for x in range(1,(selected[1]-selected[0])//7):
            s+=7
            print(s)
            if board[s]!= 0:
                return False

        legal_move=True

    elif (selected[1] - selected[0]) % 9 == 0:
        s=selected[0]
        for x in range(1,(selected[1]-selected[0])//9):
            s+=9
            if board[s]!= 0:
                return False
        legal_move=True
    if n % 2 != 0:
        if Capture(Bishop_w, selected, n) == True:
            return True
    elif n % 2 == 0:
        if Capture(Bishop_b, selected, n) == True:
            return True
    if legal_move==True:
        x = bishop.index(selected[0])
        bishop[x] = selected[1]
        return True

    return False


def Knight(knight,selected,n):
    if selected[1]==selected[0]+10 or selected[1]==selected[0]-10 or selected[1]==selected[0]+6 or selected[1]==selected[0]+6 or selected[1]==selected[0]+17 or selected[1]==selected[0]-17 or selected[1]==selected[0]+15 or selected[1]==selected[0]-15:
        if n % 2 != 0:
            if Capture(Knight_w, selected, n) == True:
                return True
        elif n % 2 == 0:
            if Capture(Knight_b, selected, n) == True:
                return True
        x = knight.index(selected[0])
        knight[x] = selected[1]
        return True
    return False


def Capture(piece,selected,n):
    if n%2!=0:                              #capture the black piece, ... if there is one
        if selected[1] in Pawn_b:
            Pawn_b.remove(selected[1])
            x=piece.index(selected[0])
            piece[x]=selected[1]
            return True
        elif selected[1] in Rook_b:
            Rook_b.remove(selected[1])
            x=piece.index(selected[0])
            piece[x]=selected[1]
            return True
        elif selected[1] in Knight_b:
            Knight_b.remove(selected[1])
            x=piece.index(selected[0])
            piece[x]=selected[1]
            return True
        elif selected[1] in Bishop_b:
            Bishop_b.remove(selected[1])
            x=piece.index(selected[0])
            piece[x]=selected[1]
            return True
        elif selected[1] in Queen_b:
            Queen_b.remove(selected[1])
            x = piece.index(selected[0])
            piece[x] = selected[1]
            return True

        else:
            return False

    if n%2==0:                          #capture the white piece, ... if there is one
        if selected[1] in Pawn_w:
            Pawn_w.remove(selected[1])
            x=piece.index(selected[0])
            piece[x]=selected[1]
            return True
        elif selected[1] in Rook_w:
            Rook_w.remove(selected[1])
            x=piece.index(selected[0])
            piece[x]=selected[1]
            return True
        elif selected[1] in Knight_w:
            Knight_w.remove(selected[1])
            x=piece.index(selected[0])
            piece[x]=selected[1]
            return True
        elif selected[1] in Bishop_w:
            Bishop_w.remove(selected[1])
            x=piece.index(selected[0])
            piece[x]=selected[1]
            return True
        elif selected[1] in Queen_w:
            Queen_w.remove(selected[1])
            x = piece.index(selected[0])
            piece[x] = selected[1]
            return True
        else:
            return False

def check(selected,n):

    if n%2!=0 and friendly_fire(selected[1],n)==False:

        if selected[0] in Pawn_w:
            if Pawn(selected,Pawn_w,Pawn_start_w,1,n)==True:
                return True
        elif selected[0] in Rook_w:
            if Rook(Rook_w,selected,n)==True:
                return True
        elif selected[0] in Bishop_w:
            if Bishop(Bishop_w,selected,n)==True:
                return True
        elif selected[0] in Knight_w:
            if Knight(Knight_w,selected,n)==True:
                return True
        elif selected[0] in Queen_w:            #because a Queen is just a combination of Rook and a Bishop
            if Bishop(Queen_w,selected,n)==True:
                return True
            elif Rook(Queen_w,selected,n)==True:
                return True

        elif selected[0] == King_w[0]:
            if selected[1] == 0 and 0 in Rook_w:
                i=Rook.index(0)
                Rook[i]=24
                King_w[0]=16
            if Capture(King_w,selected,n)==True:
                return True
            else:
                King_w[0]=selected[1]
                return True
        else:

            return False

    if n%2 ==0 and friendly_fire(selected,n)==False:             #move black
        if Pawn(selected, Pawn_b, Pawn_start_b,-1,n)==True:
            return True
        elif selected[0] in Rook_b:
            if Rook(Rook_b,selected,n)==True:
                return True
        elif selected[0] in Bishop_b:
            if Bishop(Bishop_b,selected,n)==True:
                return True
        elif selected[0] in Knight_b:
            if Knight(Knight_b, selected, n) == True:
                return True
        elif selected[0] in Queen_b:            #because a Queen is just a combination of Rook and a Bishop
            if Bishop(Queen_b,selected,n)==True:
                return True
            elif Rook(Queen_b,selected,n)==True:
                return True
        elif selected[0] == King_b[0]:
            if Capture(King_b,selected,n)==True:
                return True
            else:
                King_b[0]=selected[1]
                return True

        else:
            return False

def friendly_fire(square,n):
    if n%2!=0:
        if square in white_pieces:
            return True
        else:
            return False
    elif n%2==0:
        if square in black_pieces:
            return True
        else:
            return False

def Check_and_Mate(n):              #if a piece aligns with a king, then
    if n%2!=0:
        print("inside the checking system")
        for bishop in Bishop_b:
            print("in")
            print(bishop)
            a = [bishop]*4
            for x in range(7):
                if (a[0] +9)%8!=0 and a[0]%8!=7:   #should not go through the border
                    a[0]+=9
                if (a[1] +7)%8!=0 and a[1]%8!=7:
                    a[1]+=7
                a[2]-=9
                a[3]-=7
                print(a)
                if King_w[0] in a :
                    print(a)
                    print("So... you are in check right now")
                    return True
                for y in range(len(a)):
                    if 0<=a[y]<64:
                        if board[a[y]]!=0:
                            a[y]=-100
    return False


def start():
    n=1
    mate_and_quit = [0, 0]
    Pawn_w = [1, 9, 17, 25, 33, 41, 49, 57]
    Pawn_b = [x + 5 for x in Pawn_w]
    Rook_w = [0, 56]
    Rook_b = [7, 63]
    Knight_w = [8, 48]
    Knight_b = [15, 55]
    Bishop_w = [16, 40]
    Bishop_b = [23, 47]
    Queen_w, Queen_b, King_w, King_b = [24], [31], [32], [39]
    while mate_and_quit[1]==0:
        board_update()
        printfield(board)
        move_choice(n)
        n+=1


