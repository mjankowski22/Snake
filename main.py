import turtle
import time
import snake
import apple as ap

screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake = snake.Snake()


screen.listen()
screen.onkeypress(snake.turnLeft,"Left")
screen.onkeypress(snake.turnRight,"Right")
screen.onkeypress(snake.turnUp,"Up")
screen.onkeypress(snake.turnDown,"Down")

apple = ap.Apple(snake.squares)
score=0
pen=turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0,250)
pen.pendown()

game_is_on = True

while game_is_on:
    screen.update()
    pen.write(f"Score: {score}",False,"center",font=('Arial', 14, 'normal'))
    time.sleep(0.1)
    snake.move()
    if snake.squares[0].xcor()>= apple.object.xcor()-15 and snake.squares[0].xcor()<= apple.object.xcor()+15  and snake.squares[0].ycor()>= apple.object.ycor()-15 and snake.squares[0].ycor()<= apple.object.ycor()+15:
        snake.append_square()
        apple.object.goto(-500,-500)
        apple= ap.Apple(snake.squares)
        pen.clear()
        score+=1

    game_is_on = snake.detect_collisions()

screen.update()
pen.clear()
pen.write("You lose!",False,"center",font=('Arial', 14, 'normal'))


screen.exitonclick()
