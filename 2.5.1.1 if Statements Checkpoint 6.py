Label("Purple Click Counter", 200, 20, size=20, bold=True)
Label("Click in the purple part of", 200, 45)
Label("the canvas to increase the counter!", 200, 65)

Polygon(0, 0, 0, 400, 400, 400, fill="purple")
counter = Label(0, 125, 275, fill="plum", size=100, bold=True)


def onMousePress(mouseX, mouseY):
    # The counter value should increase if the click is on the purple side of
    # the canvas.
    ### (HINT: Every point in the purple area has mouseY at least as big as
    #          mouseX!)
    ### Place Your Code Here ###
    if mouseY >= mouseX:
        counter.value += 1
