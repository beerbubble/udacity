import turtle

def draw():
    window = turtle.Screen()
    
    window.bgcolor("red")

    pen = turtle.Turtle()

    pen.shape("triangle")

    pen.color("white")

    pen.speed(-5)

    i = 0

    while (i<36):
        draw_square(pen)
        i=i+1
    # draw_circle(pen)
    # draw_triangle(pen)
    window.exitonclick()

def draw_square(turtle):

    i=0
    while (i<4):
        turtle.forward(100)
        turtle.right(90)
        i+=1
    turtle.right(10)

def draw_circle(pen):
    pen.shape("arrow")
    pen.color("blue")
    pen.circle(100)

def draw_triangle(pen):
    pen.shape("turtle")
    pen.color("green")
    pen.right(180)
    i=0
    while (i<3):
        pen.forward(100)
        pen.right(120)
        i+=1


draw()