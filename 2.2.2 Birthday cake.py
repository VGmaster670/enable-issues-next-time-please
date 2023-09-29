# background
Rect(0, 0, 400, 150, fill="lightSteelBlue")
Rect(0, 150, 400, 250, fill="steelBlue")

# plate
Oval(200, 260, 360, 200, fill="lavender")

# cake
Oval(200, 240, 300, 170, fill="tan")
Rect(50, 200, 300, 40, fill="tan")
Oval(200, 200, 300, 170, fill="wheat")
Rect(50, 160, 300, 40, fill="wheat")
Oval(200, 160, 300, 170, fill="saddleBrown")


def onMousePress(mouseX, mouseY):
    # Draw a candle.
    ### Place Your Code Here ###
    Line(
        mouseX,
        mouseY,
        mouseX,
        mouseY - 50,
        fill=gradient("paleVioletRed", "pink", start="bottom"),
        lineWidth=8,
    )


def onMouseRelease(mouseX, mouseY):
    # Draw a flame for the candle.
    ### (HINT: A flame is a circle and a triangle. Which shape should be used
    #          to draw a triangle? Use the inspector tool to find the points!)
    ### Place Your Code Here ###
    Circle(mouseX, mouseY - 50, 5, fill="lightYellow")
    Polygon(
        mouseX - 5,
        mouseY - 50,
        mouseX,
        mouseY - 60,
        mouseX + 5,
        mouseY - 50,
        fill="lightYellow",
    )
