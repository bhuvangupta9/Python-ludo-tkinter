from tkinter import *  # Tkinter is used as the GUI.
import random
root = Tk()

canvas = Canvas(width = 1200, height = 800, bg = 'yellow')
root.resizable(width=False, height=False)

canvas.pack(expand = YES, fill = BOTH)

gif1 = PhotoImage(file = 'ludo board.gif')
canvas.create_image(50, 10, image = gif1, anchor = NW)

player1 = PhotoImage(file="blue.gif")
player2 = PhotoImage(file="green.gif")

b2 = Label(image=player1, width=20, height=20)
b3 = Label(image=player1, width=20, height=20)
b4 = Label(image=player1, width=20, height=20)

g1 = Label(image=player2, width=20, height=20)
g2 = Label(image=player2, width=20, height=20)
g3 = Label(image=player2, width=20, height=20)
g4 = Label(image=player2, width=20, height=20)

bluex1 = (100, 357, 357, 357, 357, 357, 305, 260, 215, 170, 125,  80,  80,  80, 125, 170, 215, 260, 305, 357, 357, 357, 357, 357, 357, 405, 450, 450, 450, 450, 450, 450, 495, 540, 585, 630, 675, 720, 720, 720, 675, 630, 585, 540, 495, 450, 450, 450, 450, 450, 450, 405, 405, 405, 405, 405, 405, 405)
bluey1 = (650, 645, 595, 545, 499, 453, 408, 408, 408, 408, 408, 408, 360, 315, 315, 315, 315, 315, 315, 270, 225, 180, 135,  85,  40,  40,  40,  85, 130, 180, 225, 270, 315, 315, 315, 315, 315, 315, 360, 408, 408, 408, 408, 408, 408, 450, 498, 545, 589, 638, 685, 685, 640, 595, 550, 499, 455, 405)
bluex2 = (100, 357, 357, 357, 357, 357, 305, 260, 215, 170, 125,  80,  80,  80, 125, 170, 215, 260, 305, 357, 357, 357, 357, 357, 357, 410, 450, 450, 450, 450, 450, 450, 495, 540, 585, 630, 675, 720, 720, 720, 675, 630, 585, 540, 495, 450, 450, 450, 450, 450, 450, 405, 405, 405, 405, 405, 405, 405)
bluey2 = (550, 645, 595, 545, 499, 453, 408, 408, 408, 408, 408, 408, 360, 315, 315, 315, 315, 315, 315, 270, 225, 180, 135,  85,  40,  40,  40,  85, 130, 180, 225, 270, 315, 315, 315, 315, 315, 315, 360, 408, 408, 408, 408, 408, 408, 450, 498, 545, 589, 638, 685, 685, 640, 595, 550, 499, 455, 405)
bluex3 = (200, 357, 357, 357, 357, 357, 305, 260, 215, 170, 125,  80,  80,  80, 125, 170, 215, 260, 305, 357, 357, 357, 357, 357, 357, 410, 450, 450, 450, 450, 450, 450, 495, 540, 585, 630, 675, 720, 720, 720, 675, 630, 585, 540, 495, 450, 450, 450, 450, 450, 450, 405, 405, 405, 405, 405, 405, 405)
bluey3 = (650, 645, 595, 545, 499, 453, 408, 408, 408, 408, 408, 408, 360, 315, 315, 315, 315, 315, 315, 270, 225, 180, 135,  85,  40,  40,  40,  85, 130, 180, 225, 270, 315, 315, 315, 315, 315, 315, 360, 408, 408, 408, 408, 408, 408, 450, 498, 545, 589, 638, 685, 685, 640, 595, 550, 499, 455, 405)
bluex4 = (200, 357, 357, 357, 357, 357, 305, 260, 215, 170, 125,  80,  80,  80, 125, 170, 215, 260, 305, 357, 357, 357, 357, 357, 357, 410, 450, 450, 450, 450, 450, 450, 495, 540, 585, 630, 675, 720, 720, 720, 675, 630, 585, 540, 495, 450, 450, 450, 450, 450, 450, 405, 405, 405, 405, 405, 405, 405)
bluey4 = (550, 645, 595, 545, 499, 453, 408, 408, 408, 408, 408, 408, 360, 315, 315, 315, 315, 315, 315, 270, 225, 180, 135,  85,  40,  40,  40,  85, 130, 180, 225, 270, 315, 315, 315, 315, 315, 315, 360, 408, 408, 408, 408, 408, 408, 450, 498, 545, 589, 638, 685, 685, 640, 595, 550, 499, 455, 405)

