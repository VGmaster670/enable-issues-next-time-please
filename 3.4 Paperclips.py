app.background = "burlyWood"

# laptop
Rect(240, 0, 160, 70, fill="gray")
Rect(320, 33, 50, 30, fill="dimGray")
Rect(300, 18, 90, 10)
Line(255, 23, 300, 23, lineWidth=10, dashes=(10, 5))
Line(260, 8, 400, 8, lineWidth=10, dashes=(10, 5))

# coffee mug
Circle(80, 10, 30, fill="saddleBrown", border="ivory", borderWidth=7)
Rect(46, 24, 10, 14, fill="ivory", rotateAngle=50)

# other stationery
Rect(300, 310, 100, 170, fill="darkSlateBlue", rotateAngle=50)
Rect(390, 340, 40, 20, fill="slateBlue", rotateAngle=50, align="center")
Line(384, 304, 260, 405, fill="indigo", lineWidth=10)
Line(334, 117, 380, 178, fill="steelBlue", lineWidth=5)
RegularPolygon(333, 116, 3, 3, fill="gray", rotateAngle=-160)
Oval(375, 165, 5, 20, fill="steelBlue", rotateAngle=-30)
Rect(-40, 110, 100, 150, fill="darkSalmon", rotateAngle=-20)
Rect(-30, 120, 80, 130, fill="white", rotateAngle=-20)
Polygon(60, 330, 100, 330, 100, 365, 95, 370, 60, 370, fill="gold")
Polygon(50, 330, 90, 330, 90, 365, 85, 370, 50, 370, fill="skyBlue", rotateAngle=30)

paperclips = Group()


def drawPaperclip(x, y, size, color, angle):
    # Draws a paperclip with the given attributes and adds it to the paperclips
    # group.
    clip = Group(
        Line(229, 160, 229, 220, fill=color, lineWidth=3),
        Circle(217, 220, 13.5, fill=None, border=color, borderWidth=2),
        Line(205, 220, 205, 160, fill=color, lineWidth=3),
        Rect(207, 160, 20, 59, fill="burlyWood"),
        Circle(214, 160, 11, fill=None, border=color, borderWidth=2),
        Line(224, 160, 224, 210, fill=color, lineWidth=3),
        Rect(207, 160, 15, 50, fill="burlyWood"),
        Circle(218, 210, 8, fill=None, border=color, borderWidth=2),
        Line(211, 210, 211, 175, fill=color, lineWidth=3),
        Rect(213, 175, 9, 35, fill="burlyWood"),
    )
    clip.centerX = x
    clip.centerY = y
    clip.width *= size
    clip.height *= size
    clip.rotateAngle = angle

    # Custom property to check if a clip has been picked up by the magnet.
    clip.isPickedUp = False

    paperclips.add(clip)


# Draws the paperclips.
drawPaperclip(210, 130, 0.5, "cadetBlue", 20)
drawPaperclip(270, 220, 0.7, "hotPink", 20)
drawPaperclip(75, 265, 0.7, "hotPink", 90)
drawPaperclip(315, 300, 0.5, "cadetBlue", -30)
drawPaperclip(85, 195, 0.7, "cadetBlue", -10)
drawPaperclip(154, 240, 0.5, "cadetBlue", -40)
drawPaperclip(120, 110, 0.5, "gold", -50)
drawPaperclip(200, 355, 0.5, "hotPink", 50)
drawPaperclip(197, 295, 0.5, "gold", -10)
drawPaperclip(150, 320, 0.7, "hotPink", -10)
drawPaperclip(285, 145, 0.5, "gold", 40)
drawPaperclip(140, 180, 0.7, "hotPink", 40)

magnet = Group(
    Rect(180, 175, 20, 15, fill="salmon"),
    Label("S", 190, 180, size=10, font="monospace"),
    Rect(180, 190, 20, 15, fill="gray"),
    Rect(180, 205, 20, 15, fill="cadetBlue"),
    Label("N", 190, 215, size=10, font="monospace"),
)


def onMouseMove(mouseX, mouseY):
    # Moves the magnet to the mouse's position.
    magnet.centerX = mouseX
    magnet.centerY = mouseY

    # For each paperclip, if it hits the magnet, pick it up. And if a paperclip is
    # picked up, set the clip's center coordinates to match the mouse's position.
    ### (HINT: The drawPaperclip function defines a custom property we can
    #          use to check if a clip has been picked up!)
    ### Place Your Code Here ###
    for paperclip in paperclips:
        if paperclip.hitsShape(magnet) == True:
            paperclip.isPickedUp = True
        if paperclip.isPickedUp == True:
            paperclip.centerX = mouseX
            paperclip.centerY = mouseY
