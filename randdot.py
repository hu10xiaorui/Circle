import pygame
from random import randint as rand
WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
TEXTCOLOR = (  0,   0,  0)
(width, height) = (800, 800)
background_color= 0,0,0
running = True
vector=[rand(0,10),rand(0,10)]
def getPos():
    #pos = pygame.mouse.get_pos()
    pos=rand(0,1920),rand(0,1080)
    print(pos)
    return (pos)

def drawCircle():

    print(vector)
    color=rand(0,255),rand(0,255),rand(0,255)
    pos=getPos()
    size= rand(1,200)
    circle=pygame.draw.circle(screen, color, pos, size)


def fquit ():

    tk.destroy()
def continuer():
    main()
    tk.destroy()
def main():
    global running, screen, vector
    pygame.init()
    #screen = pygame.display.set_mode((width, height))
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    print(screen)
    pygame.display.set_caption("screen saver")
    screen.fill(background_color)
    pygame.display.update()
    for x in range (100):
        #time.sleep(0.05)
        drawCircle()
        pygame.display.update()
    while running:
        ev = pygame.event.get()


        for event in ev:
            '''
            if event.type == pygame.MOUSEBUTTONUP:
                drawCircle()
                pygame.display.update()
            '''
            #vector=[rand(0,10),rand(0,10)]
            #circle = circle.move(vector)
            if event.type == pygame.QUIT:
                running = False
            if pygame.key.get_focused():
                press = pygame.key.get_pressed()
            else:
                press = False

            if press:
                for i in range(0, len(press)):
                    if press[i] == 1:
                        name = pygame.key.name(i)
                        print(name)
                        if name == "":
                            pass
                        else:
                            pygame.quit()



import sys
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
    from tkinter.constants import *
else:
    # Python 3
    import tkinter as tk
    from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="I make the program crash when pressing space bar to be idle friendly, Please do not mind")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Okay, I won't",command=continuer)
button.pack(side=RIGHT)
button4 = tkinter.Button(frame,text="Nope,I will",command=fquit)
button4.pack(side=LEFT)
tk.mainloop()