greenx1 = (650, 450, 450, 450, 450, 450, 495, 540, 585, 630, 675, 720, 720, 720, 675, 630, 585, 540, 495, 450, 450, 450, 450, 450, 450, 405, 360, 357, 357, 357, 357, 357, 305, 260, 215, 170, 125,  80,  80,  80, 125, 170, 215, 260, 305, 357, 357, 357, 357, 357, 357, 405, 405, 405, 405, 405, 405, 405)
greeny1 = (100,  85, 130, 180, 225, 270, 315, 315, 315, 315, 315, 315, 360, 408, 408, 408, 408, 408, 408, 450, 498, 545, 589, 638, 685, 685, 685, 645, 595, 545, 499, 453, 408, 408, 408, 408, 408, 408, 360, 315, 315, 315, 315, 315, 315, 270, 225, 180, 135,  85,  40,  40,  85, 130, 175, 225, 270, 315)
greenx2 = (550, 450, 450, 450, 450, 450, 495, 540, 585, 630, 675, 720, 720, 720, 675, 630, 585, 540, 495, 450, 450, 450, 450, 450, 450, 405, 360, 357, 357, 357, 357, 357, 305, 260, 215, 170, 125,  80,  80,  80, 125, 170, 215, 260, 305, 357, 357, 357, 357, 357, 357, 405, 405, 405, 405, 405, 405, 405)
greeny2 = (100,  85, 130, 180, 225, 270, 315, 315, 315, 315, 315, 315, 360, 408, 408, 408, 408, 408, 408, 450, 498, 545, 589, 638, 685, 685, 685, 645, 595, 545, 499, 453, 408, 408, 408, 408, 408, 408, 360, 315, 315, 315, 315, 315, 315, 270, 225, 180, 135,  85,  40,  40,  85, 130, 175, 225, 270, 315)
greenx3 = (650, 450, 450, 450, 450, 450, 495, 540, 585, 630, 675, 720, 720, 720, 675, 630, 585, 540, 495, 450, 450, 450, 450, 450, 450, 405, 360, 357, 357, 357, 357, 357, 305, 260, 215, 170, 125,  80,  80,  80, 125, 170, 215, 260, 305, 357, 357, 357, 357, 357, 357, 405, 405, 405, 405, 405, 405, 405)
greeny3 = (200,  85, 130, 180, 225, 270, 315, 315, 315, 315, 315, 315, 360, 408, 408, 408, 408, 408, 408, 450, 498, 545, 589, 638, 685, 685, 685, 645, 595, 545, 499, 453, 408, 408, 408, 408, 408, 408, 360, 315, 315, 315, 315, 315, 315, 270, 225, 180, 135,  85,  40,  40,  85, 130, 175, 225, 270, 315)
greenx4 = (550, 450, 450, 450, 450, 450, 495, 540, 585, 630, 675, 720, 720, 720, 675, 630, 585, 540, 495, 450, 450, 450, 450, 450, 450, 405, 360, 357, 357, 357, 357, 357, 305, 260, 215, 170, 125,  80,  80,  80, 125, 170, 215, 260, 305, 357, 357, 357, 357, 357, 357, 405, 405, 405, 405, 405, 405, 405)
greeny4 = (200,  85, 130, 180, 225, 270, 315, 315, 315, 315, 315, 315, 360, 408, 408, 408, 408, 408, 408, 450, 498, 545, 589, 638, 685, 685, 685, 645, 595, 545, 499, 453, 408, 408, 408, 408, 408, 408, 360, 315, 315, 315, 315, 315, 315, 270, 225, 180, 135,  85,  40,  40,  85, 130, 175, 225, 270, 315)

bx1, bx2, bx3, bx4 = 0, 0, 0, 0
gx1, gx2, gx3, gx4 = 0, 0, 0, 0
b1 = Label(image=player1, width=20, height=20)
b1.place(x=bluex1[0], y=bluey1[0])

l2 = Label(root, text="Blue's Turn", fg='Black', background='green', font=("Arial", 24, "bold"))
l3 = Label(root, text="Green's Turn", fg='Black', background='green', font=("Arial", 24, "bold"))

flag = 1
turn = 1
die = 0

sixt = 0




def wincheck():
    global bx2, bx3, bx4, bx1, gx1, gx2, gx3, gx4
    if(bx1 == 57) & (bx2 == 57) & (bx3 == 57) & (bx4 == 57):
        L1 = Label(root, text='Blue Won', fg='Black', background='green', font=("Arial", 32, "bold"))
        L1.place(x=800, y=300)
        return 0

    elif(gx1 == 57) & (gx2 == 57) & (gx3 == 57) & (gx4 == 57):
        L1 = Label(root, text='Blue Won', fg='Black', background='green', font=("Arial", 32, "bold"))
        L1.place(x=800, y=300)
        return 0
    else:
        return 1


