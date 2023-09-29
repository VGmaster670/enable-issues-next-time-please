# background
Rect(0, 0, 400, 400, fill=gradient("turquoise", "paleTurquoise"))

# sun
Star(0, 0, 120, 60, fill="yellow", roundness=40)
Circle(0, 0, 90, fill=gradient("yellow", "khaki"))

# glass of cranberry juice
Rect(160, 150, 180, 250, fill="azure")
juice = Rect(170, 200, 160, 190, fill=gradient("tomato", "coral", start="bottom"))

# ice cubes
iceCube1 = Rect(180, 220, 40, 40, fill=rgb(229, 229, 229))
iceCube2 = Rect(240, 250, 30, 30, fill=rgb(229, 229, 229))
iceCube3 = Rect(200, 300, 35, 35, fill=rgb(229, 229, 229))

# straw
Rect(
    290,
    110,
    10,
    270,
    fill=gradient("tomato", "tomato", "tomato", "red", start="bottom"),
)
Rect(290, 100, 70, 10, fill="red")


def onMousePress(mouseX, mouseY):
    # An error occurs if you click too many times. Use the error message in
    # the console to figure out what is wrong and fix it!
    ### (HINT: Use an if statement to check the opacity of one of the ice cubes.)
    ### Fix Your Code Here ###
    if iceCube1.opacity >= 10:
        iceCube1.opacity -= 10
        iceCube2.opacity -= 10
        iceCube3.opacity -= 10
        juice.height += 2
        juice.top -= 2
