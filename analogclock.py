import turtle
import time
import math

wn = turtle.Screen()
wn.title("Analog Clock")
wn.bgcolor("black")
wn.setup(width=500, height=500)
wn.tracer(0)

clock = turtle.Turtle()
clock.hideturtle()
clock.speed(0)
clock.pensize(3)


def draw_hand(angle, length, color, width):
    clock.color(color)
    clock.pensize(width)
    clock.penup()
    clock.goto(0, 0)
    clock.setheading(90 - angle)
    clock.pendown()
    clock.forward(length)
    clock.penup()


def draw_numbers():
    clock.color("white")
    clock.penup()

    for number in range(1, 13):

        angle = math.radians(number * 30)

        x = 165 * math.sin(angle)
        y = 165 * math.cos(angle)

        clock.goto(x, y - 10)

        clock.write(
            str(number),
            align="center",
            font=("Arial", 16, "bold")
        )


def draw_clock():
    clock.clear()

    # Clock circle
    clock.color("white")
    clock.pensize(3)
    clock.penup()
    clock.goto(0, -200)
    clock.setheading(0)
    clock.pendown()
    clock.circle(200)
    clock.penup()

    # Numbers 1 to 12
    draw_numbers()

    # Current time
    now = time.localtime()

    second = now.tm_sec
    minute = now.tm_min
    hour = now.tm_hour % 12

    second_angle = second * 6
    minute_angle = minute * 6 + second * 0.1
    hour_angle = hour * 30 + minute * 0.5

    # Hands
    draw_hand(second_angle, 180, "red", 1)
    draw_hand(minute_angle, 150, "blue", 3)
    draw_hand(hour_angle, 100, "green", 5)


while True:
    draw_clock()
    wn.update()
    time.sleep(1)