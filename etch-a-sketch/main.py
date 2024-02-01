from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def forward():
    t.forward(10)

def backward():
    t.backward(10)

def left():
    t.setheading(t.heading() + 10)

def right():
    t.setheading(t.heading() - 10)

def clear():
    t.penup()
    t.hideturtle()
    t.clear()
    t.home()
    t.pendown()
    t.showturtle()

s.onkey(forward, "w")
s.onkey(backward, "s")
s.onkey(left, "a")
s.onkey(right, "d")
s.onkey(clear, "c")
s.listen()
s.mainloop()
