import time
import tkinter as tk
import turtle

# Initializing Tkinter.
root = tk.Tk()
canvas = tk.Canvas(master = root, width = 1000, height = 700)
canvas.grid(row=0, columnspan=40)

# Initialize Turtle module
turtle = turtle.RawTurtle(canvas)
turtle.pencolor("#000000")
turtle.shape('turtle')

class Movement():

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

    def reset():
        "Resets the turtle to 0,0 and the defaults specified in settings."
        turtle.speed(5)
        turtle.reset()

    def clear():
        "Clears the screen of turtle drawings."
        turtle.clear()

    def stamp():
        turtle.stamp()

class Shape():
    """Makes the turtle draw various shapes"""

    def circle(radius=160):
        "Draws a circle."
        turtle.circle(radius)

    def crescent(length = 100):
        "Draws a crescent."
        turtle.right(40)
        turtle.circle(length,180)
        turtle.forward(-20)
        turtle.circle(length,-190)

    def heart():
        "Draws a heart."
        turtle.left(90)
        turtle.circle(30,180)
        turtle.left(180)
        turtle.circle(30,180)
        turtle.left(45)
        turtle.forward(85)
        turtle.left(90)
        turtle.forward(85)

    def hexagon(length=160):
        "Draws a hexagon."
        for hexagon in range(6):
            turtle.forward(length)
            turtle.right(60)

    def oval(length = 60):
        "Draws an oval."
        turtle.left(45)
        for i in range(2):
            turtle.circle(length,90)
            turtle.circle(length/2,90)

    def pentagon(length = 60):
        "Draws a pentagon."
        turtle.right(36)
        for pentagon in range(5):
            turtle.forward(length)
            turtle.right(72)

    def square(length=225):
        "Draws a square."
        for square in range(4):
            turtle.forward(length)
            turtle.right(90)

    def star(length=300):
        "Draws a star."
        for star in range(5):
            turtle.forward(length)
            turtle.right(144)  

    def triangle(length=320):
        "Draws an equilateral triangle."
        for triangle in range(3):
            turtle.forward(length)
            turtle.right(120) 

class Circular():
    """Makes the turtle draw various shapes in a circular pattern"""

    def circle():
        "Draws a circle of circles with a 5 pixel variance."
        for circle in range(72):
            Shape.circle()
            turtle.right(5)

    def crescent():
        "Draws a circle of crescents with a 5 pixel variance."
        for circle in range(72):
            Shape.crescent()
            turtle.right(5)

    def heart():
        "Draws a circle of hearts with a 5 pixel variance."
        for circle in range(72):
            Shape.heart()
            turtle.right(2)

    def hexagon():
        "Draws a circle of hexagons with a 5 pixel variance."
        for circle in range(72):
            Shape.hexagon()
            turtle.right(5)

    def oval():
        "Draws a circle of ovals with a 5 pixel variance."
        for circle in range(72):
            Shape.oval()
            turtle.right(5)

    def pentagon():
        "Draws a circle of pentagons with a 5 pixel variance."
        for circle in range(72):
            Shape.pentagon()
            turtle.right(5)

    def square():
        "Draws a circle of squares with a 5 pixel variance."
        for cirle in range(72):
            Shape.square()
            turtle.right(5)

    def star():
        "Draws a circle of stars with a 5 pixel variance."
        for circle in range(72):
            Shape.star()
            turtle.right(5)

    def triangle():
        "Draws a circle of equilateral triangles with a 5 pixel variance."
        for circle in range(72):
            Shape.triangle()
            turtle.right(5)


class Spiral():
    """Makes various shapes into spiral patterns"""

    def circle(length=50):
        "Makes a spiral of circles."
        for spiral in range(65):
            Shape.circle(length)
            turtle.right(5)
            length = length + 1
        turtle.speed(5)

    def crescent(length = 50):
        "Makes a spiral of crescents."
        for spiral in range(65):
            Shape.crescent(length)
            turtle.right(5)
            length = length + 1

    def heart(length = 50):
        "Makes a spiral of hearts."
        for spiral in range(65):
            Shape.heart(length)
            turtle.right(5)
            length = length +1

    def hexagon(length=40):
        "Makes a spiral of hexagons."
        for spiral in range(65):
            Shape.hexagon(length)
            turtle.right(5)
            length = length + 2

    def oval(length = 40):
        "Makes a spiral of ovals."
        for spiral in range(65):
            Shape.oval(length)
            turtle.right(5)
            length = length + 2

    def pentagon(length = 40):
        "Makes a spiral of pentagons."
        for spiral in range(65):
            Shape.pentagon(length)
            turtle.right(5)
            length = length + 5

    def square(length=40):
        "Makes a spiral of squares."
        for spiral in range(65):
            Shape.square(length)
            turtle.right(5)
            length = length + 3

    def star(length=100):
        "Makes a spiral of stars."
        for spiral in range(65):
            Shape.star(length)
            turtle.right(5)
            length = length + 5

    def triangle(length=40):
        "Makes a spiral of triangles."
        for spiral in range(65):
            Shape.triangle(length)
            turtle.right(5)
            length = length + 5


