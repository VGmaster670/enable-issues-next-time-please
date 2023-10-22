import random

app.background = "gold"

infectedZone = Rect(0, 0, 1, 400, fill="crimson")
people = Group()


def drawPerson(cx, cy):
    head = Circle(cx, cy, 20, fill="tan")
    person = Group(
        head,
        # face
        Circle(cx + 8, cy - 5, 2),
        Circle(cx - 8, cy - 5, 2),
        Circle(cx, cy + 5, 5),
    )
    person.head = head

    # Randomly assign if the person is immune or not, and if they are draw
    # a blue "halo" behind them.
    isImmuneOptions = [True, False]
    person.isImmune = choice(isImmuneOptions)
    if person.isImmune:
        halo = Circle(person.centerX, person.centerY, 25, fill="skyBlue")
        person.add(halo)
        halo.toBack()

    people.add(person)


def createPeople():
    # Create 15 people randomly positioned in the canvas.
    for a in range(15):
        drawPerson(random.randint(0, 400), random.randint(0, 400))


def moveInfectedZone(x):
    # If we clicked to the right of the infected zone's right edge, increase the
    # width of the infected zone to be 1 pixel more than the x position.
    if not infectedZone.hits(x, 200):
        infectedZone.width = x + 1

    # If the infected zone is further right than a non-immune person's left
    # edge, that person's head should become green.
    ### Place Your Code Here ###
    for person in people.children:
        if not infectedZone.right > person.left and person.isImmune:
            person.head.fill = "green"


def onMousePress(mouseX, mouseY):
    # Call the moveInfectedZone function with the mouse's position as an argument.
    moveInfectedZone(mouseX)
