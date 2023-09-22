# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
painter.pensize(5)

# move turtle without marking a line
painter.penup()
painter.goto(0, -20)
painter.pendown()

# draw a semi-circle
painter.circle(100, 180)

# move turtle without marking a line
painter.penup()
painter.goto(0, 20)
painter.pendown()

# draw a 3-step semi-circle
painter.circle(100, 180, 3)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()