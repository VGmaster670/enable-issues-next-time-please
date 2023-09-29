app.background = gradient(rgb(150, 225, 175), rgb(95, 180, 155), start="top")

leftArm = Line(200, 190, 140, 100, fill=rgb(70, 75, 75), lineWidth=5)
rightArm = Line(200, 190, 260, 100, fill=rgb(70, 75, 75), lineWidth=5)
stickPerson = Group(
    Circle(200, 140, 30, fill=rgb(70, 75, 75)),
    Line(200, 170, 200, 275, fill=rgb(70, 75, 75), lineWidth=6),
    Line(200, 275, 150, 325, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 275, 250, 325, fill=rgb(70, 75, 75), lineWidth=5),
    leftArm,
    rightArm,
)
stickPerson.bottom = 325

# pull up bar
Line(
    50,
    100,
    350,
    100,
    fill=gradient("gainsboro", "silver", "gainsboro", start="top"),
    lineWidth=6,
)
Line(
    50,
    100,
    50,
    400,
    fill=gradient("gainsboro", "silver", "gainsboro", start="top"),
    lineWidth=6,
)
Line(
    350,
    100,
    350,
    400,
    fill=gradient("gainsboro", "silver", "gainsboro", start="top"),
    lineWidth=6,
)

pullUpCounter = Label(0, 100, 60, fill=rgb(70, 75, 75), size=25)


def onMousePress(mouseX, mouseY):
    # Increase the number of pull-ups done.
    ### Place Your Code Here ###
    pullUpCounter.value += 1
    # Move the stickPerson group up.
    ### (HINT: Use the bottom property!)
    ### Place Your Code Here ###
    stickPerson.bottom = 250
    # Then change the left and right arm, so they are gripping the bar.
    ### (HINT: Change the y2 values of the arms.)
    ### Place Your Code Here ###
    leftArm.y2 = 100
    rightArm.y2 = 100


def onMouseRelease(mouseX, mouseY):
    # Move the stickPerson group down.
    ### (HINT: Use the bottom property!)
    ### Place Your Code Here ###
    stickPerson.bottom = 325
    # Then change the left and right arm, so they are gripping the bar.
    ### (HINT: Reset the y2 values of the arms.)
    ### Place Your Code Here ###
    leftArm.y2 = 100
    rightArm.y2 = 100
