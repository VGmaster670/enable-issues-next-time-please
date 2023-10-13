app.background = "cornFlowerBlue"

# Stores the currently selected sprinkle.
app.selected = None

# table and sprinkle bottle
Rect(0, 150, 400, 250, fill="white")
Oval(395, 245, 70, 100, fill="gainsboro", rotateAngle=45)
Rect(
    410,
    210,
    90,
    60,
    border="darkGrey",
    rotateAngle=315,
    align="center",
    fill=gradient("gold", "mediumAquamarine", "cornFlowerBlue", start="left"),
)
Oval(
    380,
    240,
    30,
    60,
    fill=gradient("crimson", "gold", start="left"),
    border="darkGrey",
    rotateAngle=315,
)
Oval(375, 245, 25, 40, fill="white", border="darkGrey", rotateAngle=315)
Oval(370, 250, 25, 40, fill="white", border="darkGrey", rotateAngle=315)

# cupcake
Oval(200, 225, 150, 65, fill="gainsboro")
Oval(200, 220, 100, 30, fill=rgb(125, 65, 15))
Polygon(125, 150, 275, 150, 250, 220, 150, 220, fill=rgb(125, 65, 15))
Oval(200, 150, 150, 60, fill=rgb(105, 55, 10))
Oval(200, 140, 130, 55, fill="linen", border="white"),
Oval(202, 125, 105, 45, fill="linen", border="white"),
Oval(205, 115, 80, 35, fill="linen", border="white")
Oval(205, 105, 50, 25, fill="linen", border="white")
Line(205, 60, 205, 65, fill="white"),
Line(205, 65, 205, 103, fill="lightSalmon", lineWidth=10),
Line(205, 65, 205, 103, fill="coral", lineWidth=10, dashes=(4, 4))

sprinkles = Group(
    Circle(80, 330, 7, fill="mediumPurple"),
    Circle(180, 330, 7, fill="salmon"),
    Circle(130, 305, 7, fill="gold"),
    Circle(60, 310, 7, fill="mediumAquamarine"),
    Circle(125, 360, 7, fill="cornFlowerBlue"),
    RegularPolygon(260, 360, 8, 5, fill="mediumAquamarine"),
    RegularPolygon(290, 310, 8, 3, fill="coral"),
    RegularPolygon(320, 340, 8, 6, fill="salmon"),
    RegularPolygon(240, 320, 8, 4, fill="crimson"),
    RegularPolygon(300, 370, 8, 4, fill="cornFlowerBlue"),
    Line(195, 305, 205, 315, fill="mediumPurple", lineWidth=6),
    Line(210, 370, 200, 380, fill="coral", lineWidth=6),
    Line(80, 365, 90, 375, fill="cornFlowerBlue", lineWidth=6),
    Line(40, 350, 30, 360, fill="mediumAquamarine", lineWidth=6),
    Line(25, 315, 35, 325, fill="salmon", lineWidth=6),
    Star(350, 370, 10, 5, fill="mediumPurple"),
    Star(380, 330, 10, 5, fill="crimson"),
    Star(350, 310, 10, 5, fill="gold"),
)


def onMousePress(mouseX, mouseY):
    # If the selected sprinkle is clicked on, let go of it. If any other sprinkle
    # is clicked on, that sprinkle should become the selected sprinkle.
    ### (HINT: We should let go of something by making it no longer selected.)
    ### Place Your Code Here ###
    for sprinkle in sprinkles:
        if sprinkle.hits(mouseX, mouseY):
            app.selected = sprinkle
        elif sprinkle.hits(mouseX, mouseY):
            app.selected = None


def onMouseMove(mouseX, mouseY):
    # Moves the selected sprinkle to the mouse's coordinates.
    if app.selected != None:
        app.selected.centerX = mouseX
        app.selected.centerY = mouseY
