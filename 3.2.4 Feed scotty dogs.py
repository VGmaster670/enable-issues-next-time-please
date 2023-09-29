# background
app.background = "mediumSeaGreen"
Line(200, 0, 200, 400, fill="seaGreen", lineWidth=400, opacity=30, dashes=(5, 6))

app.rotationSpeed = 5
app.dogSpeed = 10

# nom labels
noms = Group(Label("nom", 80, 55), Label("nom", 50, 40), Label("nom", 40, 75))
noms.opacity = 0

food = Oval(70, 95, 4, 2, fill="sienna", border="black")
bowl = Polygon(40, 95, 100, 95, 110, 120, 30, 120, fill="tomato", border="black")

scottyDogs = Group()


def drawScotty(x, y):
    # Draws a scotty centered at (x, y) and adds the new dog to the
    # scottyDogs group.
    scotty = Group(
        Polygon(
            200,
            200,
            200,
            150,
            180,
            190,
            170,
            150,
            160,
            200,
            125,
            192,
            140,
            200,
            100,
            200,
            105,
            265,
            110,
            260,
            155,
            260,
            170,
            275,
            170,
            340,
            210,
            340,
            220,
            320,
            270,
            320,
            280,
            340,
            320,
            340,
            315,
            250,
            325,
            235,
            215,
            230,
            fill=rgb(50, 50, 50),
            border="black",
        ),
        Polygon(215, 230, 155, 260, 170, 275, fill="red"),
    )
    scotty.centerX = x
    scotty.centerY = y
    scotty.width = 100
    scotty.height = 90
    scottyDogs.add(scotty)


# draw three scotty dogs
drawScotty(315, 80)
drawScotty(345, 260)
drawScotty(130, 325)


def onMousePress(mouseX, mouseY):
    # Adds food to the bowl as long as the bowl isn't full.
    if food.width < 50:
        food.width += 2
        food.height += 1

    # Rotate each dog in the scottyDogs group by the appropriate rotation speed.
    # If the dog is to the right of the bowl, the dog should move left.
    # If the dog is below the bowl, the dog should move up.
    ### (HINT: Check the position of the dog using it's center coordinates and
    #          check the position of the bowl using it's right bottom.)
    ### Place Your Code Here ###
    for dog in scottyDogs:
        if dog.rotateAngle == app.rotationSpeed:
            dog.rotateAngle -= app.rotationSpeed
        else:
            dog.rotateAngle += app.rotationSpeed
        if dog.centerY > bowl.bottom:
            dog.centerY -= 10
        if dog.centerX > bowl.right:
            dog.centerX -= 10
    # If the noms are not at full opacity yet, the group's opacity should
    # increase. Otherwise, each of the noms should be rotated by the
    # appropriate rotationSpeed.
    ### Place Your Code Here ###
    for nom in noms:
        if nom.opacity < 100:
            nom.opacity += 5
        else:
            if nom.rotateAngle == app.rotationSpeed:
                nom.rotateAngle -= app.rotationSpeed
            else:
                nom.rotateAngle += app.rotationSpeed
    # Change app.rotationSpeed so that the dog waddles back and forth
    # and the noms shake.
    ### Place Your Code Here ###
    pass
