app.background = "black"

app.colors = ["teal", "violet", "aquamarine", "pink", "tomato"]
app.index = 0

# ground
Rect(0, 360, 400, 40, fill="darkSlateBlue")

# moon
Circle(320, 80, 35, fill="azure")
Star(320, 80, 50, 500, fill="azure")


def drawTree(x, y, color):
    if y < 320:
        Polygon(x - 5, y, x + 5, y, x + 10, 380, x - 10, 380, fill="grey")
        Circle(x - 20, y, 18, fill=color)
        Circle(x + 20, y, 18, fill=color)
        Oval(x, y - 15, 50, 45, fill=color)
        Oval(x, y + 10, 45, 35, fill=color)


def onMousePress(mouseX, mouseY):
    # Draw a tree where the mouse is pressed using the color at the current index
    # in the app.colors list. Then update the index so the next tree drawn uses
    # the next color in the list.
    ### Place Your Code Here ###
    drawTree(mouseX, mouseY, app.colors[app.index % 5])
    app.index += 1
