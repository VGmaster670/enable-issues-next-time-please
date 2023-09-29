def drawMountains():
    Polygon(0, 175, 150, 175, 50, 100, fill="steelBlue")
    Polygon(210, 175, 400, 175, 300, 100, fill="midnightBlue")
    Polygon(50, 175, 190, 175, 130, 120, fill="midnightBlue")


def drawOcean():
    Polygon(0, 285, 180, 175, 0, 175, fill="dodgerBlue")
    Polygon(0, 285, 180, 175, 190, 175, 0, 350, fill="tan")


def drawGroundAndSky(groundColor):
    Rect(0, 0, 400, 175, fill="lightSkyBlue")
    Rect(0, 175, 400, 225, fill=groundColor)
    Polygon(0, 350, 0, 400, 400, 400, 400, 350, 210, 175, 190, 175, fill="grey")
    Line(
        200,
        175,
        200,
        400,
        lineWidth=10,
        dashes=True,
        fill=gradient("grey", "silver", start="top"),
    )


def drawScene(isMountainous, isDesert, isBeach, isNightTime, destination, milesToGo):
    # Draw the ground and ocean based on the values of the first three parameters.
    ### Place Your Code Here ###
    if isMountainous == True:
        drawGroundAndSky("lightGreen")
        drawMountains()
    elif isDesert == True:
        drawGroundAndSky("burlyWood")
    elif isBeach == True:
        drawGroundAndSky("lightGreen")
        drawOcean()
    # Draw the sign board with destination and milesToGo.
    ### Place Your Code Here ###
    Line(290, 200, 290, 230, fill="black")
    Line(370, 200, 370, 230, fill="black")
    Rect(280, 140, 100, 60, fill="green", border="white")
    Label(destination, 330, 160, size=16, fill="white")
    Label(milesToGo, 330, 180, size=18, fill="white")
    # Make the scene darker if it is night-time.
    ### (HINT: Use the Inspector to see what was added to the canvas for this
    #          test case.)
    ### Place Your Code Here ###
    if isNightTime == True:
        Rect(0, 0, 400, 400, fill="black", opacity=50)