class Color():
    def black():
        "Sets the line color to black."
        turtle.pencolor("#000000")

    def blue():
        "Sets the line color to blue."
        turtle.pencolor("#0000FF")

    def green():
        "Sets the line color to green."
        turtle.pencolor("#00FF00")

    def orange():
        "Sets the line color to orange."
        turtle.pencolor("#FFA500")

    def pink():
        "Sets the line color to pink."
        turtle.pencolor("#FF6FFF")

    def red():
        "Sets the line color to red."
        turtle.pencolor("#FF0000")

    def violet():
        "Sets the line color to purple."
        turtle.pencolor("#7F00FF")
        
    def yellow():
        "Sets the line color to yellow."
        turtle.pencolor("#FFF200")

    def rainbow():
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.pencolor(colors)
        """
        turtle.pencolor("#0000FF") # Blue 
        turtle.pencolor("#00FF00") # Green 
        turtle.pencolor("#FFA500") # Orange
        turtle.pencolor("#FF6FFF") # Pink
        turtle.pencolor("#FF0000") # Red 
        turtle.pencolor("#7F00FF") # Purple  
        turtle.pencolor("#FFF200") # Yellow
        """

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

# Row 2 Draw Forward, Colors.
button = tk.Button(root, text = '↑', command = Movement.forward)
button.grid(column = 2, row = 2)
button = tk.Label(root, text = 'Color')
button.grid(column = 5, row = 2)
button = tk.Button(root, text = 'Black', command = Color.black)
button.grid(column = 6, row = 2)
button = tk.Button(root, text = 'Blue', command = Color.blue)
button.grid(column = 7, row = 2)
button = tk.Button(root, text = 'Green', command = Color.green)
button.grid(column = 8, row = 2)
button = tk.Button(root, text = 'Orange', command = Color.orange)
button.grid(column = 9, row = 2)
button = tk.Button(root, text = 'Pink', command = Color.pink)
button.grid(column = 10, row = 2)
button = tk.Button(root, text = 'Red', command = Color.red)
button.grid(column = 11, row = 2)
button = tk.Button(root, text = 'Violet', command = Color.violet)
button.grid(column = 12, row = 2)
button = tk.Button(root, text = 'Yellow', command = Color.yellow)
button.grid(column = 13, row = 2)
button = tk.Button(root, text = 'Rainbow', command = Color.rainbow)
button.grid(column = 14, row = 2)

# Row 3. Rotate Left and Right, Speed Settings, Stamp, Clear, Reset.
button = tk.Button(root, text = '←', command = Movement.left)
button.grid(column = 1, row = 3)
button = tk.Button(root, text = '→', command = Movement.right)
button.grid(column = 3, row = 3)
button = tk.Label(root, text = 'Control')
button.grid(column = 5, row = 3)
button = tk.Button(root, text = 'Slowest', command = Speed.slowest)
button.grid(column = 6, row = 3)
button = tk.Button(root, text = 'Slow', command = Speed.slow)
button.grid(column = 7, row = 3)
button = tk.Button(root, text = 'Regular', command = Speed.regular)
button.grid(column = 8, row = 3)
button = tk.Button(root, text = 'Fast', command = Speed.fast)
button.grid(column = 9, row = 3)
button = tk.Button(root, text = 'Fastest', command = Speed.fastest)
button.grid(column = 10, row = 3)
button = tk.Button(root, text = 'Filler')
button.grid(column = 11, row = 3)
button = tk.Button(root, text = 'Stamp', command = Movement.stamp)
button.grid(column = 12, row = 3)
button = tk.Button(root, text = 'Clear', command = Movement.clear)
button.grid(column = 13, row = 3)
button = tk.Button(root, text = 'Reset', command = Movement.reset)
button.grid(column = 14, row = 3)

