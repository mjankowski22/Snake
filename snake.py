import turtle

class Snake:
    def __init__(self):
        self.squares=[
            turtle.Turtle("square"),
            turtle.Turtle("square"),
            turtle.Turtle("square")
        ]
        x=-40
        for square in self.squares:
            square.color("white")
            square.penup()
            square.goto(x,0)
            x+=20
            square.appended=False
        self.squares[0].setheading(180)
        self.squares[0].color("gray")
        self.appended= False

    def move(self):
        
        if self.appended:
            for i in range(len(self.squares)-2,0,-1):
                self.squares[i].goto(self.squares[i-1].xcor(),self.squares[i-1].ycor())
            self.appended= False
        else: 
            for i in range(len(self.squares)-1,0,-1):
                self.squares[i].goto(self.squares[i-1].xcor(),self.squares[i-1].ycor())
        self.squares[0].forward(20)
        self.squares[len(self.squares)-1].appended=False
    
    def turnLeft(self):
        if self.squares[0].heading()!=0 and self.squares[0].heading()!=180:
            self.squares[0].setheading(180)
    def turnRight(self):
        if self.squares[0].heading()!=0 and self.squares[0].heading()!=180:
            self.squares[0].setheading(0)
    def turnUp(self):
        if self.squares[0].heading()!=270 and self.squares[0].heading()!=90:
            self.squares[0].setheading(90)
    def turnDown(self):
        if self.squares[0].heading()!=90 and self.squares[0].heading()!=270:
            self.squares[0].setheading(270)

    def append_square(self):
        square = turtle.Turtle("square")
        square.color("white")
        square.penup()
        square.goto(self.squares[len(self.squares)-2].xcor(),self.squares[len(self.squares)-2].ycor())
        self.squares.append(square)
        self.appended=True

    def detect_collisions(self):
        for i in range(1,len(self.squares)):
            if self.squares[i].xcor()>self.squares[0].xcor()-10 and self.squares[i].xcor()<self.squares[0].xcor()+10 and  self.squares[i].ycor()>self.squares[0].ycor()-10 and self.squares[i].ycor()<self.squares[0].ycor()+10:
                return False
        if self.squares[0].xcor()>290:
            self.squares[0].goto(-290,self.squares[0].ycor())
            return True
        elif  self.squares[0].xcor()<-290 :
            self.squares[0].goto(290,self.squares[0].ycor())
            return True
        elif self.squares[0].ycor()>290 :
            self.squares[0].goto(self.squares[0].xcor(),-290)
            return True
        elif  self.squares[0].ycor()<-290:
            self.squares[0].goto(self.squares[0].xcor(),290)
            return True
        return True