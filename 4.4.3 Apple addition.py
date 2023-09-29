# chalkboard
Rect(0, 0, 400, 400, fill=rgb(70, 70, 70), border="saddleBrown", borderWidth=15)
Rect(300, 375, 60, 10, fill="white")
Label("+", 200, 110, fill="white", size=60)
Label("=", 200, 230, fill="white", size=60)

# sum and summation statement
sumResult = Label("", 200, 290, fill="white", size=60)
statement = Label("", 200, 340, fill="white", size=12)

apples = Group()


def drawApple(x, y, color):
    # Draws an apple of the color and at the coordinates given.
    apples.add(
        Circle(x, y, 12, fill=color),
        Oval(x - 5, y - 12, 10, 5, fill="lightGreen", rotateAngle=20),
    )


def drawManyApples(num1, num2):
    # Draws multiple apples in a line.
    for i in range(num1):
        drawApple(i * 30 + 50, 50, "lightCoral")

    for i in range(num2):
        drawApple(i * 30 + 50, 170, "yellowGreen")


def onKeyPress(key):
    # Erases the chalkboard.
    apples.clear()

    # Asks for two one digit numbers.
    numRedApples = app.getTextInput("Give me a one digit number")
    numGreenApples = app.getTextInput("Give me another one digit number")

    # Using the two numbers inputted, draw the correct number of apples.
    # Modify the values of the sumResult label and the statement label
    # to describe the inputted math problem.
    ### (HINT: Use the helper function drawManyApples to help draw the apples.)
    ### Fix Your Code Here ###
    drawManyApples(int(numRedApples), int(numGreenApples))
    sumResult.value = int(numRedApples) + int(numGreenApples)
    statement.value = (
        numRedApples
        + " red apples and "
        + numGreenApples
        + " green apples makes "
        + str(sumResult.value)
        + " apples total!"
    )
