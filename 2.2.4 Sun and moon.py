sky = Rect(0, 0, 400, 400, fill='midnightBlue')

moon = Circle(200, 170, 100, fill='gold')
sun = Circle(175, 140, 100, fill='midnightBlue')

# cloud
Circle(240, 240, 30, fill='white')
Circle(200, 260, 45, fill='white')
Circle(150, 270, 30, fill='white')
Circle(250, 290, 30, fill='white')
Circle(275, 260, 40, fill='white')

def onMousePress(mouseX, mouseY):
    # Make it daytime by changing the fills of the globals.
    ### Place Your Code Here ###
    sky.fill="skyblue"
    moon.fill="skyBlue"
    sun.fill=gradient("yellow","gold")

def onMouseRelease(mouseX, mouseY):
    # Make it nighttime by changing the fills back.
    ### Place Your Code Here ###
    sky.fill="midnightBlue"
    moon.fill="gold"
    sun.fill="midnightBlue"
