app.background = "black"
app.stepsPerSecond = 12

app.alphabet = "abcdefghijklmnopqrstuvwxyz"
app.currentIndex = 0

letters = Group()


def drawLetters():
    # Draws the letters evenly spaced and add them to the letters group.
    spacing = 395 / len(app.alphabet)
    for i in range(len(app.alphabet)):
        x = 10 + i * spacing
        letters.add(Label(app.alphabet[i], x, 200, fill="white", size=15, bold=True))


drawLetters()


def onStep():
    # Get the current letter by using the alphabet and app.currentIndex.
    ### Place Your Code Here ###
    currentLetter = app.alphabet[app.currentIndex % 26]

    # Loops over the letters Group.
    for letter in letters:
        # Set the currentLetter's fill to red and increase its size.
        ### (HINT: Compare letter.value to currentLetter to find when
        #          letter is the currentLetter.)
        ### Place Your Code Here ###
        if letter.value == currentLetter:
            letter.fill = "red"
            letter.size = 36
        # Set all other letters' fills to white and decrease their size.
        ### Fix Your Code Here ###
        if letter.value != currentLetter:
            letter.fill = "white"
            if letter.size > 15:
                letter.size -= 3

    # Increase the currentIndex by 1 and reset to 0 if the end of the
    # alphabet is reached.
    ### Place Your Code Here ###
    app.currentIndex += 1
    if app.currentIndex >= 26:
        app.currentIndex = 0
