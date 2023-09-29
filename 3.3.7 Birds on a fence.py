# background
app.background = gradient("orange", "lightCoral")

# clouds
cloud1 = Star(75, 121, 50, 550, roundness=45, opacity=30, fill="white")
cloud2 = Star(160, 90, 60, 550, roundness=45, opacity=30, fill="white")
cloud3 = Star(306, 260, 60, 550, roundness=45, opacity=30, fill="white")
cloud1.width = 300
cloud2.width = 400
cloud3.width = 500

# sun
Circle(200, 200, 70, fill=gradient("tomato", "orangeRed"))

# fence
Line(0, 80, 400, 80, lineWidth=1)
Line(400, 180, 0, 180, lineWidth=1)
Line(0, 280, 400, 280, lineWidth=1)
Line(5, 56, 5, 400, lineWidth=8)
Line(395, 56, 395, 400, lineWidth=8)
Line(0, 60, 12, 60)
Line(0, 65, 20, 65)
Line(388, 60, 400, 60)
Line(380, 65, 400, 65)


def shiftBirds(birdList):
    # Change the centerXs of each bird in the list to arrange them
    # appropriately on the wire.
    birdGap = 400 / (len(birdList) + 1)
    ### (HINT: Loop through the list, and use the local variable birdGap
    #          combined with the index in order to space out the birds.)
    ### Place Your Code Here ###
    for index in range(len(birdList)):
        birdList[index].centerX = birdGap * (index + 1)


def addNewBird(birdList, yVal, prevDir):
    # Adds a new bird (with the correct direction) to the given list.

    # bird
    bird = Group(
        Circle(200, 202, 7),
        Oval(200, 220, 20, 35),
        Oval(209, 219, 7, 15),
        Oval(191, 219, 7, 15),
        Polygon(197, 234, 203, 234, 205, 255, 195, 255),
    )

    # beaks
    rightBeak = Polygon(206, 198, 210, 200, 206, 204)
    leftBeak = Polygon(194, 198, 190, 200, 194, 204)
    rightBeak.visible = False
    leftBeak.visible = False

    # Add the correct beak to the bird (and toggle that beak's visibility)
    # depending on its direction. Change the bird's rotateAngle and set its
    # direction as a custom property.
    ### (HINT: The bird should have the opposite direction to the direction
    #          of the most recent bird in the list, given by prevDir.)
    ### (HINT: Use the Inspector to figure out what the correct rotateAngle
    #          is for each direction)
    ### Place Your Code Here ###
    if prevDir == "left":
        bird.add(rightBeak)
        rightBeak.visible = True
        bird.direction = "right"
        bird.rotateAngle = 5
    else:
        bird.add(leftBeak)
        leftBeak.visible = True
        bird.direction = "left"
        bird.rotateAngle = -5
    # Set the bird's centerY, add it to the inputted list and shift the birds
    # on the wire using the previously written helper function.
    ### Place Your Code Here ###
    bird.centerY = yVal
    birdList.append(bird)
    shiftBirds(birdList)


# lists of birds for each line
app.line1 = []
app.line2 = []
app.line3 = []

# initial birds
addNewBird(app.line1, 80, "left")
addNewBird(app.line2, 180, "right")
addNewBird(app.line3, 280, "left")


def onMousePress(x, y):
    # Adds a new bird to a wire when the mouse is clicked above it
    if y < 80:
        addNewBird(app.line1, 80, app.line1[-1].direction)
    elif 80 < y < 180:
        addNewBird(app.line2, 180, app.line2[-1].direction)
    elif 180 < y < 280:
        addNewBird(app.line3, 280, app.line3[-1].direction)
