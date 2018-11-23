import turtle

my_turtle = turtle.Turtle()


def square(length, angle):
	#This part of the code draws the square
	my_turtle.forward(length)
	my_turtle.left(angle)
	my_turtle.forward(length)
	my_turtle.left(angle)
	my_turtle.forward(length)
	my_turtle.left(angle)
	my_turtle.forward(length)
	my_turtle.left(angle)

#Adding multiple arguements to functions
square(250, 90)
square(200, 90)
square(150, 90)
square(100, 90)
square(50, 90)
square(25, 90)