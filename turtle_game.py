import turtle

my_turtle = turtle.Turtle()


def square(length, angle):
	#This part of the code draws the square
	my_turtle.forward(length)
	my_turtle.right(angle)
	my_turtle.forward(length)
	my_turtle.right(angle)
	my_turtle.forward(length)
	my_turtle.right(angle)
	my_turtle.forward(length)
	my_turtle.right(angle)
	my_turtle.forward(length)

#a for loop 
for i in range (4):
	#Adding multiple arguements to functionse
	square(50, 45)