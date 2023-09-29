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
    centerX = 0
    for cabbage in range(5):
        drawCabbage(centerX, 0)
        centerX += 100
    centerX = 0
    for cabbage in range(5):
        drawCabbage(centerX, 100)
        centerX += 100
    centerX = 0
    for cabbage in range(5):
        drawCabbage(centerX, 200)
        centerX += 100
    centerX = 0
    for cabbage in range(5):
        drawCabbage(centerX, 300)
        centerX += 100
    centerX = 0
    for cabbage in range(5):
        drawCabbage(centerX, 400)
        centerX += 100

    ### Intended Solution ###
    # centerY=0
    # for a in range(5):
    #     centerX=0
    #     for b in range(5):
    #         drawCabbage(centerX,centerY)
    #         centerX+=100
    #     centerY+=100
