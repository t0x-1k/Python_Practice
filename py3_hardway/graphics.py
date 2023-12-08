import turtle

#set up turtle
pen = turtle.turtle()
pen.speed(0)
pen.width(2)

#get user input
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
age  = input("How old are you? ")

#clearing input and drawing information on screen
pen.clear()
pen.write("Height: {}".format(height), align="center", font=("Arial", 12, "normal"))
pen.goto(0, -30)
pen.write("Weight: {}".format(weight), align="center", font=("Arial", 12, "normal"))
pen.goto(0, -60)
pen.write("Age: {}".format(age), align="center", font=("Arial", 12, "normal"))


#keep window open
turtle.mainloop()