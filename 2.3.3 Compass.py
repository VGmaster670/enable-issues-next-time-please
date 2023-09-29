app.background = gradient("black", "darkSeaGreen", "darkSeaGreen")

magnet = Rect(
    170,
    20,
    60,
    360,
    fill=gradient("mediumBlue", "darkBlue", "darkRed", "crimson", start="top"),
)

# compass
Circle(200, 200, 130, fill=gradient("tan", "saddleBrown", start="left"))
Circle(200, 200, 110, fill=gradient("darkSlateGray", "darkSlateGray", "black"))
Star(200, 200, 90, 30, fill="silver", roundness=10)
Star(200, 200, 90, 4, fill=gradient("cornSilk", "darkGoldenrod"), roundness=15)

needle = Polygon(
    190,
    200,
    200,
    110,
    210,
    200,
    200,
    290,
    fill=gradient("crimson", "crimson", "black", "black", start="top"),
)

Circle(200, 200, 5, fill=gradient("silver", "grey"))


def onMousePress(mouseX, mouseY):
    # Rotate the magnet and needle.
    ### (HINT: To figure out how far to rotate, use the inspector and then
    #          click the mouse. How much do they rotate for 1 mouse press?)
    ### Place Your Code Here ###
    magnet.rotateAngle += 45
    needle.rotateAngle += 45
