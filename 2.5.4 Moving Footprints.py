app.background = gradient("tan", "cornSilk", start="left")

# ocean
Polygon(0, 30, 35, 275, 0, 400, fill="cornSilk")
Polygon(0, 170, 15, 275, 0, 330, fill="royalBlue")

# left footprint
soleLeft = Oval(175, 365, 20, 45, fill=rgb(60, 60, 60))
heelLeft = Circle(175, 390, 8, fill=rgb(60, 60, 60))
spaceLeft = Rect(165, 380, 20, 5, fill="wheat")

# right footprint
soleRight = Oval(225, 295, 20, 45, fill=rgb(60, 60, 60))
heelRight = Circle(225, 320, 8, fill=rgb(60, 60, 60))
spaceRight = Rect(215, 310, 20, 5, fill="wheat")


def onMousePress(mouseX, mouseY):
    # Move whichever foot is farther down on the canvas.
    ### Place Your Code Here ###
    if heelLeft.centerY > heelRight.centerY:
        soleLeft.centerY -= 140
        heelLeft.centerY -= 140
        spaceLeft.centerY -= 140
    else:
        soleRight.centerY -= 140
        heelRight.centerY -= 140
        spaceRight.centerY -= 140
    # When both feet are above the canvas, move them to below the canvas.
    if soleRight.bottom < 0:
        soleLeft.centerY = 500
        heelLeft.centerY = 525
        spaceLeft.centerY = 518
        soleRight.centerY = 430
        heelRight.centerY = 455
        spaceRight.centerY = 448
