# background
Rect(0, 0, 400, 300, fill="darkSlateBlue")
Oval(90, 290, 270, 115, fill="darkGreen")
Oval(290, 290, 305, 150, fill="darkGreen")
Rect(0, 300, 400, 100, fill="dimGrey")

# This circle is the light that we will want to change onMousePress/Release.
# Store it in a variable!
### Place Your Code Here ###
light = Circle(250, 130, 75, fill="darkSlateBlue")
# lamp post and lamp
Rect(140, 270, 40, 80, fill=rgb(35, 20, 5))
Line(160, 270, 160, 50, fill=rgb(35, 20, 5), lineWidth=10)
Line(140, 70, 260, 70, fill=rgb(35, 20, 5), lineWidth=10)
Circle(160, 45, 10, fill=rgb(35, 20, 5))
Line(250, 75, 250, 100, fill=rgb(35, 20, 5))
Polygon(225, 115, 250, 100, 275, 115, fill=rgb(35, 20, 5))
Polygon(225, 115, 275, 115, 265, 155, 235, 155, fill=None, border=rgb(35, 20, 5))


def onMousePress(mouseX, mouseY):
    # Turn the street light on.
    ### Place Your Code Here ###
    light.fill = gradient("lemonChiffon", "darkSlateBlue")


def onMouseRelease(mouseX, mouseY):
    # Turn the street light off.
    ### Place Your Code Here ###
    light.fill = "darkSlateBlue"
