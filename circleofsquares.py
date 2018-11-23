import turtle

my_project = turtle.Turtle()

#change speed here
my_project.speed(10)
my_project.color('blue')

def drawsquare():
	for i in range(4):
		my_project.forward(50)
		my_project.right(90)
	my_project.right(10)

for i in range(36):
	drawsquare()

def biggersquare(length, angle):
	for i in range(4):
		my_project.forward(length)
		my_project.right(angle)
	my_project.right(10)
for i in range(36):
	biggersquare(100,90)
def biggestsquare(length, angle):
	for i in range(4):
		my_project.forward(length)
		my_project.right(angle)
	my_project.right(10)
for i in range(36):
	biggersquare(200,90)
#This code ensure the turtle window stays open after turtle stops
turtle.mainloop()