import turtle
import time
import random

delay = 0.05

# Score
score = 0

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
#head.shapesize(0.5)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.speed(0)
food.penup()
food.color("red")
#food.shapesize(0.5)
food.goto(0, 100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

segments = []

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

    # Eating food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        # Growing snake's body
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.speed(0)
        new_segment.penup()
        new_segment.color("grey")
        new_segment.goto(0, 0)
        segments.append(new_segment)

    # Move segments in a reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move first segment where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)



    move()

    time.sleep(delay)

# wn.mainloop()
