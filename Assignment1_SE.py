

import turtle


def drawSquare(myTurtle, sideLength):
    for i in range(4):
        myTurtle.forward(sideLength)
        myTurtle.right(90)

def TurtleFlower(babyTurtle, numOfSquares):
    for i in range(numOfSquares):
        babyTurtle.color("SteelBlue")
        babyTurtle.begin_fill()
        drawSquare(babyTurtle, sideLength=100)
        babyTurtle.end_fill()
        babyTurtle.right(360/numOfSquares)

def main():
    babyTurtle = turtle.Turtle()
    TurtleFlower(babyTurtle, 10)
    turtle.done()

main()
