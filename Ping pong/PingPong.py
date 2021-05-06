

#Ping Pong Game
import turtle

int_speed = 1/3
#Window
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-390, 0)


#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+380, 0)



#Pong
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx = int_speed
ball.dy = int_speed


#Pen
pen =turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0    Player 2: 0", align='center', font=("Courier", 18, "normal"))

#Score
score_1 =0
score_2 =0



#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')






#Main Game Loop
while True:
    wn.update()

    #Move Pong
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = int_speed
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = -int_speed
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx= int_speed
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}    Player 2: {}".format(score_1, score_2), align='center', font=("Courier", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx= int_speed
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}    Player 2: {}".format(score_1, score_2), align='center', font=("Courier", 18, "normal"))

    # Paddle and ball Collisions
    if ball.xcor() > 360 and ball.xcor() <390 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()- 40):
        ball.setx(360)
        ball.dx *= -1
        ball.dx -=0.2

    if ball.xcor() < -370 and ball.xcor() >-390 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()- 40):
        ball.setx(-370)
        ball.dx *= -1
        ball.dx += 0.2

