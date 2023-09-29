# background
Rect(0, 0, 400, 400, fill="slateBlue")


def drawFire(x):
    Circle(x, 315, 10, fill="red")
    Polygon(x - 10, 315, x + 10, 315, x, 280, fill="red")
    Circle(x, 315, 7, fill="orange")
    Polygon(x - 7, 315, x + 7, 315, x, 285, fill="orange")
    Circle(x, 315, 3, fill="gold")
    Polygon(x - 3, 315, x + 3, 315, x, 290, fill="gold")


def makePotion(color):
    # Color the liquid in the cauldron using the parameter.
    ### Fix Your Code Here ###
    Oval(200, 215, 225, 180, fill=gradient(rgb(90, 90, 90), "black"))
    Oval(200, 150, 200, 50, fill=color, border="black", borderWidth=10)
    Polygon(125, 275, 145, 290, 120, 320, 110, 320)
    Polygon(275, 275, 255, 290, 280, 320, 290, 320)

    # Create three flames below the cauldron.
    ### (HINT: We created a drawFire function for you above! You just need to
    #          call it with the correct arguments!)
    ### Place Your Code Here ###
    drawFire(170)
    drawFire(200)
    drawFire(230)
    # Draws the two bubbles.
    Circle(235, 40, 20, fill=color, border="black")
    Oval(227, 40, 10, 17, fill="ghostWhite")
    Oval(230, 40, 5, 15, fill=color)
    Circle(165, 95, 30, fill=color, border="black")
    Oval(150, 95, 10, 25, fill="ghostWhite")
    Oval(154, 95, 5, 22, fill=color)
