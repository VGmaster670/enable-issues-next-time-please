# background
app.background = "lightGrey"

# Define the backlight variable.
backlight = Rect(0, 0, 400, 200, fill="fireBrick")

# Scotty dog
Polygon(
    130,
    60,
    150,
    140,
    150,
    70,
    170,
    130,
    260,
    130,
    220,
    150,
    325,
    160,
    315,
    260,
    290,
    240,
    210,
    240,
    210,
    270,
    130,
    205,
)
Polygon(125, 220, 208, 314, 180, 340, 80, 280)
Polygon(210, 270, 225, 274, 209, 256, fill=None, border="black")
Polygon(130, 205, 210, 270, 227, 276, 215, 320, 125, 220, fill=None, border="black")


def onMousePress(mouseX, mouseY):
    # The height of the backlight should change depending on the mouse.
    # Remember that heights can't be 0!
    ### (HINT: The top of the backlight is always at the top of the canvas.)
    ### (HINT: Add 1 to the mouseY to avoid 0.)
    ### Place Your Code Here ###
    backlight.height = mouseY + 1
