# symbol generation using python turtle

from turtle import *

def main():
    colors=("red","orange","yellow","seagreen","orchid4","royalblue1","dodgerblue1")
    reset()
    Screen()
    up()
    goto(-320,-195)
    width(70)
    for pcolor in colors:
        color(pcolor)
        down()
        forward(640)
        up()
        backward(640)
        left(90)
        forward(66)
        right(90)

width(25)
color("white")
down()

circle(170)
left(90)
forward(340)
up()
left(180)
forward(170)
right(45)
down()
forward(170)
up()
backward(170)
left(90)
down()
forward(170)
up()
goto(0,300)

if __name__ == "__main__":
    main()
    mainloop()

   
