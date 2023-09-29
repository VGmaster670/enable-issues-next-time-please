import random

app.background = gradient("skyBlue", "lightBlue", "skyBlue", start="top")

# fallen snow
Oval(60, 360, 300, 200, fill=gradient("white", "snow", "white"))
Oval(180, 400, 300, 200, fill=gradient("white", "snow", "white"))
Oval(350, 380, 300, 200, fill=gradient("white", "snow", "white"))

# snowman arms
Line(100, 220, 120, 210, fill="saddleBrown")
Line(60, 220, 40, 210, fill="saddleBrown")
Line(114, 212, 116, 205, fill="saddleBrown")
Line(47, 212, 50, 205, fill="saddleBrown")

# head and body
Circle(80, 195, 20, fill=gradient("white", "snow", "white"))
Circle(80, 220, 25, fill=gradient("white", "snow", "white"))
Circle(80, 245, 30, fill=gradient("white", "snow", "white"))

# buttons
Circle(80, 220, 5)
Circle(80, 245, 5)

# face
RegularPolygon(80, 200, 5, 3, fill="orange")
Circle(75, 190, 3)
Circle(85, 190, 3)
Rect(80, 185, 20, 30, fill=gradient("black", "gray", start="top"), align="bottom")
Rect(80, 185, 30, 10, align="bottom")
RegularPolygon(94, 173, 6, 3, fill="green")
Circle(89, 177, 3, fill="red")


def onMousePress(mouseX, mouseY):
    # Define the random variables to be used to create a new snowflake.
    ### (HINT: Make sure to define them in the order radius, point,
    #          roundness, and then opacity so that the autograder grades
    #          properly!)
    ### (HINT: The radius is between 6-12, points is between 8-20, roundness is
    #          between 0-80, and opacity is between 60-100 (all inclusive).)
    ### Place Your Code Here ###
    radius = random.randint(6, 12)
    point = random.randint(8, 20)
    roundness = random.randint(0, 80)
    opacity = random.randint(60, 100)
    # Use the variables to create a new snowflake.
    ### Place Your Code Here ###
    Star(
        mouseX,
        mouseY,
        radius,
        point,
        roundness=roundness,
        opacity=opacity,
        fill=gradient("white", "snow", "white", start="center"),
    )
