app.background = "slateBlue"

# blood moon
Circle(340, 60, 40, fill="darkSalmon")


def drawTree(x, y, size):
    Polygon(x - size, 400, x, y, x + size, 400, fill="darkSlateBlue")


def drawCloud(x, y):
    Circle(x, y, 40, fill="lavender")
    Circle(x - 40, y, 20, fill="lavender")
    Circle(x + 40, y, 20, fill="lavender")
    Rect(x - 60, y, 120, 40, fill="slateBlue")


# Draw the clouds, using the drawCloud function.
### Place Code Here ###
drawCloud(100, 160)
drawCloud(200, 100)
drawCloud(350, 150)
# Draw the trees, using the drawTree function.
### Place Code Here ###
drawTree(50, 200, 50)
drawTree(90, 240, 40)
drawTree(175, 300, 25)
drawTree(325, 180, 80)
