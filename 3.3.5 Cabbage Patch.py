app.background = gradient("sienna", "chocolate")


def drawCabbage(x, y):
    cabbage = Group(
        Star(200, 200, 50, 8, fill="mediumSeaGreen", rotateAngle=30, roundness=80),
        Star(200, 200, 40, 8, fill="lightGreen", rotateAngle=50, roundness=80),
        Star(200, 200, 30, 8, fill="paleGreen", rotateAngle=70, roundness=80),
    )
    cabbage.centerX = x
    cabbage.centerY = y


def drawCabbages():
    # Draw 5 rows of cabbages using a for loop. In each loop you should draw
    # 5 cabbages. They should all be 100 pixels apart.
    ### Place Your Code Here ###
    centerY = 0
    for _ in range(5):
        centerX = 0
        for _ in range(5):
            drawCabbage(centerX, centerY)
            centerX += 100
        centerY += 100