# Row 4. Draw Backward and Shapes
button = tk.Button(root, text = '↓', command = Movement.back)
button.grid(column = 2, row = 4)
button = tk.Label(root, text = 'Shape')
button.grid(column = 5, row = 4)
button = tk.Button(root, text = 'Circle', command = Shape.circle)
button.grid(column = 6, row = 4)
button = tk.Button(root, text = 'Crescent', command = Shape.crescent)
button.grid(column = 7, row = 4)
button = tk.Button(root, text = 'Heart', command = Shape.heart)
button.grid(column = 8, row = 4)
button = tk.Button(root, text = 'Hexagon', command = Shape.hexagon)
button.grid(column = 9, row = 4)
button = tk.Button(root, text = 'Oval', command = Shape.oval)
button.grid(column = 10, row = 4)
button = tk.Button(root, text = 'Pentagon', command = Shape.pentagon)
button.grid(column = 11, row = 4)
button = tk.Button(root, text = 'Square', command = Shape.square)
button.grid(column = 12, row = 4)
button = tk.Button(root, text = 'Star', command = Shape.star)
button.grid(column = 13, row = 4)
button = tk.Button(root, text = 'Triangle', command = Shape.triangle)
button.grid(column = 14, row = 4)

# Row 5. Circular Patterns.
button = tk.Label(root, text = 'Circular Patterns')
button.grid(column = 5, row = 5)
button = tk.Button(root, text = 'Circle', command = Circular.circle)
button.grid(column = 6, row = 5)
button = tk.Button(root, text = 'Crescent', command = Circular.crescent)
button.grid(column = 7, row = 5)
button = tk.Button(root, text = 'Heart', command = Circular.heart)
button.grid(column = 8, row = 5)
button = tk.Button(root, text = 'Hexagon', command = Circular.hexagon)
button.grid(column = 9, row = 5)
button = tk.Button(root, text = 'Oval', command = Circular.oval)
button.grid(column = 10, row = 5)
button = tk.Button(root, text = 'Pentagon', command = Circular.pentagon)
button.grid(column = 11, row = 5)
button = tk.Button(root, text = 'Square', command = Circular.square)
button.grid(column = 12, row = 5)
button = tk.Button(root, text = 'Star', command = Circular.star)
button.grid(column = 13, row = 5)
button = tk.Button(root, text = 'Triangle', command = Circular.triangle)
button.grid(column = 14, row = 5)

# Row 6. Spiral Patterns.
button = tk.Label(root, text = 'Spiral Patterns')
button.grid(column = 5, row = 6)
button = tk.Button(root, text = 'Circle', command = Spiral.circle)
button.grid(column = 6, row = 6)
button = tk.Button(root, text = 'Crescent', command = Spiral.crescent)
button.grid(column = 7, row = 6)
button = tk.Button(root, text = 'Heart', command = Spiral.heart)
button.grid(column = 8, row = 6)
button = tk.Button(root, text = 'Hexagon', command = Spiral.hexagon)
button.grid(column = 9, row = 6)
button = tk.Button(root, text = 'Oval', command = Spiral.oval)
button.grid(column = 10, row = 6)
button = tk.Button(root, text = 'Pentagon', command = Spiral.pentagon)
button.grid(column = 11, row = 6)
button = tk.Button(root, text = 'Square', command = Spiral.square)
button.grid(column = 12, row = 6)
button = tk.Button(root, text = 'Star', command = Spiral.star)
button.grid(column = 13, row = 6)
button = tk.Button(root, text = 'Triangle', command = Spiral.triangle)
button.grid(column = 14, row = 6)

# Row 7. Pen up, Pen down.
button = tk.Button(root, text = 'Pen Up', command = Pen.up)
button.grid(column = 1, row = 7)
button = tk.Button(root, text = 'Pen Down', command = Pen.down)
button.grid(column = 3, row = 7)

# Row 8. Add and Remove Turtles, Turtle Race, Reset, Quit.
button = tk.Button(root, text = 'Add Turtle')
button.grid(column = 1, row = 8)
button = tk.Button(root, text = 'Remove Turtle')
button.grid(column = 3, row = 8)
button = tk.Button(root, text = 'Turtle Race')
button.grid(column = 12, row = 8)
button = tk.Button(root, text = 'Reset', command = Movement.reset)
button.grid(column = 13, row = 8)
button = tk.Button(root, text = 'Quit', command = root.destroy)
button.grid(column = 14, row = 8)

root.grid_columnconfigure(4, minsize=100)

col_count, row_count = root.grid_size()

for col in range(14):
    root.grid_columnconfigure(col, minsize=35)

for row in range(8):
    root.grid_rowconfigure(row, minsize=35)

root.mainloop()