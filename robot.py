import turtle

Mj = turtle.Turtle()
turtle.bgcolor("sky blue")
turtle.title("michael and joseph robot")


def rectangle(length, width, color):
    Mj.color(color)
    Mj.pendown()
    Mj.begin_fill()
    for i in range(4):
        if i % 2 != 0:
            Mj.forward(length)
            Mj.right(90)

        else:
            Mj.forward(width)
            Mj.right(90)

    Mj.end_fill()
    Mj.penup()


Mj.penup()
Mj.speed(0)

Mj.goto(-100, -150)  # left shoe of the robot
rectangle(20, 60, "yellow")

Mj.goto(-30, -150)  # right shoe of the robot
rectangle(20, 60, "yellow")

Mj.goto(-70, -50)  # left leg of the robot
rectangle(100, 20, "red")

Mj.goto(-25, -50)  # right leg of the robot
rectangle(100, 20, "red")

Mj.goto(-90, 100)  # body of the robot
rectangle(150, 100, "green")

Mj.goto(-150, 70)  # left hand of the robot
rectangle(15, 60, "purple")
Mj.goto(-150, 110)  # left hand of the robot
rectangle(40, 15, "purple")

Mj.goto(10, 70)  # right hand of the robot
rectangle(15, 60, "purple")
Mj.goto(55, 110)  # right hand of the robot
rectangle(40, 15, "purple")

Mj.goto(-50, 170)  # neck of the robot
rectangle(70, 20, "pink")

Mj.goto(-85, 170)  # head of the robot
rectangle(50, 90, "orange")

Mj.goto(-60, 160)  # eye of the robot
rectangle(20, 40, "black")
Mj.goto(-50, 155)  # left eye of the robot
rectangle(5, 5, "white")
Mj.goto(-35, 155)  # right eye of the robot
rectangle(5, 5, "white")

Mj.goto(-65, 136)  # mouth of the robot
rectangle(5, 50, "brown")

Mj.goto(-155, 130)  # left finger of the robot
rectangle(25, 25, "violet")
Mj.goto(-147, 130)  # left finger of the robot
rectangle(15, 10, turtle.bgcolor())

Mj.goto(50, 130)  # right finger of the robot
rectangle(25, 25, "violet")
Mj.goto(58, 130)  # right finger of the robot
rectangle(15, 10, turtle.bgcolor())

turtle.hideturtle()
turtle.done()
