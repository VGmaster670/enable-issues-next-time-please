app.background = "lightSkyBlue"

wrapper = Star(200, 200, 120, 50, roundness=90, fill="seashell")
ears = Polygon(
    240,
    120,
    280,
    80,
    280,
    160,
    160,
    120,
    120,
    80,
    120,
    160,
    fill=gradient("tan", "pink", start="top"),
    visible=False,
    border="wheat",
    borderWidth=10,
)

# muffin top
Circle(200, 200, 100, fill="wheat")
Circle(150, 200, 25, fill="midnightBlue")
Circle(250, 200, 25, fill="midnightBlue")
Circle(200, 250, 15, fill="midnightBlue")


def onMousePress(mouseX, mouseY):
    # Turn the muffin into a chihuahua.
    ### Place Your Code Here ###
    ears.visible = True
    app.background = "peru"
    wrapper.centerY = 230
    wrapper.radius = 90
    wrapper.fill = "grey"


def onMouseRelease(mouseX, mouseY):
    # This turns the chihuahua back into a muffin.
    ears.visible = False
    app.background = "lightSkyBlue"
    wrapper.centerY = 200
    wrapper.radius = 120
    wrapper.fill = "seashell"