def playerpos():
    global bx2, bx3, bx4, bx1, gx1, gx2, gx3, gx4, b1, b2, b3, b4, g1, g2, g3, g4, bluex1, bluex2, bluex3, bluex4, bluey1, bluey2, bluey3, bluey4, greenx1, greenx2, greenx3, greenx4, greeny1, greeny2, greeny3, greeny4
    b1.place(x=bluex1[bx1], y=bluey1[bx1])
    b2.place(x=bluex2[bx2], y=bluey2[bx2])
    b3.place(x=bluex3[bx3], y=bluey3[bx3])
    b4.place(x=bluex4[bx4], y=bluey4[bx4])

    g1.place(x=greenx1[gx1], y=greeny1[gx1])
    g2.place(x=greenx2[gx2], y=greeny2[gx2])
    g3.place(x=greenx3[gx3], y=greeny3[gx3])
    g4.place(x=greenx4[gx4], y=greeny4[gx4])
    print(bx1)
    return


def selectcheck(x):
    global die, bx2, bx3, bx4, bx1, gx1, gx2, gx3, gx4
    global btn1, btn2, btn3, btn4
    if die == 6:
        if turn == 1:
            if x == 1:
                if bx1 == 0:
                    bx1=bx1+1
                else:
                    bx1=bx1+6
            elif x == 2:
                if bx2 == 0:
                    bx1=bx1+1
                else:
                    bx2=bx2+6
            elif x == 3:
                if bx3 == 0:
                    bx3=bx3+1
                else:
                    bx3=bx3+6
            elif x == 4:
                if bx4 == 0:
                    bx4=bx4+1
                else:
                    bx4=bx4+6
        else:
            if x == 1:
                if gx1 == 0:
                    gx1=gx1+1
                else:
                    gx1=gx1+6
            elif x == 2:
                if gx2 == 0:
                    gx2=gx2+1
                else:
                    gx2=gx2+6
            elif x == 3:
                if gx3 == 0:
                    gx3=gx3+1
                else:
                    gx3=gx3+6
            elif x == 4:
                if gx4 == 0:
                    gx4=gx4+1
                else:
                    gx4=gx4+6
    else:
        if turn == 1:
            if x == 1:
                if bx1>0:
                    bx1=bx1+die
            elif x == 2:
                if bx2>0:
                    bx1=bx1+die
            elif x == 3:
                if bx3 > 0:
                    bx3=bx3+die
            elif x == 4:
                if bx4 > 0:
                    bx4=bx4+die
        else:
            if x == 1:
                if gx1 > 0:
                    gx1=gx1+die
            elif x == 2:
                if gx2 > 0:
                    gx2=gx2+die
            elif x == 3:
                if gx3 == 0:
                    gx3=gx3+die
            elif x == 4:
                if gx4 == 0:
                    gx4=gx4+die
    btn1.place(x=1000, y=1000)
    btn2.place(x=1000, y=1000)
    btn3.place(x=1000, y=1000)
    btn4.place(x=1000, y=1000)
    playerpos()



def playerselect():
    global btn1, btn2, btn3, btn4, sixt
    if turn == 1:
        if bx1+die <= 57:
            btn1.place(x=800, y=500)
        if bx2+die <= 57:
            btn2.place(x=800, y=550)
        if bx3+die <= 57:
            btn3.place(x=800, y=600)
        if bx4+die <= 57:
            btn4.place(x=800, y=650)
    elif turn == 2:
        if gx1+die <= 57:
            btn1.place(x=800, y=500)
        if gx2+die <= 57:
            btn2.place(x=800, y=550)
        if gx3+die <= 57:
            btn3.place(x=800, y=600)
        if gx4+die <= 57:
            btn4.place(x=800, y=650)

    if die == 6:
        sixt=sixt+1
        rll()

def rll():
    global sixt
    if sixt < 3:
        global bx2, bx3, bx4, bx1, die
        dice = 6
        #dice = random.randint(1, 7)
        L1 = Label(root, text=dice, fg='Black', background='green', font=("Arial", 24, "bold"))
        L1.place(x=800, y=200)
        die = dice
        playerselect()
    else:
        return


btn1 = Button(root, text="  P1   ", relief="raised", font=("Arial", 12), command="selectcheck(1)")
btn2 = Button(root, text="  P2   ", relief="raised", font=("Arial", 12), command="selectcheck(2)")
btn3 = Button(root, text="  P3   ", relief="raised", font=("Arial", 12), command="selectcheck(3)")
btn4 = Button(root, text="  P4   ", relief="raised", font=("Arial", 12), command="selectcheck(4)")

#root.mainloop()
while wincheck():
    if flag:
        playerpos()
        flag = 0
        l2.place(x=800, y=50)
        button = Button(root, text="   ROLL   ", relief="raised", font=("Arial", 20), command=rll)
        button.place(x=805, y=120)
        turn = 2

    else:
        if turn == 1:
            l3.place(x=1000, y=1000)
            l2.place(x=800, y=50)
            turn = 2
        else:
            l2.place(x=1000, y=1000)
            l3.place(x=800, y=50)
            turn = 1
    root.mainloop()