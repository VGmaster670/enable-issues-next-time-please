sky = Rect(0, 0, 400, 330, fill=gradient("lightCyan", "lightSkyBlue", start="top"))
ground = Rect(0, 330, 400, 70, fill="mediumSeaGreen")

leaves = Star(200, 150, 150, 16, fill=rgb(200, 240, 80), roundness=90)

# Define this custom property to keep track of the amount of green in the leaves.
### Fix Your Code Here ###
leaves.green = 240

# tree trunk and limbs
Polygon(200, 100, 165, 350, 235, 350, fill="saddleBrown")
Polygon(200, 300, 200, 250, 300, 175, fill="saddleBrown")
Polygon(200, 300, 200, 250, 100, 150, fill="saddleBrown")
Polygon(200, 200, 200, 175, 125, 100, fill="saddleBrown")
Polygon(200, 250, 200, 200, 275, 100, fill="saddleBrown")


def onMousePress(mouseX, mouseY):
    # If the green in the leaves is greater than 100, decrease it.
    # Otherwise, change the color of the sky and ground to match autumn colors!
    ### (HINT: Use rgb and your custom property to change the fill of the
    #          leaves.)
    ### Place Your Code Here ###
    if leaves.green > 100:
        leaves.green -= 10
        leaves.fill = rgb(200, leaves.green, 80)
    else:
        sky.fill = gradient("lightYellow", "coral", start="top")
        ground.fill = "chocolate"
