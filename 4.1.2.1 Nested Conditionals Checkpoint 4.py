app.background = "black"

Line(200, 0, 200, 400, fill="lightGrey")
Line(0, 200, 400, 200, fill="lightGrey")


def onMousePress(mouseX, mouseY):
    if mouseX < 200:
        # If the mouse is on the left side of the screen, draw a star in
        # the upper half of the canvas and a circled label on the bottom
        # half.
        ### Place Your Code Here ###
        if mouseY < 200:
            Star(mouseX, mouseY, 30, 7, fill="springGreen")
        else:
            Circle(mouseX, mouseY, 35, fill="fuchsia")
            Label("Woohoo!", mouseX, mouseY)
    else:
        RegularPolygon(mouseX, mouseY, 25, 6, fill="orange")
