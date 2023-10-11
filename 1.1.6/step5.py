#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used

# creates the body of a spider
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

# constructs the spider legs
legs = 8
lengthoflegs = 100
spacing = 1500 / legs
spider.pensize(5)
n = 0

# draws the spider legs
while (n < legs):
  spider.goto(0,0)
  spider.setheading(spacing * n)
  spider.forward(lengthoflegs)
  n = n + 1

# draws eyes on the spider
spider.pencolor("white")
spider.fillcolor("red")
spider.begin_fill()
spider.end_fill()
spider.penup()
spider.goto(-9, 0)
spider.pendown()
spider.circle(10, 360)
spider.pencolor("white")
spider.fillcolor("red")
spider.begin_fill()
spider.end_fill()

spider.pencolor("white")
spider.fillcolor("red")
spider.begin_fill()
spider.end_fill()
spider.penup()
spider.goto(9, 5)
spider.pendown()
spider.circle(10, 360)
spider.pencolor("white")
spider.fillcolor("red")
spider.begin_fill()
spider.end_fill()



spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()




