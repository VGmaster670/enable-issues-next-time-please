app.background = "azure"

head = Circle(200, 200, 30, fill="mediumOrchid")
app.colors = ["mediumOrchid", "mediumSpringGreen", "blue"]
app.colorIndex = 0


def getNewHeadColor():
    # Cycle through the three colors.
    head.fill = app.colors[app.colorIndex]
    app.colorIndex += 1
    if app.colorIndex == len(app.colors):
        app.colorIndex = 0


def onKeyHold(keys):
    # Depending on the keys held down, move the head in an appropriate direction.
    ### Place Your Code Here ###
    if "left" in keys:
        head.centerX -= 10
    if "right" in keys:
        head.centerX += 10
    if "up" in keys:
        head.centerY -= 10
    if "down" in keys:
        head.centerY += 10
    # Draw a new circle where the head is with the same fill.
    ### Place Your Code Here ###
    Circle(head.centerX, head.centerY, 30, fill=head.fill)
    # Change the color of the head.
    ### Place Your Code Here ###
    getNewHeadColor()
