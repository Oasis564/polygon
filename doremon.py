import turtle as t

t.speed(9999)

# head
t.circle(75)
t.penup()
t.left(10)
t.forward(10)
t.pendown()
t.circle(60)

# eyes
t.penup()
t.left(90)
t.forward(140)
t.left(90)
t.forward(10)
t.pendown()
t.circle(20)
t.penup()
t.right(237)
t.forward(44)
t.pendown()
t.circle(20)

# nose
t.right(180)
t.circle(10)
t.penup()
t.left(90)
t.forward(10)
t.left(48)
t.forward(10)
t.pendown()
t.forward(50)

# smile
for i in range(0,180):
    t.right(1)
    t.forward(1)
    


input()