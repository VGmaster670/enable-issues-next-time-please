app.background = "azure"

app.colors = ["mediumVioletRed", "chocolate", "limeGreen", "dodgerBlue"]
app.index = 0

balloons = Group()


def drawCircularBalloon(cx, cy, color):
    balloon = Group(
        Line(200, 200, 200, 300, fill="gainsboro"),
        Oval(200, 200, 60, 70, fill=color),
        Circle(200, 235, 4, fill=color),
    )
    balloon.centerX = cx
    balloon.centerY = cy
    balloons.add(balloon)


def drawSquareBalloon(cx, cy, color):
    balloon = Group(
        Line(200, 200, 200, 300, fill="gainsboro"),
        Rect(200, 200, 60, 60, fill=color, align="center"),
        Circle(200, 235, 4, fill=color),
    )
    balloon.centerX = cx
    balloon.centerY = cy
    balloons.add(balloon)


def onMousePress(mouseX, mouseY):
    # Draw a new balloon using the current app.index for app.colors. Every second
    # balloon should be square.
    ### (HINT: We have created two functions above that draw the two different
    # balloon shapes.)
    if app.index == (0):
        drawCircularBalloon(mouseX, mouseY, app.colors[app.index])
        print(app.index)
    if app.index == (2):
        drawCircularBalloon(mouseX, mouseY, app.colors[app.index])
        print(app.index)
    if app.index == (1):
        drawSquareBalloon(mouseX, mouseY, app.colors[app.index])
        print(app.index)
    if app.index == (3):
        drawSquareBalloon(mouseX, mouseY, app.colors[app.index])
        print(app.index)

    # Updates the current index for the next time we press the mouse.
    app.index = (app.index + 1) % 4
