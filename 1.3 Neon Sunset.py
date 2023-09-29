Rect(0, 0, 400, 400, fill=gradient("black", rgb(90, 30, 140), start="top"))

# stars and sun
Star(250, 30, 10, 4, fill="hotPink", roundness=10)
Star(45, 130, 10, 4, fill="hotPink", roundness=10)
Star(370, 150, 10, 4, fill="hotPink", roundness=10)
Circle(200, 300, 100, fill=gradient("yellow", rgb(255, 80, 220), start="top"))

# Draw the comet.
### Place Your Code Here ###
Polygon(40, 0, 40, 40, 345, 95, fill=gradient("black", "magenta", start="left"))
Star(345, 95, 30, 6, fill="hotPink", roundness=10)
Star(345, 95, 15, 4, fill="orange", roundness=30)
# Then draw the mountains.
### Place Your Code Here ###
Polygon(
    10,
    355,
    130,
    355,
    70,
    255,
    fill=gradient("blueViolet", "magenta", start="bottom-left"),
)
Polygon(
    300,
    355,
    345,
    260,
    400,
    355,
    fill=gradient("darkOrchid", "slateBlue", start="top-left"),
)
Polygon(
    235,
    355,
    310,
    230,
    385,
    355,
    fill=gradient("magenta", "darkViolet", start="top-left"),
)
# ground
Rect(0, 350, 400, 50, fill=gradient("blueViolet", "indigo", start="top"))
