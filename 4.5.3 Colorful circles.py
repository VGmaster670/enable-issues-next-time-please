import random

app.background = "darkBlue"
app.stepsPerSecond = 3

circles = Group()


def onStep():
    colors = ["lightCoral", "deepSkyBlue", "mediumPurple", "lavender", "crimson"]

    # Loop through the colors and add a circle for each color.
    # Each circle should have a random x and y coordinate between 0 and
    # 400 and a random radius between 5 and 20. (all inclusive.)
    ### Place Your Code Here ###
    for color in colors:
        circle = Circle(
            random.randint(0, 400),
            random.randint(0, 400),
            random.randint(5, 20),
            fill=color,
            border="black",
            borderWidth=3,
        )
        circles.add(circle)
    # Increases the size of all the circles until they get to 50, then
    # removes them.
    for circle in circles.children:
        circle.radius += 5
        if circle.radius > 50:
            circles.remove(circle)
