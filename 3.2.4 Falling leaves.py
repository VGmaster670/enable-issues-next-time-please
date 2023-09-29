# background
app.background = gradient("white", "steelBlue", start="top-left")

# sun
Circle(50, 50, 30, fill=gradient("tomato", "orange"))

# grass
Rect(0, 320, 400, 80, fill=gradient("oliveDrab", "olive", start="top"))

# tree trunk
Polygon(
    216,
    320,
    207,
    283,
    214,
    250,
    207,
    205,
    212,
    180,
    192,
    164,
    191,
    196,
    182,
    235,
    186,
    258,
    172,
    320,
    fill=gradient("sienna", "saddleBrown", "sienna", start="left"),
)
Oval(
    195,
    225,
    8,
    40,
    fill=gradient(rgb(59, 19, 5), rgb(109, 49, 10)),
    border="black",
    borderWidth=0.5,
    rotateAngle=10,
    dashes=True,
)

# tree branches
Line(208, 180, 266, 112, fill=gradient("sienna", "peru", start="bottom"), lineWidth=4)
Line(248, 134, 237, 81, fill=gradient("sienna", "peru", start="bottom"), lineWidth=3)
Line(261, 143, 279, 153, fill=gradient("sienna", "peru", start="bottom"))
Line(233, 151, 280, 136, fill=gradient("sienna", "peru", start="bottom"), lineWidth=3)
Line(193, 200, 128, 141, fill=gradient("sienna", "peru", start="bottom"), lineWidth=4)
Line(143, 156, 138, 108, fill=gradient("sienna", "peru", start="bottom"), lineWidth=3)
Line(162, 172, 162, 124, fill=gradient("sienna", "peru", start="bottom"), lineWidth=3)
Line(152, 164, 106, 157, fill=gradient("sienna", "peru", start="bottom"), lineWidth=3)
Line(195, 173, 168, 82, fill=gradient("sienna", "peru", start="bottom"), lineWidth=4)
Line(188, 146, 194, 98, fill=gradient("sienna", "peru", start="bottom"), lineWidth=3)
Line(192, 116, 225, 90, fill=gradient("sienna", "peru", start="bottom"))
Line(184, 133, 150, 112, fill=gradient("sienna", "peru", start="bottom"), lineWidth=3)
Line(209, 218, 260, 180, fill=gradient("sienna", "peru", start="bottom"), lineWidth=4)

# leaves group
leaves = Group()


def drawLeaf(x, y, size, angle):
    # Draws a leaf centered at (x, y) with the given size and angle
    # and adds the new leaf to the leaves group.
    leaf = Group(
        Arc(50, 50, 40, 25, -90, 180, fill=gradient("orange", "maroon", start="left")),
        Arc(54, 50, 32, 25, 90, 180, fill=gradient("orange", "maroon", start="left")),
        Polygon(30, 50, 38, 50, 40, 56, fill="orange"),
        Line(30, 50, 70, 50, lineWidth=0.5),
        Line(60, 50, 52, 38, lineWidth=0.5),
        Line(60, 50, 52, 62, lineWidth=0.5),
        Line(43, 50, 36, 42, lineWidth=0.5),
        Line(43, 50, 36, 53, lineWidth=0.5),
    )
    leaf.centerX = x
    leaf.centerY = y
    leaf.width *= size
    leaf.height *= size
    leaf.rotateAngle = angle
    leaves.add(leaf)


# Draw the leaves on the tree.
drawLeaf(110, 165, 0.6, -30),
drawLeaf(118, 151, 0.5, 30),
drawLeaf(137, 102, 0.5, 100),
drawLeaf(130, 129, 0.6, 30),
drawLeaf(169, 140, 0.5, 150),
drawLeaf(160, 92, 0.7, 30),
drawLeaf(155, 154, 0.4, 30),
drawLeaf(183, 105, 0.5, 120),
drawLeaf(203, 130, 0.7, 150),
drawLeaf(200, 98, 0.5, 50),
drawLeaf(250, 96, 0.6, 130),
drawLeaf(229, 88, 0.5, 20),
drawLeaf(234, 119, 0.6, 25),
drawLeaf(270, 121, 0.5, 180),
drawLeaf(228, 141, 0.4, 45),
drawLeaf(279, 146, 0.3, 130),
drawLeaf(240, 160, 0.6, 190),
drawLeaf(239, 183, 0.5, 60),
drawLeaf(263, 186, 0.4, 190)


def onMousePress(mouseX, mouseY):
    # Drop each leaf in the leaves group by the appropriate
    # speed and increase their rotateAngle accordingly.
    # The leaf should move only if its center is above the grass.
    ### (HINT: Check the position of each leaf using its center coordinate.)
    ### Place Your Code Here ###
    for lofs in leaves:
        if lofs.centerY < 320:
            lofs.centerY += 8
            lofs.rotateAngle += 20
