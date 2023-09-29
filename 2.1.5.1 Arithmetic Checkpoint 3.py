Rect(0, 0, 400, 300, fill="lightBlue")
Rect(0, 300, 400, 100, fill="ghostWhite")


def drawSnowman(x):
    # body
    Circle(x, 235, 35, fill="white")
    Circle(x, 290, 40, fill="white")

    # eyes
    Circle(x - 15, 225, 6)
    Circle(x + 15, 225, 6)

    # Fix the nose so that it is drawn properly.
    ### (HINT: One of these points needs to moved to the left!)
    ### Fix Your Code Here ##
    Polygon(x - 15, 245, x, 240, x, 250, fill="orangeRed")
