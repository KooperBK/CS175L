import turtle

t = turtle.Turtle()
t.speed(100)
t.pencolor("red")

for x in range(8):
    t.pensize(10)
    t.pendown()
    t.forward(100)
    t.right(45)
t.penup()
t.backward(46)
t.right(90)
t.forward(80)
t.left(180)
t.fillcolor("red")
t.begin_fill()
for x in range(8):
    t.fillcolor("red")
    t.pendown()
    t.right(45)
    t.forward(80)
t.end_fill()
t.penup()
text_x = t.xcor() + 97
text_y = t.ycor() - 75
t.goto(text_x, text_y)
t.color("white")
t.write("STOP", align="center", font=("Arial", 40, "bold"))
t.penup()
t.forward(300)
