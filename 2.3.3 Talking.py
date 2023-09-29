# background
Rect(0, 0, 400, 400, fill="lavenderBlush")

# This draws the voice.
voice = Star(140, 215, 75, 8, roundness=10, visible=False)
Rect(80, 135, 75, 160, fill="lavenderBlush")

# face
Oval(30, 140, 230, 350, fill="lightSkyBlue")
Polygon(0, 0, 130, 0, 145, 60, 180, 130, 145, 155, 0, 210, fill="lightSkyBlue")
eye = Circle(80, 50, 15)

mouth = Polygon(
    150, 185, 80, 185, 95, 225, 140, 250, fill="lavenderBlush", visible=False
)


def onMousePress(x, y):
    # Open the mouth and talk.
    ### Place Your Code Here ###
    mouth.visible = True
    voice.visible = True
    eye.radius = 20


def onMouseRelease(x, y):
    # Close the mouth to stop talking.
    ### Place Your Code Here ###
    mouth.visible = False
    voice.visible = False
    eye.radius = 15
