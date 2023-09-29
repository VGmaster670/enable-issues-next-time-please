# background
Rect(0, 0, 400, 400, fill=rgb(215, 160, 165))


def drawIceCream(iceCreamFlavorList):
    # ice cream cone
    Polygon(175, 290, 225, 290, 200, 360, fill="peru")

    # This stores the centerY of the next ice cream scoop.
    centerY = 275

    # Loop through the colors in the iceCreamFlavorList and draw each scoop onto
    # the cone.
    ### (HINT: The centerY of the ice cream scoop decreases by 25 on each
    #          loop iteration.)
    ### Fix Your Code Here ###
    for scoop in iceCreamFlavorList:
        Circle(200, centerY, 30, fill=scoop)
        centerY -= 25
