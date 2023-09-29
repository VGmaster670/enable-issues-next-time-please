Rect(0, 0, 400, 200, fill="lightGrey")
Rect(0, 200, 400, 200, fill="thistle")

# Create a variable that stores the rectangle. Name it tabby.
### Place Your Code Here ###
tabby = Rect(200, 200, 50, 50, fill="darkOrange")


def onMousePress(mouseX, mouseY):
    # This moves tabby to the x position of the mouse.
    tabby.centerX = mouseX

    # Move tabby to be 200 pixels above where the mouse was pressed.
    ### (HINT: We can subtract from the mouseY!)
    ### Place Your Code Here ###
    tabby.centerY = mouseY - 200
