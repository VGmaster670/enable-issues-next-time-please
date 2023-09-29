app.squares = []
app.colorList = ["teal", "black", "midnightBlue", "white", "indigo"]


def drawSquares(numRects):
    colorIndex = 0
    width = 505

    # Run the following code numRects times to draw all of the rectangles.
    ### Fix Your Code Here ###
    for idfk in range(numRects):
        color = app.colorList[colorIndex]
        square = Rect(200, 200, width, width, fill=color, align="center")
        app.squares.append(square)

        colorIndex = (colorIndex + 1) % len(app.colorList)
        width -= 500 / numRects


def onMousePress(mouseX, mouseY):
    # Rotate all of the the squares stored in app.squares. Every square at an
    # even index should rotate 5 degrees clockwise. The rest should rotate
    # counter-clockwise.
    ### Place Your Code Here ###
    for index in range(len(app.squares)):
        if index % 2 == 0:
            app.squares[index].rotateAngle += 5
        else:
            app.squares[index].rotateAngle -= 5
