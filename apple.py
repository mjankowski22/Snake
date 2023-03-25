import random
import turtle

class Apple:

    def __init__(self,squares):
        self.object = turtle.Turtle("circle")
        self.object.color("green")
        self.object.penup()
        self.object.turtlesize(0.5)

        flag=True

        while flag:
            flag=False
            x = random.randint(-28,28)
            y = random.randint(-28,28)
            x=x*10
            y=y*10
            for square in squares:
                if square.xcor()==x and square.ycor()==y:
                    flag=True
        self.object.goto(x,y)
            

    