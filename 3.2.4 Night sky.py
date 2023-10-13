app.background = gradient("midnightBlue", "indigo", "darkSlateBlue", start="top")

objects = Group()


def drawStar(x, y, size):
    # Draws a star centered at (x, y) with the given size and adds it to the
    # objects group
    star = Star(x, y, 3, 50, roundness=20, fill="gold")
    star.width *= size
    star.height *= size
    objects.add(star)


def drawCloud(x, y, size, angle):
    # Draws a nebular cloud centered at (x, y) with the given parameters and
    # adds it to the objects group.
    cloud = Group(
        Star(200, 200, 20, 150, roundness=10),
        Star(202, 202, 20, 150, roundness=10),
        Star(198, 196, 20, 150, roundness=10),
        Star(198, 203, 20, 150, roundness=10),
        Star(203, 195, 20, 150, roundness=10),
    )
    cloud.fill = gradient("royalBlue", "mediumSlateBlue", "salmon")
    cloud.centerX = x
    cloud.centerY = y
    cloud.rotateAngle = angle
    cloud.width *= size
    cloud.height *= size
    objects.add(cloud)


def drawPlanet(x, y, size, color, angle, ringColor):
    # Draws a planet centered at (x, y) with the given parameters and adds it
    # to the objects group.
    planet = Group(
        Arc(200, 200, 30, 30, 90, 180, fill=color),
        Oval(200, 200, 50, 20, fill=ringColor, opacity=60),
        Arc(200, 200, 30, 30, -90, 180, fill=color),
    )
    planet.centerX = x
    planet.centerY = y
    planet.width *= size
    planet.height *= size
    planet.rotateAngle = angle
    objects.add(planet)


# stars
drawStar(256, 82, 0.5)
drawStar(67, 307, 0.3)
drawStar(351, 191, 0.2)
drawStar(143, 144, 0.6)
drawStar(95, 39, 0.7)
drawStar(324, 266, 0.4)
drawStar(276, 219, 0.3)
drawStar(253, 154, 0.2)
drawStar(152, 271, 0.1)
drawStar(30, 141, 0.3)
drawStar(32, 355, 0.1)
drawStar(164, 268, 0.3)

# clouds
drawCloud(181, 334, 0.3, 30)
drawCloud(202, 120, 0.2, 190)

# planets
drawPlanet(200, 200, 0.1, gradient("red", "brown", start="top"), 30, "orange")
drawPlanet(77, 99, 0.05, gradient("teal", "seaGreen", start="top"), 0, None)
drawPlanet(
    49, 218, 0.05, gradient("darkRed", "fireBrick", "peru", start="top"), -30, None
)
drawPlanet(
    363, 356, 0.06, gradient("fireBrick", "darkRed", "red", start="top"), 20, None
)
drawPlanet(
    217, 270, 0.12, gradient("fireBrick", "darkRed", "red", start="top"), -40, None
)
drawPlanet(
    344,
    41,
    0.1,
    gradient("lightSteelBlue", "powderBlue", "lightCyan", start="top"),
    90,
    "steelBlue",
)
drawPlanet(277, 357, 0.13, gradient("teal", "seaGreen", start="top"), 0, None),
drawPlanet(
    117,
    365,
    0.1,
    gradient("lightSteelBlue", "powderBlue", "lightCyan", start="top"),
    20,
    "steelBlue",
)
drawPlanet(
    311, 125, 0.05, gradient("red", "brown", "red", "brown", start="top"), -30, "orange"
)
drawPlanet(166, 50, 0.13, gradient("fireBrick", "darkRed", "red", start="top"), 0, None)

# Sets the size custom properties.
for obj in objects.children:
    obj.smallW = obj.width
    obj.smallH = obj.height
    obj.largeW = obj.width * 8
    obj.largeH = obj.height * 8

lens = Group(
    Circle(200, 200, 80, fill="skyBlue", opacity=20),
    Arc(245, 160, 10, 30, 0, 180, fill="white", rotateAngle=-45, opacity=80),
)
telescope = Group(
    Circle(200, 200, 600, fill=None, border="black", borderWidth=520), lens
)
telescope.visible = False


def onMousePress(mouseX, mouseY):
    # Toggle the telescope's visibility by setting it to False when
    # it's True, and True otherwise.
    if telescope.visible:
        telescope.visible = False
    else:
        telescope.visible = True

    # Moves the telescope and resets all objects to their small sizes.
    telescope.centerX = mouseX
    telescope.centerY = mouseY
    for obj in objects.children:
        obj.width = obj.smallW
        obj.height = obj.smallH


def onMouseMove(mouseX, mouseY):
    # If the telescope is not visible, moves it off screen. Otherwise,
    # center it at the position of the mouse.
    if telescope.visible == False:
        telescope.centerX = 500
    else:
        telescope.centerX = mouseX
        telescope.centerY = mouseY

    # Loop through the objects to check which ones are hit by the lens.
    # Objects in the lens should be large and objects outside the lens should
    # be small.
    ### (HINT: Each objet has custom properties for the small and large sizes.)
    ### (HINT: Check whether the center of the object hits the lens.)
    ### Place Your Code Here ###
    for object in objects.children:
        if lens.hits(object.centerX, object.centerY):
            object.width = object.largeW
            object.height = object.largeH
        else:
            object.width = object.smallW
            object.height = object.smallH
