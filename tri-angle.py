import turtle
def draw():
	window = turtle.Screen()
	window.bgcolor("brown")

	nate = turtle.Turtle()
	nate.shape("turtle")
	nate.color("white")

	for i in range(3):
		nate.forward(200)
		nate.left(240)

	window.exitonclick()


draw()