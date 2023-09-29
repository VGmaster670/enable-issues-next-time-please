background = Rect(0, 0, 400, 400, fill="dimGray")

# button shadow
Circle(230, 230, 100, fill="darkRed")

button = Circle(200, 200, 100, fill=gradient("red", "fireBrick", start="top-left"))

# messages
message1 = Label("Do not press!", 200, 20, fill="white", size=20)
message2 = Label("Oh no!", 200, 60, fill=None, size=50)


def onMousePress(mouseX, mouseY):
    # Press the button.
    ### Place Your Code Here ###
    button.centerX += 15
    button.centerY += 15
    # Change which message is being displayed.
    ### (HINT: To make a message disappear, you can give it a fill of None!)
    ### Place Your Code Here ###
    message1.fill = None
    message2.fill = "black"
    # Change the background color.
    ### Place Your Code Here ###
    background.fill = "gold"


def onMouseRelease(mouseX, mouseY):
    # This function resets the button, labels, and background.
    button.centerX = 200
    button.centerY = 200

    message1.fill = "white"
    message2.fill = None

    background.fill = "dimGray"
