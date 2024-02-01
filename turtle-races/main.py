from turtle import Turtle, Screen
import random

s = Screen()

t = Turtle(visible=False)
t.penup()
t.goto(300, 150)
t.pendown()
t.goto(300, -250)

t.penup()
t.goto(-300, 250)
t.write("Press 'space' to start the race." )

# Podium
t.penup()
t.goto(0, 230)
t.write("1")
t.goto(-20,250)
t.pendown()
t.goto(20, 250)

t.penup()
t.goto(-80, 190)
t.write("2")
t.goto(-100,210)
t.pendown()
t.goto(-60, 210)
t.penup()

t.penup()
t.goto(80, 190)
t.write("3")
t.goto(60,210)
t.pendown()
t.goto(100, 210)

# Create turtles
turtles = []
colors = ["red", "green", "blue", "orange", "magenta", "cyan", "purple"]
turtles_number = len(colors)

for i in range(turtles_number):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-300, 100 - i * 50)
    turtles.append(t)


# Game
def start():
    podium = []

    while len(podium) < turtles_number:
        for i in range(turtles_number):
            t = turtles[i]
            xcoord = t.xcor()
            if xcoord < 300:
                t.forward(10 + random.random()*20)
            else:
                if i not in podium:
                    podium.append(i)

    print(podium)

    turtles[podium[0]].goto(0, 255)
    turtles[podium[1]].goto(-80, 215)
    turtles[podium[2]].goto(80, 215)


s.onkeypress(start, 'space')
s.listen()
s.mainloop()
