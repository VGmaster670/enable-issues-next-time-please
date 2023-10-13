app.background = gradient("white", "wheat", start="top")

app.fruitsToBlend = []


def drawOrange(cx, cy, o):
    o.add(
        Circle(cx, cy, 20, fill="khaki", border="darkOrange", borderWidth=2),
        Circle(cx, cy, 16, fill="orange"),
        Star(cx, cy, 18, 10, fill="khaki", roundness=15),
    )
    o.juiceColor = "orange"


def drawGrapes(cx, cy, g):
    g.add(
        Arc(85, 35, 30, 30, -40, 30, fill="green"),
        Circle(85, 35, 6, fill="darkMagenta"),
        Circle(93, 33, 6, fill="purple"),
        Circle(78, 40, 6, fill="purple"),
        Circle(90, 42, 6, fill="darkOrchid"),
        Circle(85, 45, 6, fill="darkOrchid"),
        Circle(92, 50, 6, fill="orchid"),
    )
    g.centerX = cx
    g.centerY = cy
    g.juiceColor = "purple"


def drawWatermelon(cx, cy, w):
    w.add(
        Arc(cx, cy, 40, 40, 30, 180, fill="yellowGreen"),
        Arc(cx, cy, 34, 34, 30, 180, fill="lemonChiffon"),
        Arc(cx, cy, 30, 30, 30, 180, fill="darkSalmon"),
    )
    w.juiceColor = "darkSalmon"


orange = Group()
grapes = Group()
watermelon = Group()
drawOrange(48, 45, orange)
drawGrapes(85, 40, grapes)
drawWatermelon(105, 40, watermelon)

# basket
Polygon(20, 45, 130, 45, 120, 55, 30, 55, fill="saddleBrown")
Polygon(30, 55, 120, 55, 110, 85, 40, 85, fill="cornSilk", border="tan", borderWidth=3)
Polygon(50, 45, 100, 45, 75, 75, fill="tan")
Line(35, 70, 115, 70, fill="tan", lineWidth=3)
Line(57, 57, 62, 82, fill="tan", lineWidth=3)
Line(93, 57, 89, 83, fill="tan", lineWidth=3)
Line(30, 45, 25, 0, fill="tan", lineWidth=3)
Line(120, 45, 125, 0, fill="tan", lineWidth=3)

# juicer
funnel = Group(
    Rect(250, 50, 80, 15, fill=None, border="oliveDrab", borderWidth=3),
    Polygon(260, 65, 320, 65, 310, 100, 270, 100, fill="oliveDrab"),
)
Polygon(
    240,
    100,
    340,
    100,
    340,
    350,
    115,
    350,
    115,
    300,
    240,
    300,
    240,
    100,
    fill="yellowGreen",
)
Line(243, 150, 337, 150, fill="white", lineWidth=3)

powerButton = Circle(290, 270, 20, fill="white", border="oliveDrab", borderWidth=5)
Line(290, 252, 290, 270, fill="oliveDrab", lineWidth=6)
Polygon(
    242,
    140,
    242,
    165,
    190,
    165,
    190,
    140,
    fill=None,
    border="yellowGreen",
    borderWidth=3,
)
Polygon(190, 148, 190, 157, 160, 157, 160, 148, fill="yellowGreen")
Polygon(
    242,
    190,
    242,
    300,
    170,
    300,
    170,
    210,
    160,
    190,
    fill=None,
    border="white",
    borderWidth=3,
)

# table
Rect(0, 350, 400, 25, fill="tan")


def onMousePress(mouseX, mouseY):
    newFruit = Group()
    if orange.contains(mouseX, mouseY):
        drawOrange(275, 55, newFruit)
    if grapes.contains(mouseX, mouseY):
        drawGrapes(295, 55, newFruit)
    if watermelon.contains(mouseX, mouseY):
        drawWatermelon(305, 55, newFruit)

    # When the new fruit has some children, add it to the fruitsToBlend list and
    # move the funnel in front of it.
    ### Place Your Code Here ###
    if len(newFruit.children) > 0:
        app.fruitsToBlend.append(newFruit)
        funnel.toFront()
    # When the power button is clicked on, blend the fruits by clearing them and
    # drawing a rectangle in the cup with an appropriate opacity and color.
    ### Place Your Code Here ###
    if powerButton.contains(mouseX, mouseY):
        for fruit in app.fruitsToBlend:
            fruit.clear()
            Rect(175, 210, 65, 90, fill=fruit.juiceColor, opacity=30)
        app.fruitsToBlend = []
