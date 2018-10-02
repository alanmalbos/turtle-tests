import turtle

def drawing():
	window = turtle.Screen()
	window.bgcolor("red")

	draw_square()
	draw_circle()
	draw_triangle()

	window.exitonclick()


def draw_square():
	

	# instancing a turtle to draw
	brad = turtle.Turtle()

	# customizing the turtle
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(2)

	# drawing a square
	count = 0
	while count < 4:
		brad.forward(100)
		brad.right(90)
		count += 1

	

def draw_circle():
	# instancing a new turtle
	bozo = turtle.Turtle()

	# customizing the new turtle
	bozo.shape("arrow")
	bozo.color("yellow")
	bozo.speed(2)

	# drawing a circle
	bozo.circle(100)

def draw_triangle():
	# instancing a new turtle
	xuxa = turtle.Turtle()

	# customizing the new turtle
	xuxa.shape("turtle")
	xuxa.color("purple")
	xuxa.speed(2)

	# draw a triangle
	count = 0
	while count < 3:
		xuxa.forward(100)
		xuxa.right(120)
		count += 1

drawing()