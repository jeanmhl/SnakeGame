from turtle import Turtle, Screen
import time
from food import Food
from snake import Snake
import random
import ctypes

ctypes.windll.user32.MessageBoxW(0, "Take as much food as you want! :) Q : Turn left, D : Turn right. You can make the Snake Funky with touch C", "Greetings to the Funky Snake Game", 1)

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("The Funky Snake Game")
screen.tracer(0)

snake = Snake()

food = Food()
scoreboard = Turtle()
scoreboard.penup()
scoreboard.goto(0, 280)
scoreboard.color("white")
scoreboard.hideturtle()
scoreboard.write(f"Your score is {food.score}", True, "center")

gameover = Turtle()
gameover.penup()

gameover.color("white")
gameover.hideturtle()



is_ON = True
while is_ON:
    while snake.detect_collision():
        screen.update()
        time.sleep(0.15)
        snake.move()

        if snake.list_square[0].distance(food) < 15:
            food.pop()
            snake.add()
            scoreboard.clear()
            scoreboard.goto(0, 280)
            scoreboard.write(f"Your score is {food.score}", True, "center")
        else:
            pass
        for square in snake.list_square:
            if square == snake.list_square[0] or square == snake.list_square[1]:
                pass
            elif snake.notdetectiontail() == False:
                print("collision de queue chef")


                break


    else:
        gameover.write("GAME OVER :(")
        is_ON = False
        break


screen.exitonclick()

