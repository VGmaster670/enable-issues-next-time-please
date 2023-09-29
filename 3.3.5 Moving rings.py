app.background = "black"

app.ringList = []


def drawCircles(n):
    # Creates n rings.
    for index in range(n):
        # Every second ring should be thin.
        if index % 2 == 1:
            width = 3
        else:
            width = 5
        angle = 18 * index

        # Gets the center coordinate of the ring by using the angle
        # and the center of the canvas.
        centerX, centerY = getPointInDir(200, 200, angle, 60)

        # Adds the ring to the rings group.
        rings.add(
            Circle(
                centerX,
                centerY,
                60,
                fill=None,
                border="mediumAquamarine",
                borderWidth=width,
            )
        )


rings = Group()
drawCircles(20)
app.ringList = rings.children


def onMouseDrag(mouseX, mouseY):
    ### onMouseDrag gets called when the mouse is held and moved. More notes on
    ### it are in the Unit 2, Section 2 notes "onMouseMove and onMouseDrag".
    borderColor = gradient("pink", "hotPink", start="top")

    # For every other ring, set the border fill to borderColor and increase
    # or decrease the radius depending on the mouse position.
    ### (HINT: The list app.ringList contains every ring in the
    #          rings group!)
    ### (HINT: When mouseX is 0, the radius should be 1. When
    #          mouseX is 400, the radius should be 201.)
    ### Place Your Code Here ###
    # for ring in app.ringList:
    for index in range(len(app.ringList)):
        if index % 2 == 0:
            app.ringList[index].border = borderColor
            app.ringList[index].radius = (mouseX / 2) + 1


def onMouseRelease(mouseX, mouseY):
    # Resets all the ring borders to mediumAquamarine.
    for ring in app.ringList:
        ring.border = "mediumAquamarine"
