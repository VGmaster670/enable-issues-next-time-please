app.background = "lightYellow"

# modern mickey
# body and pants
Oval(200, 400, 200, 220)
Oval(110, 390, 25, 55, fill="red", border="black"),
Oval(290, 390, 25, 55, fill="red", border="black"),
Rect(104, 368, 192, 50, fill="red")
Oval(200, 368, 194, 22)
Oval(175, 400, 20, 40, fill="gold")
Oval(225, 400, 20, 40, fill="gold")

# face
Circle(200, 200, 100)
Circle(105, 105, 50)
Circle(295, 105, 50)
Oval(200, 250, 160, 100, fill="peachPuff", border="black")
Oval(180, 180, 70, 150, fill="peachPuff")
Oval(220, 180, 70, 150, fill="peachPuff")
Oval(185, 185, 25, 55, fill="white", border="black", borderWidth=1.5)
Oval(185, 200, 12, 25)
Oval(215, 185, 25, 55, fill="white", border="black", borderWidth=1.5)
Oval(215, 200, 12, 25)

# mouth
Oval(200, 220, 60, 20, fill=None, border="black", borderWidth=1.5, dashes=(33, 68))
Oval(200, 260, 80, 40)
Oval(200, 249, 70, 20, fill="peachPuff"),
Oval(200, 276, 40, 10, fill="fireBrick")

retroPants = Group(
    Oval(110, 390, 25, 55, fill="white", border="black"),
    Oval(290, 390, 25, 55, fill="white", border="black"),
    Rect(104, 368, 192, 50, fill="white"),
    Oval(200, 368, 194, 22),
)

retroButtons = Group(Oval(175, 400, 20, 40), Oval(225, 400, 20, 40))

retroFace = Group(
    Circle(200, 200, 100),
    Circle(105, 105, 50),
    Circle(295, 105, 50),
    Oval(200, 250, 160, 100, fill="white", border="black"),
    Oval(180, 180, 70, 150, fill="white"),
    Oval(220, 180, 70, 150, fill="white"),
)

retroEyes = Group(
    Oval(185, 185, 25, 55),
    Polygon(184, 185, 172, 172, 172, 198, fill="white"),
    Oval(215, 185, 25, 55),
    Polygon(214, 185, 202, 172, 202, 198, fill="white"),
    Oval(200, 220, 60, 20, fill=None, border="black", borderWidth=1.5, dashes=(33, 68)),
)

retroMouth = Group(
    Oval(200, 225, 35, 20),
    Oval(200, 260, 80, 40),
    Oval(200, 249, 70, 20, fill="white"),
    Oval(200, 277, 40, 10, fill="white"),
)

retroMickey = Group(retroPants, retroFace, retroButtons, retroEyes, retroMouth)

# nose
Oval(200, 225, 35, 20)


def onMousePress(mouseX, mouseY):
    # If any part of retro mickey is clicked on, that part should be cleared,
    # revealing the more modern version behind it!
    ### Place Your Code Here ###
    if retroPants.hits(mouseX, mouseY) == True:
        retroMickey.remove(retroPants)
    if retroFace.hits(mouseX, mouseY) == True:
        retroMickey.remove(retroFace)
    if retroButtons.hits(mouseX, mouseY) == True:
        retroMickey.remove(retroButtons)
    if retroEyes.hits(mouseX, mouseY) == True:
        retroMickey.remove(retroEyes)
    if retroMouth.hits(mouseX, mouseY) == True:
        retroMickey.remove(retroMouth)
