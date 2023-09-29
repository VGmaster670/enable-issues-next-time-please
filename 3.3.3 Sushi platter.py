app.background = gradient("lightPink", "whiteSmoke", rgb(170, 210, 50), start="top")

# possible sushi fillings
app.fillings = ["salmon", "oliveDrab", "gold", "darkGreen", "hotPink"]

# sushi platter
Polygon(140, 130, 10, 240, 350, 340, 400, 297, 400, 207, fill=rgb(255, 245, 100))
Polygon(10, 240, 10, 270, 350, 370, 350, 340, fill="gold")
Polygon(350, 340, 350, 370, 400, 327, 400, 297, fill="peru")

# chopsticks
Polygon(100, 330, 85, 345, 100, 350, 115, 335, fill="green")
Polygon(85, 345, 85, 350, 100, 355, 100, 350, fill="darkGreen")
Polygon(100, 350, 100, 355, 115, 340, 115, 335)
Line(70, 330, 255, 400, lineWidth=5)
Line(75, 325, 270, 390, lineWidth=4.5)


def drawSushi(cx, cy, fillingColor):
    # Draws a single sushi with the specified filling.
    sushi = Group(
        Oval(200, 200, 50, 40, rotateAngle=10),
        Polygon(175, 200, 225, 200, 225, 225, 175, 225),
        Oval(200, 225, 50, 40, rotateAngle=10),
        Oval(200, 200, 45, 35, fill="white", rotateAngle=10),
        Oval(200, 200, 20, 15, fill=fillingColor, rotateAngle=10),
    )
    sushi.centerX = cx
    sushi.centerY = cy


def drawThreeSushi(colorIndex1, colorIndex2, colorIndex3):
    # Draw 3 sushi with filling. The app.fillings list has the possible filling
    # colors, and the colorIndex parameters are indexes for that list.
    ### (HINT: We provide a drawSushi function above. It takes the sushi
    #          position and color as inputs.)
    ### (HINT: The center positions of the sushis are: (160, 180), (230, 240),
    #          and (320, 220).)
    ### Place Your Code Here ###

    drawSushi(160, 180, app.fillings[colorIndex1])
    drawSushi(230, 240, app.fillings[colorIndex2])
    drawSushi(320, 220, app.fillings[colorIndex3])
