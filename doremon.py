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
t.right(90)
for i in range(0,90):
    t.right(1)
    t.forward(0.8)
  
t.left(180)
t.penup()  
for i in range(0,90):
    t.left(1)
    t.forward(0.8)
    
t.pendown()
for i in range(0,90):
    t.left(1)
    t.forward(0.8)
    
# whiskers
t.penup()
t.left(180)
t.forward(20)
t.right(90)
t.forward(50)
t.forward(20)
t.pendown()
t.forward(25)
t.penup()
t.left(180)
t.forward(70)
t.pendown()
t.forward(25)
t.penup()
t.left(180)
t.forward(45)
t.right(30)
t.forward(20)
t.pendown()
t.forward(25)
t.penup()
t.left(180)
t.forward(50)
t.left(60)
t.forward(20)
t.pendown()
t.forward(25)
t.penup()
t.left(180)
t.forward(55)
t.forward(20)
t.pendown()
t.forward(25)
t.penup()
t.left(180)
t.forward(55)
t.right(60)
t.forward(20)
t.pendown()
t.forward(25)
t.penup()
t.left(180)
t.forward(55)
t.left(80)

# body


    


input()