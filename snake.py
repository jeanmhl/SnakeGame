from turtle import Turtle, Screen
import time
import random

screen = Screen()

class Snake:

    def __init__(self):
        self.list_square = []
        self.create_snake()
        self.turn_left()
        self.turn_right()
        self.changecolor()
        self.move()
        self.notdetect = True

    def create_snake(self):
        for x in range(4):
            square = Turtle()
            square.penup()
            square.shape("square")
            square.color("white")
            square.speed(1)
            square.goto(x*30, 0)
            self.list_square.append(square)

    def changecolor(self):
        R = random.random()
        B = random.random()
        G = random.random()

        return (R, G, B)

    def funky_snake(self):
        for x in range(len(self.list_square)):
            self.list_square[x].color(self.changecolor())
        print("Funky Snake!")
        self.list_square[0].write("I am a FFuUunky snake !")

    def turn_right(self):
        self.list_square[0].right(90)

    def turn_left(self):
        self.list_square[0].left(90)

    def add(self):
        square = Turtle()
        square.penup()
        square.shape("square")
        square.color(self.changecolor())
        square.speed(1)
        square.goto(self.list_square[-1].pos())
        self.list_square.append(square)
        self.list_square[0].clear()
        self.list_square[0].write("MIaammm")

    def notdetectiontail(self):
        self.notdetect = True

        for square in self.list_square:
            if square == self.list_square[0] or square == self.list_square[1]:
                pass
            elif square.distance(self.list_square[0].pos()) < 10:
                print("collision de queue chef def ")
                self.notdetect = False
                print(self.notdetect)

            else:
                pass

        return self.notdetect

    def move(self):
        self.list_square[0].forward(20)


        screen.listen()
        screen.onkey(key="q", fun=self.turn_left)
        screen.onkey(key="d", fun=self.turn_right)
        screen.onkey(key="c", fun=self.funky_snake)

        for segnum in range(len(self.list_square) - 1, 0, -1):
            self.list_square[segnum].goto(self.list_square[(segnum - 1)].pos())


    def detect_collision(self):
        (a,b) = self.list_square[0].pos()
        if self.notdetectiontail() and abs(a)<300 and abs(b)<300:
            return True

        else:
            print("Collision")
            self.list_square[0].write("Aïe collision !!!")
            return False
