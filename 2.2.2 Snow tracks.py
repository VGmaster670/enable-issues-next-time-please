# background
Rect(0, 0, 400, 400, fill="whiteSmoke")


def drawSmallPaw(x, y):
    Oval(x, y, 20, 16, fill="saddleBrown")
    Oval(x - 12, y - 8, 6, 8, fill="saddleBrown")
    Oval(x - 4, y - 14, 6, 8, fill="saddleBrown")
    Oval(x + 4, y - 14, 6, 8, fill="saddleBrown")
    Oval(x + 12, y - 8, 6, 8, fill="saddleBrown")


def drawBigPaw(x, y):
    Oval(x, y, 50, 40, fill="saddleBrown")
    Oval(x - 30, y - 20, 15, 20, fill="saddleBrown")
    Oval(x - 10, y - 35, 15, 20, fill="saddleBrown")
    Oval(x + 10, y - 35, 15, 20, fill="saddleBrown")
    Oval(x + 30, y - 20, 15, 20, fill="saddleBrown")


def onMousePress(mouseX, mouseY):
    # Draw two paw prints of a bear.
    ### (HINT: We wrote two functions above that draw paw prints!)
    ### Place Your Code Here ###
    drawBigPaw(mouseX, mouseY)
    drawBigPaw(mouseX - 100, mouseY - 50)
    # Draw two paw prints of a dog.
    ### Place Your Code Here ###
    drawSmallPaw(mouseX + 200, mouseY)
    drawSmallPaw(mouseX + 150, mouseY - 30)
