import turtle
t=turtle.Turtle()

def moveto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()


print(t.pos())

t.color("light green")
t.fillcolor("red")
t.begin_fill()
for i in range(4): #goes 0,1,2,3
    t.forward(50)
    t.right(90)
t.end_fill()

t.penup()
t.goto(200,200)
t.pendown()
t.color("blue")
numsides = 7
sidelength = 70
angle = 360/numsides
for i in range(numsides):
    t.forward(sidelength)
    t.right(angle)

t.fillcolor("green")
t.penup()
t.goto(-200,200)
t.pendown()
t.begin_fill()
t.circle(-125)
t.end_fill()

moveto(-200,-200)
print(t.pos())

turtle.done()
