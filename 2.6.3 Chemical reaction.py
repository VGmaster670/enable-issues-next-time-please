# background
Rect(0, 0, 400, 320, fill="lavender")

# table
Rect(0, 320, 400, 80, fill="gray")

# flask and stopper
Polygon(
    80,
    320,
    320,
    320,
    250,
    170,
    250,
    100,
    150,
    100,
    150,
    170,
    fill="aliceBlue",
    border="white",
    borderWidth=15,
)
Rect(165, 90, 70, 40, fill="saddleBrown")

# hidden spill
spill = Polygon(
    165,
    0,
    165,
    165,
    102,
    305,
    298,
    305,
    235,
    165,
    235,
    0,
    fill=rgb(170, 170, 220),
    visible=False,
)

# liquid
liquid = Polygon(104, 305, 296, 305, 235, 170, 165, 170, fill=rgb(170, 170, 220))
liquid.pressure = 0

# bubbles
Circle(220, 230, 20, fill="white", opacity=10)
Circle(190, 260, 10, fill="white", opacity=10)


def onMousePress(mouseX, mouseY):
    # Move the liquid's bottom up or down by 5 pixels, based on its current
    # position.
    ### Place Your Code Here ###
    if liquid.bottom == 305:
        liquid.bottom -= 5
    else:
        liquid.bottom += 5
    # Every mouse press, the pressure should increase. When it gets to 10,
    # the liquid should explode out of the flask.
    ### (HINT: We defined a custom property and spill variable above that
    #          might be helpful.)
    ### Place Your Code Here ###
    liquid.pressure += 1
    if liquid.pressure == 10:
        spill.visible = True
