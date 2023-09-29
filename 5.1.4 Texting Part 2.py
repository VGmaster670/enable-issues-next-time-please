import random

app.stepsPerSecond = 1

# word choices
app.responses = ["What?!", "Me too!", "No way...", "Same! :)", "Interesting."]

border = Rect(0, 0, 400, 400, fill=None, border="grey", borderWidth=30)

# text box
Rect(30, 330, 340, 40, fill="gainsboro")
Circle(55, 350, 15, fill="white")
Circle(290, 350, 15, fill="white")
Line(55, 350, 290, 350, fill="white", lineWidth=30)
Label("Message", 80, 350, fill="gainsboro")
Label("Send", 335, 350)

texts = Group()


def drawMessage(message, isFromMyself):
    textBubble = Group(
        Circle(15, 305, 15), Circle(100, 305, 15), Line(15, 305, 100, 305, lineWidth=30)
    )

    #### START OF BLOCK DRAW_MESSAGE ####

    # This function now takes a message and a boolean isFromMyself. Depending on
    # if this text is from me or not, recolor and reposition the bubble. Then add
    # a polygon for the bubble's tail and the text bubble message.
    ### Place Your Code Here ###
    if isFromMyself == True:
        textBubble.centerX = 292
        tail = Polygon(
            335,
            textBubble.centerY,
            360,
            textBubble.bottom,
            335,
            textBubble.bottom,
            fill="dodgerBlue",
        )
        textBubble.fill = "dodgerBlue"
        label = Label(message, textBubble.centerX, textBubble.centerY, fill="white")
        textBubble.add(label)
        textBubble.add(tail)
    else:
        textBubble.centerX = 108
        tail = Polygon(
            65,
            textBubble.centerY,
            40,
            textBubble.bottom,
            65,
            textBubble.bottom,
            fill="gainsboro",
        )
        textBubble.fill = "gainsboro"
        label = Label(message, textBubble.centerX, textBubble.centerY, fill="black")
        textBubble.add(label)
        textBubble.add(tail)
    #### END OF BLOCK ####

    texts.add(textBubble)


def moveTexts():
    # Move each text message up to make space for the new one.
    # Remove the text message if it leaves the texting space.
    for text in texts.children:
        text.centerY -= 40
        if text.centerY < 30:
            texts.remove(text)


def onStep():
    moveTexts()

    message = random.choice(app.responses)
    isFromMyself = random.choice([True, False])
    drawMessage(message, isFromMyself)
