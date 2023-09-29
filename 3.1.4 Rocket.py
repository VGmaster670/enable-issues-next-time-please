# space and stars
app.background = "black"
Star(80, 90, 2, 100, fill="yellow")
Star(360, 175, 2, 100, fill="yellow")
Star(220, 145, 2, 100, fill="yellow")
Star(322, 50, 2, 100, fill="yellow")
Star(30, 290, 2, 100, fill="yellow")

# ground
Rect(
    0,
    305,
    400,
    95,
    fill=gradient(rgb(250, 250, 250), rgb(220, 220, 220), start="bottom"),
)
Oval(
    360,
    320,
    40,
    7,
    fill=gradient(rgb(190, 190, 190), rgb(210, 210, 210), start="bottom"),
)
Oval(
    335,
    375,
    80,
    18,
    fill=gradient(rgb(190, 190, 190), rgb(210, 210, 210), start="bottom"),
)
Oval(
    40,
    330,
    60,
    10,
    fill=gradient(rgb(190, 190, 190), rgb(210, 210, 210), start="bottom"),
)

# support structure
Line(75, 360, 75, 130, fill="grey", lineWidth=30, dashes=(5, 10))
Line(55, 365, 55, 130, fill="grey", lineWidth=10)
Line(95, 365, 95, 130, fill="grey", lineWidth=10)
Line(95, 135, 200, 135, fill="grey", lineWidth=10)
Line(95, 190, 190, 190, fill="grey", lineWidth=7)
Line(95, 250, 180, 250, fill="grey", lineWidth=6)

# launch pad
Oval(200, 353, 170, 75, fill="darkSlateGrey")
Oval(200, 350, 170, 75, fill="slateGrey")

# rocket
rocket = Group(
    Polygon(198, 145, 202, 145, 200, 120, fill="crimson"),
    Polygon(176, 273, 155, 350, 190, 335, fill="crimson"),
    Polygon(224, 273, 245, 350, 210, 335, fill="crimson"),
    Oval(200, 250, 50, 200, fill=gradient("gainsboro", "darkGrey", start="right")),
    RegularPolygon(200, 150, 10, 3, fill=gradient("red", "crimson", start="top")),
    Rect(188, 340, 25, 10, fill="slateGrey"),
    Line(188, 340, 212, 340, fill="gold"),
    Circle(
        200,
        210,
        15,
        border="grey",
        borderWidth=4,
        fill=gradient("powderBlue", "lightCyan", "powderBlue", start="right-top"),
    ),
)

exhaust = Group()


def drawExhaust(x, y):
    smoke = Group(
        Circle(x - 10, y, 20, fill="grey", opacity=20),
        Circle(x, y, 20, fill="grey", opacity=20),
        Circle(x + 10, y, 20, fill="grey", opacity=20),
    )
    exhaust.add(smoke)


flame = Polygon(
    188,
    340,
    212,
    340,
    220,
    370,
    203,
    350,
    200,
    365,
    197,
    350,
    180,
    370,
    fill=gradient("orangeRed", "orange", start="top"),
)
flame.visible = False


def onMousePress(mouseX, mouseY):
    # On each mouse press make sure the flame is visible, draw the exhaust at the
    # bottom of the rocket, and move the rocket.
    ### Place your code here ###
    flame.visible = True
    drawExhaust(rocket.centerX, rocket.bottom)
    rocket.centerY -= 20
    flame.centerY -= 20


def onMouseRelease(mouseX, mouseY):
    # On mouse release, increase the width of the exhaust group by 40, and
    # increase its height by 20.
    ### Place your code here ###
    exhaust.width += 40
    exhaust.height += 20
