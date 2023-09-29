import random

app.stepsPerSecond = 5
app.nextRadius = 0

Rect(0, 0, 400, 400)


def onStep():
    if app.nextRadius < 200:
        # Increases the radius by 5.
        app.nextRadius += 5

        # Define these variables to generate new random values for the next
        # circle. Borders are at most 50 and dash values are at most 100.
        ### (HINT: redGreen is used in an rgb so it can't be bigger than 255!)
        ### Fix Your Code Here ###
        redGreen = random.randint(0, 255)
        newBorderWidth = random.randint(0, 50)
        dashWidth = random.randint(0, 100)
        dashSpace = random.randint(0, 100)

        # Draws the next circle with the values generated above.
        Circle(
            200,
            200,
            app.nextRadius,
            fill=None,
            border=rgb(redGreen, 255 - redGreen, 255),
            borderWidth=newBorderWidth,
            dashes=(dashWidth, dashSpace),
        )
