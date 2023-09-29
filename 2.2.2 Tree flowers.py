# background
Rect(0, 0, 400, 150, fill=gradient("skyBlue", "powderBlue", start="top"))
Rect(0, 150, 400, 250, fill="darkSeaGreen")

# tree
Star(200, 130, 200, 16, fill="seaGreen", roundness=90)
Polygon(200, 100, 150, 400, 250, 400, fill="saddleBrown")
Polygon(200, 300, 100, 150, 200, 250, 300, 175, fill="saddleBrown")
Polygon(200, 200, 200, 175, 125, 100, fill="saddleBrown")
Polygon(200, 250, 200, 200, 275, 100, fill="saddleBrown")


def onMousePress(mouseX, mouseY):
    # Draw a flower where the mouse is pressed.
    ### (HINT: A flower is drawn using 3 shapes.)
    ### Place Your Code Here ###
    Star(mouseX, mouseY, 25, 10, roundness=90, fill="gold")
    Star(mouseX, mouseY, 20, 20, roundness=50, fill="salmon")
    Circle(mouseX, mouseY, 10, fill="darkOrange")
