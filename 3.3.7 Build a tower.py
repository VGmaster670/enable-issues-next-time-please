app.background = gradient("white", "powderBlue", start="top-left")

# Stores a list of colors that make up the tower's layers.
app.towerColors = []

# sun
Circle(40, 40, 30, fill=gradient("orange", "gold"))

# landscape
Oval(65, 340, 500, 150, fill="forestGreen")
Oval(
    170,
    330,
    200,
    100,
    fill=None,
    border=gradient("paleTurquoise", "skyBlue"),
    borderWidth=40,
)
Oval(310, 325, 400, 100, fill="forestGreen")
Oval(200, 400, 1000, 150, fill=rgb(10, 150, 30))
Circle(25, 290, 4, fill="goldenrod")
Circle(25, 300, 4, fill="goldenrod")
Circle(15, 295, 4, fill="goldenrod")
Circle(325, 310, 4, fill="goldenrod")
Circle(325, 320, 4, fill="goldenrod")
Circle(315, 315, 4, fill="goldenrod")

# materials
marble = Group(
    Polygon(
        51,
        378,
        67,
        357,
        75,
        354,
        85,
        364,
        86,
        373,
        92,
        378,
        fill="lightGrey",
        border="silver",
    ),
    Polygon(
        40, 378, 43, 365, 55, 367, 62, 370, 67, 378, fill="lightGrey", border="silver"
    ),
)

granite = Group(
    Polygon(
        155,
        370,
        162,
        358,
        173,
        355,
        185,
        359,
        188,
        378,
        fill="dimGray",
        border=rgb(95, 95, 95),
    ),
    Polygon(
        125,
        378,
        126,
        366,
        145,
        360,
        150,
        355,
        156,
        365,
        176,
        369,
        188,
        378,
        fill="dimGray",
        border=rgb(95, 95, 95),
    ),
)

limestone = Group(
    Polygon(
        233,
        378,
        234,
        361,
        243,
        355,
        250,
        350,
        257,
        364,
        265,
        366,
        270,
        378,
        fill="gray",
        border="dimGray",
    ),
    Polygon(
        214,
        378,
        222,
        368,
        242,
        360,
        247,
        362,
        250,
        359,
        261,
        378,
        fill="gray",
        border="dimGray",
    ),
)

tower = Group()


def drawLayer(color, bottomVal):
    # Draws a single layer of the tower with the given color and y position.
    layer = Group(
        Rect(290, 375, 20, 10, border="black", borderWidth=0.5),
        Rect(310, 375, 20, 10, border="black", borderWidth=0.5),
        Rect(330, 375, 20, 10, border="black", borderWidth=0.5),
        Rect(350, 375, 20, 10, border="black", borderWidth=0.5),
        Rect(370, 375, 20, 10, border="black", borderWidth=0.5),
        Rect(290, 365, 10, 10, border="black", borderWidth=0.5),
        Rect(300, 365, 20, 10, border="black", borderWidth=0.5),
        Rect(320, 365, 20, 10, border="black", borderWidth=0.5),
        Rect(340, 365, 20, 10, border="black", borderWidth=0.5),
        Rect(360, 365, 20, 10, border="black", borderWidth=0.5),
        Rect(380, 365, 10, 10, border="black", borderWidth=0.5),
        Rect(290, 350, 10, 15, border="black", borderWidth=0.5),
        Rect(313, 350, 10, 15, border="black", borderWidth=0.5),
        Rect(335, 350, 10, 15, border="black", borderWidth=0.5),
        Rect(357, 350, 10, 15, border="black", borderWidth=0.5),
        Rect(380, 350, 10, 15, border="black", borderWidth=0.5),
    )
    layer.bottom = bottomVal
    layer.fill = color
    tower.add(layer)


def makeTower():
    # Draws the tower using the app.towerColors list.
    tower.clear()
    for i in range(len(app.towerColors)):
        drawLayer(app.towerColors[i], 380 - i * 20)


def onMousePress(mouseX, mouseY):
    # Check if the marble, limestone or granite is clicked on and add the
    # appropriate color to the app.towerColors list.
    ### (HINT: The color to be added to the list is the same as the
    #          fill of the material clicked on.)
    ### Place Your Code Here ###
    if marble.hits(mouseX, mouseY):
        app.towerColors.append("lightGrey")
    if granite.hits(mouseX, mouseY):
        app.towerColors.append("dimGray")
    if limestone.hits(mouseX, mouseY):
        app.towerColors.append("gray")
    # Loop through the tower group to check if any layer is clicked on.
    # If it is, remove the fill of that layer from the app.towerColors list.
    ### Place Your Code Here ###
    for layer in tower:
        if layer.hits(mouseX, mouseY):
            app.towerColors.remove(layer.fill)
    # Re-draws the tower with the modified app.towerColors list.
    makeTower()
