"""
To do:
1. Figure out how to change color upon each new line (rainbow).

2. Fix several circular and spiral patterns not making the desired pattern.

3. Either figure out how to add and remove turtles, or find something else 
of interest to fill those buttons.

4. Refactor buttons. Perhaps a for loop with a list for each section?
"""

import tkinter as tk
import turtle

# Initializing Tkinter.
root = tk.Tk()
canvas = tk.Canvas(master = root, width = 900, height = 600)
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

class Button:
    def __init__(self, setText, setCommand, setRow, setColumn):
        self.setText = setText
        self.setCommand = setCommand
        self.setRow = setRow
        self.setColumn = setColumn

    def smallButton(setText, setCommand, setRow, setColumn):
        button = tk.Button(root, text = setText, command = setCommand, height = 2, width = 4)
        button.grid(row = setRow, column = setColumn)

    def mediumButton(setText, setCommand, setRow, setColumn):
        button = tk.Button(root, text = setText, command = setCommand, height = 2, width = 10)
        button.grid(row = setRow, column = setColumn)

# Directional Buttons
Button.smallButton('↑', Movement.forward, 3, 2)
Button.smallButton('←', Movement.left, 4, 1)
Button.smallButton('→', Movement.right, 4, 3)
Button.smallButton('↓', Movement.back, 5, 2)

# Color Change Buttons
#Label.label('Color', 2, 5)
Button.mediumButton('Black', Color.black, 2, 6)
Button.mediumButton('Blue', Color.blue, 2, 7)
Button.mediumButton('Green', Color.green, 2, 8)
Button.mediumButton('Orange', Color.orange, 2, 9)
Button.mediumButton('Pink', Color.pink, 2, 10)
Button.mediumButton('Red', Color.red, 2, 11)
Button.mediumButton('Violet', Color.violet, 2, 12)
Button.mediumButton('Yellow', Color.yellow, 2, 13)
Button.mediumButton('Rainbow', Color.rainbow, 2, 14)

# Speed, Stamp, Clear, Reset Buttons
#Label.label('Control', 3, 5)
Button.mediumButton('Slowest\nSpeed', Speed.slowest, 3, 6)
Button.mediumButton('Slow\nSpeed', Speed.slow, 3, 7)
Button.mediumButton('Normal\nSpeed', Speed.regular, 3, 8)
Button.mediumButton('Fast\nSpeed', Speed.fast, 3, 9)
Button.mediumButton('Fastest\nSpeed', Speed.fastest, 3, 10)
Button.mediumButton('Pen\nUp', Pen.up, 3, 11)
Button.mediumButton('Pen\nDown', Pen.down, 3, 12)
Button.mediumButton('Add\nTurtle', Color.rainbow, 3, 13)
Button.mediumButton('Remove\nTurtle', Color.rainbow, 3, 14)

# Shape Buttons
#Label.label('Shape', 4, 5)
Button.mediumButton('Circle', Shape.circle, 4, 6)
Button.mediumButton('Crescent', Shape.crescent, 4, 7)
Button.mediumButton('Heart', Shape.heart, 4, 8)
Button.mediumButton('Hexagon', Shape.hexagon, 4, 9)
Button.mediumButton('Oval', Shape.oval, 4, 10)
Button.mediumButton('Pentagon', Shape.pentagon, 4, 11)
Button.mediumButton('Square', Shape.square, 4, 12)
Button.mediumButton('Star', Shape.star, 4, 13)
Button.mediumButton('Triangle', Shape.triangle, 4, 14)

# Circular Pattern Buttons
#Label.label('Circle Pattern', 5, 5)
Button.mediumButton('Circular\nCircles', Circular.circle, 5, 6)
Button.mediumButton('Circular\nCrescents', Circular.crescent, 5, 7)
Button.mediumButton('Circular\nHearts', Circular.heart, 5, 8)
Button.mediumButton('Circular\nHexagons', Circular.hexagon, 5, 9)
Button.mediumButton('Circular\nOvals', Circular.oval, 5, 10)
Button.mediumButton('Circular\nPentagons', Circular.pentagon, 5, 11)
Button.mediumButton('Circular\nSquares', Circular.square, 5, 12)
Button.mediumButton('Circular\nStars', Circular.star, 5, 13)
Button.mediumButton('Circular\nTriangles', Circular.triangle, 5, 14)

# Spiral Pattern Buttons
#Label.label('Spiral Pattern', 6, 5)
Button.mediumButton('Spiral\nCircles', Spiral.circle, 6, 6)
Button.mediumButton('Spiral\nCrescents', Spiral.crescent, 6, 7)
Button.mediumButton('Spiral\nHearts', Spiral.heart, 6, 8)
Button.mediumButton('Spiral\nHexagons', Spiral.hexagon, 6, 9)
Button.mediumButton('Spiral\nOvals', Spiral.oval, 6, 10)
Button.mediumButton('Spiral\nPentagons', Spiral.pentagon, 6, 11)
Button.mediumButton('Spiral\nSquares', Spiral.square, 6, 12)
Button.mediumButton('Spiral\nStars', Spiral.star, 6, 13)
Button.mediumButton('Spiral\nTriangles', Spiral.triangle, 6, 14)

# Clear, Reset, Quit Buttons
Button.mediumButton('Clear', Movement.clear, 8, 12)
Button.mediumButton('Reset', Movement.reset, 8, 13)
Button.mediumButton('Quit', root.destroy, 8, 14)

root.mainloop()