app.background = "black"

# moon
outerMoon = Circle(
    200, 200, 165, fill=gradient(rgb(120, 120, 120), rgb(218, 218, 218), start="left")
)
innerMoon = Circle(200, 200, 135, fill=gradient("grey", "lightGrey", start="left"))
innerMoon.nextRadius = 30


def onMousePress(mouseX, mouseY):
    # Check if the inner portion of the moon was clicked on. If it was, draw a
    # crater with radius innerMoon.nextRadius and set the nextRadius for the
    # next crater.
    ### (HINT: Use the hits method to check if the moon was clicked.)
    ### Place Your Code Here ###
    if innerMoon.hits(mouseX, mouseY) == True:
        Circle(
            mouseX,
            mouseY,
            innerMoon.nextRadius,
            fill=gradient("darkGrey", "grey", start="left"),
        )
        if innerMoon.nextRadius == 30:
            innerMoon.nextRadius = 20
        else:
            innerMoon.nextRadius = 30
    # If none of the moon was clicked on, draw a star.
    ### Place Your Code Here ###
    if (
        outerMoon.hits(mouseX, mouseY) == False
        and innerMoon.hits(mouseX, mouseY) == False
    ):
        Star(mouseX, mouseY, 5, 4, fill="white")
