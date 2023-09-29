app.background = "lightCyan"

app.cheesesEaten = 0

# wall
Rect(-2, 290, 404, 30, fill=rgb(245, 245, 245), border="black")
Rect(60, 50, 130, 150, fill="skyBlue", border="saddleBrown", borderWidth=10)
Rect(70, 160, 110, 30, fill="seaGreen")
Line(125, 50, 125, 200, fill="saddleBrown", lineWidth=5)
Line(60, 125, 190, 125, fill="saddleBrown", lineWidth=5)

# floor
Rect(0, 320, 400, 80, fill=gradient("wheat", "burlyWood", start="bottom"))
Line(200, 320, 200, 400, lineWidth=400, dashes=(0.5, 22))

# table
table = Polygon(
    -2, 402, -2, 360, 95, 275, 402, 275, 402, 402, fill="tan", border="black"
)

# mouse hole
Circle(20, 305, 10)
Rect(10, 305, 20, 15)

# mouse eyes
eyes = Group(Circle(19, 310, 1, fill="white"), Circle(22, 310, 1, fill="white"))

# cheese crumbs
Circle(80, 350, 2, fill="lemonChiffon")
Circle(114, 368, 2, fill="lemonChiffon")
Circle(126, 352, 2, fill="lemonChiffon")
Circle(175, 307, 2, fill="darkOrange")
Circle(186, 318, 2, fill="darkOrange")
Circle(216, 296, 2, fill="darkOrange")
Circle(244, 314, 2, fill="darkOrange")
Circle(313, 357, 2, fill="khaki")
Circle(332, 360, 2, fill="khaki")

# cheeses
cheeseWheel = Group(
    Oval(90, 370, 120, 25, fill="lemonChiffon", border="black"),
    Rect(30, 350, 120, 21, border="black", dashes=(21, 120), fill="lemonChiffon"),
    Oval(90, 350, 120, 25, fill="lemonChiffon", border="black"),
)

cheeseBlock = Group(
    Rect(160, 290, 80, 38, fill="darkOrange", border="black"),
    Polygon(
        159.5, 292, 170, 280, 250, 280, 240, 292, fill="darkOrange", border="black"
    ),
    Polygon(238, 290, 249, 279, 250, 317, 238, 329, fill="darkOrange", border="black"),
)

cheeseWedge = Group(
    Rect(290, 345, 80, 25, fill="khaki", border="black"),
    Polygon(
        289, 347, 305, 330, 372, 346, fill="khaki", border="black", borderWidth=1.5
    ),
)

mouse = Group(
    Line(200, 188, 190, 178, fill="pink", lineWidth=3),
    Oval(200, 200, 25, 30, fill="gainsboro", border="black", borderWidth=0.5),
    Circle(190, 205, 6, fill="darkGrey", border="black", borderWidth=1),
    Circle(210, 205, 6, fill="darkGrey", border="black", borderWidth=1),
    Polygon(
        188,
        210,
        195,
        205,
        205,
        205,
        212,
        210,
        200,
        225,
        fill="gainsboro",
        border="black",
        borderWidth=0.5,
    ),
    Rect(196, 204, 8, 4, fill="gainsboro"),
    Circle(200, 224, 2, fill="hotPink"),
    Circle(195, 212, 1.5),
    Circle(205, 212, 1.5),
)
mouse.visible = False
mouse.width = 25


def onMousePress(mouseX, mouseY):
    # When the table is clicked on, move the (animal) mouse from its hole onto
    # the table.
    ### (HINT: The mouse's centerY should be 310.)
    ### Place your code here ###
    if table.hits(mouseX, mouseY) == True:
        mouse.centerX = 120
        mouse.centerY = 310
        mouse.visible = True
        eyes.visible = False


def eatCheese(cheese):
    mouse.width += 3
    app.cheesesEaten += 1
    cheese.clear()


def onMouseRelease(mouseX, mouseY):
    # If the (computer) mouse is released on any of the cheese groups, eat the
    # cheese.
    ### (HINT: Call the eatCheese function with the proper cheese group!)
    ### Place your code here ###
    if cheeseWheel.hits(mouseX, mouseY) == True:
        eatCheese(cheeseWheel)
    if cheeseBlock.hits(mouseX, mouseY) == True:
        eatCheese(cheeseBlock)
    if cheeseWedge.hits(mouseX, mouseY) == True:
        eatCheese(cheeseWedge)
    # If there is still uneaten cheese, hides the mouse and makes the eyes
    # reappear in the mousehole.
    if app.cheesesEaten < 3:
        eyes.visible = True
        mouse.visible = False
