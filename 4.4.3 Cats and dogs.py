app.background = gradient("white", "lightCyan", start="top")

app.phrase = "catsanddogs"
app.index = 0

Oval(50, 5, 180, 100, fill="silver", border="grey")
Oval(160, 10, 160, 115, fill="silver", border="grey")
Oval(270, 5, 130, 130, fill="silver", border="grey")
Oval(360, 0, 140, 120, fill="silver", border="grey")
Rect(70, 0, 300, 40, fill="silver")


def onMousePress(mouseX, mouseY):
    # Get the next letter in app.phrase, and use it as a new Label's value.
    # Then adjust app.index appropriately.
    ### Place Your Code Here ###
    currentLetter = app.phrase[app.index % 11]
    Label(currentLetter, mouseX, mouseY, fill="steelBlue", italic=True)
    app.index += 1
