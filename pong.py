import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Player Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = -.1
ball.dy = -.1

# Middle Line
line = turtle.Turtle()
line.speed(0)
line.color('white')
line.penup()
top_of_screen = 300
line.goto(0, top_of_screen)
while top_of_screen > -300:
    line.pendown()
    top_of_screen -= 10
    line.goto(0, top_of_screen)
    line.penup()
    top_of_screen -= 10
    line.goto(0, top_of_screen)

# Score
score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 150)
score.write("{}         {}".format(score_a, score_b), align='center', font=('Courier', 50, 'normal'))


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


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Paddle A
    if paddle_b.ycor() > 250:
        paddle_b.goto(paddle_b.xcor(), 250)

    if paddle_b.ycor() < -245:
        paddle_b.goto(paddle_b.xcor(), -245)

    # Paddle B
    if paddle_a.ycor() > 250:
        paddle_a.goto(paddle_a.xcor(), 250)

    if paddle_a.ycor() < -245:
        paddle_a.goto(paddle_a.xcor(), -245)

    # Ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("{}         {}".format(score_a, score_b), align='center',
                    font=('Courier', 50, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("{}         {}".format(score_a, score_b), align='center',
                    font=('Courier', 50, 'normal'))

    # Collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 55 > ball.ycor() > paddle_b.ycor() - 55):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 55 > ball.ycor() > paddle_a.ycor() - 55):
        ball.setx(-340)
        ball.dx *= -1
