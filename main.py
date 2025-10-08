import turtle as t

def etri():
    for counter in range(0,3):
        t.forward(50)
        t.left(360/3)
        
def square():
    for counter in range(0,4):
        t.forward(50)
        t.left(90)
        
def pentagon():
    for counter in range(0,5):
        t.forward(100)
        t.left(72)
        
def hexagon():
    for counter in range(0,6):
        t.forward(100)
        t.left(360/6)
        
def heptagon():
    for i in range(0,7):
        t.forward(100)
        t.left(360/7)
        
def octagon():
    for i in range(0,8):
        t.forward(100)
        t.left(360/8)
        
def nonogon():
    for i in range(0,9):
        t.forward(100)
        t.left(360/9)
        
def decagon():
    for i in range(0,10):
        t.forward(100)
        t.left(360/10)
        
# etri()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonogon()
# decagon()


def shapes(number_of_sides):
    for i in range(number_of_sides):
        t.forward(50)
        t.left(360/number_of_sides)
    # if (number_of_sides == 3):
    #     for i in range(0,3):
    #         t.forward(50)
    #         t.left(360/3)
            
    # if (number_of_sides == 4):
    #     for i in range(0,4):
    #         t.forward(50)
    #         t.left(360/4)
            
    # if (number_of_sides == 5):
    #     for i in range(0,5):
    #         t.forward(50)
    #         t.left(360/5)
            
    # if (number_of_sides == 6):
    #     for i in range(0,6):
    #         t.forward(50)
    #         t.left(360/6)
            
    # if (number_of_sides == 7):
    #     for i in range(0,7):
    #         t.forward(50)
    #         t.left(360/7)
            
    # if (number_of_sides == 8):
    #     for i in range(0,8):
    #         t.forward(50)
    #         t.left(360/8)
            
    # if (number_of_sides == 9):
    #     for i in range(0,9):
    #         t.forward(50)
    #         t.left(360/9)
            
    # if (number_of_sides == 10):
    #     for i in range(0,10):
    #         t.forward(50)
    #         t.left(360/10)
            
choice = int(input("How many sides do you want the shape to have?"))

shapes(choice)
        

input()
    