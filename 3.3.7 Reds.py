app.stepsPerSecond = 5

app.reds = [255, 220, 200, 150, 125, 100, 90, 75, 50, 10]
app.y = 0

Rect(0, 0, 400, 400)


def drawRowOfRectangles():
    x = 0
    # Draws a rectangle for each red value.
    for red in app.reds:
        Rect(x, app.y, 40, 25, fill=rgb(red, 0, 0))
        x += 40


def onMousePress(mouseX, mouseY):
    drawRowOfRectangles()

    # Remove the last value from the app.reds list and store it in newVal.
    ### Fix Your Code Here ###
    color = app.reds.pop()
    app.reds.insert(0, color)

    # Shifts where the next rectangle will be drawn.
    app.y += 25
