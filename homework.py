import turtle

# Setup turtle
t = turtle.Turtle()
t.pensize(3)
t.speed(2)

# Function to move to the next letter
def space(dist=30):
    t.penup()
    t.forward(dist)
    t.pendown()

# === DRAWING NAME: "Osaeid" ===

# Letter O
t.circle(20)
space(40)

# Letter S
t.left(90)
t.circle(10, 180)
t.right(180)
t.circle(10, 180)
t.setheading(0)
space(40)

# Letter A
t.left(75)
t.forward(40)
t.right(150)
t.forward(40)
t.backward(20)
t.right(105)
t.forward(12)
t.setheading(0)
space(40)

# Letter E
t.forward(20)
t.backward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(15)
t.backward(15)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.setheading(0)
space(40)

# Letter I
t.forward(20)
t.backward(10)
t.right(90)
t.forward(40)
t.left(90)
t.forward(10)
t.backward(20)
t.setheading(0)
space(40)

# Letter D
t.left(90)
t.forward(40)
t.right(90)
t.circle(-20, 180)
t.setheading(0)

# Finish
t.hideturtle()
turtle.done()
