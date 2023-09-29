def drawSun(color):
    # This draws space.
    Rect(0, 0, 400, 400)

    # Change the gradient to use the function parameter.
    ### Fix Your Code Here ###
    Circle(200, 350, 500, fill=gradient(color, "black", "black"))

    # Draw the sun. Use the function parameter!
    ### Place Your Code Here ###
    Circle(200, 275, 40, fill=color)
    # planet
    Circle(200, 775, 500, fill="dodgerBlue")
    Polygon(
        155,
        280,
        50,
        305,
        120,
        330,
        185,
        300,
        260,
        300,
        330,
        325,
        365,
        310,
        255,
        280,
        fill="darkGreen",
    )
    Circle(200, 775, 500, fill=None, border="darkGreen", borderWidth=10)
    Polygon(
        120, 390, 200, 330, 250, 340, 275, 350, 290, 385, 210, 380, fill="darkGreen"
    )


##### Place your code above this line, code below is for testing purposes #####
# test case:
drawSun("darkOrange")
