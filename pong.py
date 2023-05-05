from turtle import*
import time
screen= Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
left_paddle= Turtle()
left_paddle.color("white")
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.penup()
left_paddle.goto(380,0)
def go_up():
    new_y= left_paddle.ycor()+20
    left_paddle.goto(left_paddle.xcor(),new_y)
def go_down():
    new_y= left_paddle.ycor()-20
    left_paddle.goto(left_paddle.xcor(),new_y)

right_paddle= Turtle()
right_paddle.color("white")
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.penup()
right_paddle.goto(-380,0)
def go_uep():
    new_y= right_paddle.ycor()+20
    right_paddle.goto(right_paddle.xcor(),new_y)
def go_downe():
    new_y= right_paddle.ycor()-20
    right_paddle.goto(right_paddle.xcor(),new_y)

ball= Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.x_move=10
ball.y_move=10
def move():
    new_x= ball.xcor()+ball.x_move
    new_y= ball.ycor()+ball.y_move
    ball.goto(new_x,new_y)
def bounce():
    ball.y_move*=-1
def bounce_x():
    ball.x_move*=-1
def reset_posi():
    ball.goto(0,0)
    bounce_x()

screen.listen()
screen.onkey(fun=go_up,key="Up")
screen.onkey(fun=go_down,key="Down")
screen.onkey(fun=go_uep,key="w")
screen.onkey(fun=go_downe,key="s")
game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    move()
    if ball.ycor()>280 or ball.ycor()<-280:
        bounce()
    if ball.distance(left_paddle)< 50 and ball.xcor() > 340 or ball.distance(right_paddle)< 50 and ball.xcor() <-340:
        bounce_x()
    if ball.xcor()>380:
        reset_posi()
    if ball.xcor()<-380:
        reset_posi()






screen.exitonclick()