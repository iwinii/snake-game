import turtle
import time

delay = 0.05

wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.title("Snake game")
wn.tracer(0)  # Turns off screen updates
wn.bgcolor("green")

# Snake Head
head = turtle.Turtle()
head.shape("square")
head.speed(0)
head.penup()
head.color("black")
head.goto(0, 0)
head.direction = "stop"


# Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def go_right():
    head.direction = "right"


def go_left():
    head.direction = "left"


def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")


# Main loop
while True:
    wn.update()

    move()

    time.sleep(delay)

# wn.mainloop()
