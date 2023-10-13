##################
##### Part 1 #####
##################

import random

app.background = "gold"

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

    #### START OF BLOCK DRAW_PERSON ####

    # Randomly assign if the person is immune or not, and if they are draw
    # a blue "halo" behind them.
    ### (HINT: Make sure to add the halo to the person Group.)
    ### Place Your Code Here ###
    isImmuneOptions = [True, False]
    person.isImmune = choice(isImmuneOptions)
    if person.isImmune:
        halo = Circle(person.centerX, person.centerY, 25, fill="skyBlue")
        people.add(halo)

    #### END OF BLOCK ####

    people.add(person)


def createPeople():
    #### START OF BLOCK CREATE_PEOPLE ####

    # Create 15 people randomly positioned in the canvas.
    ### Place Your Code Here ###
    for a in range(15):
        drawPerson(random.randint(0, 400), random.randint(0, 400))

    #### END OF BLOCK ####
