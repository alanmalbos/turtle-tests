import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	# instancing a turtle to draw
	brad = turtle.Turtle()

	# customizing the turtle
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(2)

	# drawing a square
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)

	# instancing a new turtle
	bozo = turtle.Turtle()

	# customizing the new turtle
	bozo.shape("arrow")
	bozo.color("yellow")
	bozo.speed(2)

	# drawing a circle
	bozo.circle(100)

	window.exitonclick()

draw_square()