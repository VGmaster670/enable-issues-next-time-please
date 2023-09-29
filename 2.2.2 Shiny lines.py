# background
Rect(0, 0, 400, 400)


def onMousePress(mouseX, mouseY):
    # Draw a line from left-top corner to where the mouse is being clicked.
    ### (HINT: Don't forget about the gradient!)
    ### Place Your Code Here ###
    Line(0, 0, mouseX, mouseY, fill=gradient("red", "black"), lineWidth=2)
