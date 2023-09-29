app.background = "navy"

hippoFace = Group(
    Circle(240, 150, 20, fill="lightPink"),
    Circle(160, 150, 20, fill="lightPink"),
    Oval(200, 180, 130, 100, fill="lightPink"),
    Oval(200, 220, 150, 120, fill="lightPink"),
    Oval(180, 230, 12, 20, fill="hotPink"),
    Oval(220, 230, 12, 20, fill="hotPink"),
    Circle(170, 185, 24, fill="white"),
    Circle(230, 185, 24, fill="white"),
    Circle(170, 185, 8),
    Circle(230, 185, 8),
)
hippoFace.height *= 0.9

# hippo
Group(
    Oval(200, 250, 220, 160, fill="lightCoral"),
    Circle(140, 330, 30, fill=rgb(205, 90, 90)),
    Circle(260, 330, 30, fill=rgb(205, 90, 90)),
    Rect(200, 330, 180, 30, fill="navy", align="top"),
    hippoFace,
    Rect(0, 235, 400, 250, fill="navy", opacity=90),
)


def drawBubbles():
    cx = 0
    cy = 0
    for i in range(250):
        cx += 35
        if cx > 410:
            cx = i / 10
            cy += 20

        bubbles.add(Circle(cx, cy, 20, fill="lightBlue", opacity=80))


bubbles = Group()
drawBubbles()


def onMouseMove(mouseX, mouseY):
    # onMouseMove is discussed in the optional notes:
    # 2.2.5 onMouseMove and onMouseDrag

    farthestLeftBubble = None

    # Find the bubble that is farthest to the left by looping through the group
    # and updating the value of farthestLeftCircle if the looping variable is
    # farther left.
    ### (HINT: If the farthestLeftBubble is None, you should set it to the
    #          looping variable.)
    ### Place Your Code Here ###
    for bubble in bubbles:
        if farthestLeftBubble == None:
            farthestLeftBubble = bubble
        elif farthestLeftBubble.left > bubble.left:
            farthestLeftBubble = bubble
    # Hide the circle that is farthest to the left.
    if farthestLeftBubble != None:
        farthestLeftBubble.visible = False
