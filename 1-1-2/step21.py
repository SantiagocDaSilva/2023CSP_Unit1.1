#   Add your code here and add comments to your code
#   to describe what each section of code is doing

# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

painter.penup()
painter.goto(0, 0)
painter.pendown()

painter.pencolor("black")
painter.fillcolor("yellow")
painter.begin_fill()
painter.circle(100)
painter.end_fill()

painter.penup()
painter.goto(-50, 120)
painter.pendown()

painter.pencolor("black")
painter.fillcolor("white")
painter.begin_fill()
painter.circle(15)
painter.end_fill()

painter.penup()
painter.goto(50, 120)
painter.pendown()

painter.pencolor("black")
painter.fillcolor("white")
painter.begin_fill()
painter.circle(15)
painter.end_fill()

painter.penup()
painter.goto(-70, 90)
painter.pendown()
painter.right(90)
painter.pencolor("black")
painter.fillcolor("white")
painter.begin_fill()
painter.circle(75,180,)
painter.end_fill()

