Rect(0, 0, 400, 400, fill="lavender")


def onMousePress(mouseX, mouseY):
    # Uncomment the local variables below so your code doesn't crash.
    ### Fix Your Code Here ###
    color1 = rgb(mouseX // 2, mouseY // 2, 255)
    color2 = rgb(255, mouseX // 2, mouseY // 2)
    radius = 20

    # Change the variable names below for the code to work.
    ### Fix Your Code Here ###
    Circle(mouseX, mouseY, 4 * radius, fill=color1)
    Circle(mouseX, mouseY, 3 * radius, fill=color2)
    Circle(mouseX, mouseY, 2 * radius, fill=color1)
    Circle(mouseX, mouseY, radius, fill=color2)
