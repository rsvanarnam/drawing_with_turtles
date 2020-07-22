import time
import tkinter
import turtle

# Initializing Tkinter.
root = tkinter.Tk()
canvas = tkinter.Canvas(master = root, width = 1000, height = 700)
canvas.grid(row=0, columnspan=40)

# Initialize Turtle module
turtle = turtle.RawTurtle(canvas)
turtle.pencolor("#000000")
turtle.shape('turtle')

class Movement:
    def __init__(self, name):
        self.name = name

    def reset():
        "Resets the turtle to 0,0 and the defaults specified in settings."
        turtle.speed(5)
        turtle.reset()

    def clear():
        "Clears the screen of turtle drawings."
        turtle.clear()

    def forward():
        "Moves the turtle forward 100 pixels."
        turtle.forward(100)

    def back():
        "Moves the turtle back 100 pixels."
        turtle.back(100)

    def left():
        "Rotates the turtle 45 degrees to the left."
        turtle.left(45)

    def right():
        "Rotates the turtle 45 degrees to the right."
        turtle.right(45)

class Shape():
    """Makes the turtle draw various shapes"""
    def square(length=225):
        "Draws a square."
        for square in range(4):
            turtle.forward(length)
            turtle.right(90)

    def triangle(length=320):
        "Draws an equilateral triangle."
        for triangle in range(3):
            turtle.forward(length)
            turtle.right(120)

    def circle(radius=160):
        "Draws a circle."
        turtle.circle(radius)

    def hexagon(length=160):
        "Draws a hexagon."
        for hexagon in range(6):
            turtle.forward(length)
            turtle.right(60)

    def star(length=300):
        "Draws a star."
        for star in range(5):
            turtle.forward(length)
            turtle.right(144)   

class Circular():
    """Makes the turtle draw various shapes in a circular pattern"""
    def square():
        "Draws a circle of squares with a 5 pixel variance."
        for cirle in range(72):
            Shape.square()
            turtle.right(5)

    def triangle():
        "Draws a circle of equilateral triangles with a 5 pixel variance."
        for circle in range(72):
            Shape.triangle()
            turtle.right(5)

    def circle():
        "Draws a circle of circles with a 5 pixel variance."
        for circle in range(72):
            Shape.circle()
            turtle.right(5)

    def hexagon():
        "Draws a circle of hexagons with a 5 pixel variance."
        for circle in range(72):
            Shape.hexagon()
            turtle.right(5)

    def star():
        "Draws a circle of stars with a 5 pixel variance."
        for circle in range(72):
            Shape.star()
            turtle.right(5)


class Spiral():
    """Makes various shapes into spiral patterns"""
    def square(length=40):
        "Makes a spiral of squares."
        for spiral in range(65):
            Shape.square(length)
            turtle.right(5)
            length = length + 3

    def triangle(length=40):
        "Makes a spiral of triangles."
        for spiral in range(65):
            Shape.triangle(length)
            turtle.right(5)
            length = length + 5

    def circle(length=50):
        "Makes a spiral of circles."
        for spiral in range(65):
            Shape.circle(length)
            turtle.right(5)
            length = length + 1
        turtle.speed(5)

    def hexagon(length=40):
        "Makes a spiral of hexagons."
        for spiral in range(65):
            Shape.hexagon(length)
            turtle.right(5)
            length = length + 2

    def star(length=100):
        "Makes a spiral of stars."
        for spiral in range(65):
            Shape.star(length)
            turtle.right(5)
            length = length + 5

class Color():
    def black():
        "Sets the line color to black."
        turtle.pencolor("#000000")

    def red():
        "Sets the line color to red."
        turtle.pencolor("#FF0000")

    def green():
        "Sets the line color to green."
        turtle.pencolor("#00FF00")

    def blue():
        "Sets the line color to blue."
        turtle.pencolor("#0000FF")
    
    def pink():
        "Sets the line color to pink"
        turtle.pencolor("#FF6FFF")
        
    def yellow():
        "Sets the line color to yellow"
        turtle.pencolor("#FFF200")

class Speed():
    def slowest():
        turtle.speed(1)
    
    def slow():
        turtle.speed(3)

    def regular():
        turtle.speed(6)

    def fast():
        turtle.speed(9)

    def fastest():
        turtle.speed(0)

class Text():
    def greeting():
        print('hello')

class Pen():
    def up():
        turtle.penup()
    
    def down():
        turtle.pendown()

