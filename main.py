import turtle

s = turtle.getscreen()
s.screensize(canvwidth=800, canvheight=600)
t = turtle.Turtle()
s.bgcolor('black')

# Score
score_a = 0
score_b = 0

# PADDLE A
a = turtle.Turtle()
a.speed(0)
a.shape('square')
a.shapesize(stretch_wid=5, stretch_len=1)
a.color('white')
a.penup()
a.goto(-350, 0)

# PADDLE B
b = turtle.Turtle()
b.speed(0)
b.shape('square')
b.shapesize(stretch_wid=5, stretch_len=1)
b.color('white')
b.penup()
b.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = -4

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center', font=('Courier', 24, 'normal'))


# Function
def a_up():
    y = a.ycor()
    y = y + 20
    a.sety(y)


def a_down():
    y = a.ycor()
    y = y - 20
    a.sety(y)


def b_up():
    y = b.ycor()
    y = y + 20
    b.sety(y)


def b_down():
    y = b.ycor()
    y = y - 20
    b.sety(y)


# Keyboard binding
s.listen()
s.onkeypress(a_up, "w")
s.onkeypress(a_down, "s")
s.onkeypress(b_up, "8")
s.onkeypress(b_down, "2")

while True:
    s.update()

    # MOVE THE BALL
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        score_a = score_a + 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        score_b = score_b + 1
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
        pen.clear()

    # Ball and Paddle collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < b.ycor() + 40 and ball.ycor() > b.ycor() - 40):
        ball.setx(340)
        ball.dx = ball.dx * -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < a.ycor() + 40 and ball.ycor() > a.ycor() - 40):
        ball.setx(-340)
        ball.dx = ball.dx * -1
