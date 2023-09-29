# background
Rect(0, 0, 400, 400, fill="tan")
Rect(25, 25, 350, 350, fill="white")
Label("NORRÅKER", 200, 70, size=36, bold=True)

# This defines a list of color options for the chair.
app.colorOptions = ["tan", "wheat", "silver", "lavenderBlush", "brown"]


def drawChair(colorIndex):
    # Get the chair color using the colorIndex parameter and the app.colorOptions
    # list. If the provided index does not exist in the list, make the chair white.
    ### (HINT: If the index is larger than 4, the index doesn't exist in the list.)
    ### Fix Your Code Here ###
    if colorIndex <= 4:
        color = app.colorOptions[colorIndex]
        colorIndex += 1
    else:
        color = "white"

    # This draws a chair using the color selected above.
    Rect(150, 200, 90, 30, fill=color, border="black")
    Rect(150, 200, 90, 10, fill=color, border="black")
    Rect(150, 300, 90, 15, fill=color, border="black")
    Polygon(
        135,
        125,
        150,
        125,
        170,
        200,
        150,
        360,
        135,
        360,
        150,
        200,
        fill=color,
        border="black",
    )
    Rect(225, 200, 15, 160, fill=color, border="black")