"""Tkinter buttons to control the turtle."""
# Directional buttons.
tkinter.Button(master = root, text = "  ↑  ", command = Movement.forward).grid(row=1, columnspan=4, padx=(15,15), pady=(10,10))
tkinter.Button(master = root, text = "  ↓  ", command = Movement.back).grid(row=3, columnspan=4, padx=(15,15), pady=(10,10))
tkinter.Button(master = root, text = "  ←  ", command = Movement.left).grid(row=2, column=1, padx=(0,5))
tkinter.Button(master = root, text = "  →  ", command = Movement.right).grid(row=2, column=3, padx=(5,0))

# Shapes.
tkinter.Button(master = root, text = "Square", command = Shape.square).grid(row=1, column=6, padx=(10,10), pady=(10,10))
tkinter.Button(master = root, text = "Triangle", command = Shape.triangle).grid(row=1, column=7, padx=(10,10), pady=(10,10))
tkinter.Button(master = root, text = "Circle", command = Shape.circle).grid(row=1, column=8, padx=(10,10), pady=(10,10))
tkinter.Button(master = root, text = "Hexagon", command = Shape.hexagon).grid(row=1, column=9, padx=(10,10), pady=(10,10))
tkinter.Button(master = root, text = "Star", command = Shape.star).grid(row=1, column=10, padx=(10,10), pady=(10,10))

# Circular Patterns.
tkinter.Button(master = root, text = "Circle Of Squares", command = Circular.square).grid(row=2, column=6, padx=(10,10))
tkinter.Button(master = root, text = "Circle of Triangles", command = Circular.triangle).grid(row=2, column=7, padx=(10,10))
tkinter.Button(master = root, text = "Circles in Circles", command = Circular.circle).grid(row=2, column=8, padx=(10,10))
tkinter.Button(master = root, text = "Circle of Hexagons", command = Circular.hexagon).grid(row=2, column=9, padx=(10,10))
tkinter.Button(master = root, text = "Circle of Stars", command = Circular.star).grid(row=2, column=10, padx=(10,10))

# Spiral Patterns.
tkinter.Button(master = root, text = "Square Spiral", command = Spiral.square).grid(row=3, column=6, padx=(10,10))
tkinter.Button(master = root, text = "Triangle Spiral", command = Spiral.triangle).grid(row=3, column=7, padx=(10,10))
tkinter.Button(master = root, text = "Circle Spiral", command = Spiral.circle).grid(row=3, column=8, padx=(10,10))
tkinter.Button(master = root, text = "Hexagon Spiral", command = Spiral.hexagon).grid(row=3, column=9, padx=(10,10))
tkinter.Button(master = root, text = "Star Spiral", command = Spiral.star).grid(row=3, column=10, padx=(10,10))

# Drawing colors.
tkinter.Button(master = root, text = "Black", command = Color.black).grid(row=4, column=6, padx=(10,10))
tkinter.Button(master = root, text = "Red", command = Color.red).grid(row=4, column=7, padx=(10,10))
tkinter.Button(master = root, text = "Green", command = Color.green).grid(row=4, column=8, padx=(10,10))
tkinter.Button(master = root, text = "Blue", command = Color.blue).grid(row=4, column=9, padx=(10,10))
tkinter.Button(master = root, text = "Pink", command = Color.pink).grid(row=4, column=10, padx=(10,10))
tkinter.Button(master = root, text = "Yellow", command = Color.yellow).grid(row=4, column=11, padx=(10,10))

# Speed control.
tkinter.Button(master = root, text = "Slowest", command = Speed.slowest).grid(row=5, column=6, padx=(10,10))
tkinter.Button(master = root, text = "Slow", command = Speed.slow).grid(row=5, column=7, padx=(10,10))
tkinter.Button(master = root, text = "Regular", command = Speed.regular).grid(row=5, column=8, padx=(10,10))
tkinter.Button(master = root, text = "Fast", command = Speed.fast).grid(row=5, column=9, padx=(10,10))
tkinter.Button(master = root, text = "Fastest", command = Speed.fastest).grid(row=5, column=10, padx=(10,10))

# Pen control, Clear, Reset, Quit.
tkinter.Button(master = root, text = "Pen Up", command = Pen.up).grid(row=7, column=6, padx=(10,10))
tkinter.Button(master = root, text = "Pen Down", command = Pen.down).grid(row=7, column=7, padx=(10,10))
tkinter.Button(master = root, text = "Clear", command = Movement.clear).grid(row=7, column=8, padx=(10,10))
tkinter.Button(master = root, text = "Reset", command = Movement.reset).grid(row=7, column=9, padx=(10,10))
tkinter.Button(master = root, text = "Quit", command = root.destroy).grid(row=7, column=10, padx=(10,10))

root.mainloop()