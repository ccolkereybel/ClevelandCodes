import turtle
import time

t=turtle.Turtle()
t.speed(80)

def moveto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

class myTurtle(Turtle):

class Circle:
    def __init__(self, radius, color, filled):
        self.radius = radius
        self.color = color
        self.filled = filled
    def __str__(self):
        if self.filled:
            return f"A {self.color} circle with a radius {self.radius} filled."
        else:
            return f"A {self.color} circle with a radius {self.radius} not filled."
    def draw(self):
        t.color(self.color)
        if self.filled:
            t.fillcolor(self.color)
            t.begin_fill()
        t.circle(self.radius)
        if self.filled:
            t.end_fill()

class Polygon:
    def __init__(self, numsides, sidelength, color, filled):
        self.numsides = numsides
        self.sidelength = sidelength
        self.color = color
        self.filled = filled
    def __str__(self):
        if self.filled:
            return f"A {self.color} {self.numsides} sided polygon filled"
        else:
            return f"A {self.color} {self.numsides} sided polygon not filled"
    def draw(self):
        t.color(self.color)
        if self.filled:
            t.fillcolor(self.color)
            t.begin_fill()
        angle = 360/self.numsides
        for i in range(self.numsides):
            t.forward(self.sidelength)
            t.right(angle)
        if self.filled:
            t.end_fill()

class SuperPolygon(Polygon):
    def __init__(self, numsides, sidelength, color, filled, thickness):
        Polygon.__init__(self, numsides, sidelength, color, filled)
        self.thickness = thickness
        

moveto(-200,-200)
p1 = Polygon(5, 35, "gray", True)
p1.draw()
print(p1)
p1.numsides = 8
p1.color = "red"
p1.draw()
print(p1)


c1 = Circle(50,"red", True) #instantiated Circle object
print(c1)
c1.draw()
time.sleep(2)
c1.color = "pink"
c1.radius = 75
c1.draw()
moveto(200,200)
c2 = Circle(5, "black", False)
for n in range(10):
    c2.draw()
    c2.radius += 5

print(c2)

moveto(-200,200)
c3 = Circle(100,"black", True)
c3.draw()

time.sleep(2)
t.clear()
x=-350
y=-350
p2 = Polygon(6,30,"black", False)
for n in range(50):
    p2.draw()
    time.sleep(.1)
    x += 5
    y += 5
    moveto(x,y)
    t.clear()

turtle.done()

