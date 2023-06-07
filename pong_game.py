import time
import turtle


# score value:
score_a = 0
score_b = 0


win = turtle.Screen()
win.setup(800,600)
win.bgcolor('blue')
win.title('pong game')
win.tracer(0)

#left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape('square')
left_paddle.color('white')
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.penup()
left_paddle.goto(-385,0)

#right paddle:

right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape('square')
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.penup()
right_paddle.goto(378,0)

# ball

t_ball = turtle.Turtle()
t_ball.speed(0)
t_ball.shape('circle')
t_ball.color('white')
t_ball.dx=0.800
t_ball.dy=0.800
t_ball.penup()

# score borad 
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.color('white')
pen.goto(0,260)
pen.write("player A: 0  player B: 0",align='center',font=('Ariel',24))


#move paddle 

#left up
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)

#left down
def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()-20)

#rignt up
def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+20)

#rignt down
def right_paddle_down():
    right_paddle.sety(right_paddle.ycor()-20)

# pen win command
win_p = turtle.Turtle()
#win_p.write("win :",align='center',font=('Ariel',24))

win.listen()
win.onkeypress(left_paddle_up,'w')
win.onkeypress(left_paddle_down,'s')
win.onkeypress(right_paddle_up,'Up')
win.onkeypress(right_paddle_down,'Down')

while True:
    win.update()
    #ball moment
    t_ball.setx(t_ball.xcor()+t_ball.dx)
    t_ball.sety(t_ball.ycor()+t_ball.dy)

    #ball collision
    #top wall
    if t_ball.ycor()>289:
        t_ball.sety(289)
        t_ball.dy *= -1
    #buttom wall
    if t_ball.ycor()<-283:
        t_ball.sety(-283)
        t_ball.dy *= -1
    #rignt wall
    if t_ball.xcor()>385:
        t_ball.setx(385)
        t_ball.dx *=-1
        score_a += 1
        pen.clear()
        pen.write("player A: {}  player B: {}".format(score_a,score_b),align='center',font=('Ariel',24))

    #left wall
    if t_ball.xcor()<-385:
        t_ball.setx(-385)
        t_ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A: {}  player B: {}".format(score_a,score_b),align='center',font=('Ariel',24))


    # collision with paddles
    if t_ball.xcor()>360 and t_ball.ycor() < right_paddle.ycor()+50 and t_ball.ycor() > right_paddle.ycor()-50:
        t_ball.dx *= -1
    if t_ball.xcor()< -363 and t_ball.ycor()<left_paddle.ycor()+50 and t_ball.ycor() >left_paddle.ycor() -50:
        t_ball.dx *= -1

 # win command...
    if score_a == 2:
        win_p.speed(0)
        win_p.penup()
        win_p.hideturtle()
        win_p.color('white')
        win_p.goto(0,160)
        win_p.write("win : player A",align='center',font=('Ariel',24))
        #time.sleep(1)
        
    if score_b == 2:
        win_p.speed(0)
        win_p.penup()
        win_p.hideturtle()
        win_p.color('white')
        win_p.goto(0,160)
        win_p.write("win : player b",align='center',font=('Ariel',24))
        #time.sleep(1)

    if score_b==2 or score_a==2:
        time.sleep(0.1)
        #break       

