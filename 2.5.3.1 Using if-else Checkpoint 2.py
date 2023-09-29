app.background = "black"

# the ship
Oval(200, 0, 800, 200, fill="dimGrey")
Oval(200, 350, 800, 200, fill="dimGrey")


def drawTeleporter(x):
    Rect(
        x - 50,
        75,
        100,
        250,
        opacity=70,
        fill=gradient("lightBlue", "grey", "lightBlue", start="left"),
    )
    Oval(x, 325, 100, 40, fill="grey")
    Oval(x, 75, 100, 40, fill="grey")


ball = Circle(75, 215, 30, fill="yellow")

drawTeleporter(75)
drawTeleporter(325)


def onMousePress(mouseX, mouseY):
    # If the ball has not reached the center of the right teleporter, move
    # the ball to the right by 25. Otherwise, change the background color and
    # reset the ball in the center of the left teleporter.
    ### Place Your Code Here ###
    if ball.centerX < 325:
        ball.centerX += 25
    else:
        app.background = gradient("steelBlue", "black")
        ball.centerX = 75


def onMouseRelease(mouseX, mouseY):
    app.background = "black"
