c = Circle(200, 200, 50, fill="plum")


def onKeyPress(key):
    if key == "up":
        c.centerY -= 10
    elif key == "down":
        c.centerY += 10

    # Edit onKeyPress so it works for left and right arrows as well
    # as up and down arrows.
    ### Place Your Code Here ###
    if key == "left":
        c.centerX -= 10
    elif key == "right":
        c.centerX += 10
