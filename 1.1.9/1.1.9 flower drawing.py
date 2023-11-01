#set up turtle

import turtle as trtl

# create turtle
painter = trtl.Turtle()



# draw square
painter.penup()
painter.pensize(3)
painter.pendown()
painter.forward(3)
# drawing first side
painter.forward(20)
painter.left(90)

# drawing second side
painter.forward(20)
painter.left(90)

# drawing third side
painter.forward(20)
painter.left(90)

# drawing fourth side
painter.forward(20)
painter.left(90)