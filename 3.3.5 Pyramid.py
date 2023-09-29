app.background = gradient(rgb(25, 25, 180), rgb(25, 25, 80), start="right-top")

Star(350, 50, 53, 500, fill="maroon")
Star(350, 50, 28, 500, roundness=90)
Rect(0, 365, 400, 135, fill="seaGreen")

pyramid = Group()


def drawPyramid(blockHeight):
    # Draw the layers leading up to the top of the pyramid.
    ### (HINT: Using an align of 'bottom' will make it easier!)
    ### Place your code here ###
    pyramid.add(
        Rect(
            25,
            380,
            350,
            blockHeight,
            align="bottom-left",
            border="black",
            borderWidth=1,
            fill=gradient("saddleBrown", "darkGoldenrod", start="top"),
        )
    )
    pyramid.add(
        Rect(
            40,
            380 - blockHeight,
            320,
            blockHeight,
            align="bottom-left",
            border="black",
            borderWidth=1,
            fill=gradient("saddleBrown", "darkGoldenrod", start="top"),
        )
    )
    pyramid.add(
        Rect(
            55,
            380 - blockHeight * 2,
            290,
            blockHeight,
            align="bottom-lef8",
            border="black",
            borderWidth=1,
            fill=gradient("saddleBrown", "darkGoldenrod", start="top"),
        )
    )
    pyramid.add(
        Rect(
            70,
            380 - blockHeight * 3,
            260,
            blockHeight,
            align="bottom-left",
            border="black",
            borderWidth=1,
            fill=gradient("saddleBrown", "darkGoldenrod", start="top"),
        )
    )
    pyramid.add(
        Rect(
            85,
            380 - blockHeight * 4,
            230,
            blockHeight,
            align="bottom-left",
            border="black",
            borderWidth=1,
            fill=gradient("saddleBrown", "darkGoldenrod", start="top"),
        )
    )
    pyramid.add(
        Rect(
            100,
            380 - blockHeight * 5,
            200,
            blockHeight,
            align="bottom-left",
            border="black",
            borderWidth=1,
            fill=gradient("saddleBrown", "darkGoldenrod", start="top"),
        )
    )
    pyramid.add(
        Rect(
            115,
            380 - blockHeight * 6,
            170,
            blockHeight,
            align="bottom-left",
            border="black",
            borderWidth=1,
            fill=gradient("saddleBrown", "darkGoldenrod", start="top"),
        )
    )
    pyramid.add(
        Rect(
            130,
            380 - blockHeight * 7,
            140,
            blockHeight,
            align="bottom-left",
            border="black",
            borderWidth=1,
            fill=gradient("saddleBrown", "darkGoldenrod", start="top"),
        )
    )

    ### Intended Solution ###
    # for val in range(8):
    #     pyramid.add(
    #         Rect(200,380-blockHeight*val,350-30*val,blockHeight,fill=gradient("saddleBrown","darkGoldenrod", start="top"),border="black",borderWidth=1,align="bottom"))

    # This variable defines the top of where the stairs should end.
    stairsTop = pyramid.top + 2 * blockHeight

    # Polygon for the staircase
    Polygon(
        85,
        380,
        160,
        stairsTop,
        240,
        stairsTop,
        315,
        380,
        fill=gradient("sienna", "goldenrod", start="top"),
        border="black",
    )

    # Chamber at the top of the pyramid
    Rect(200, stairsTop, 40, 15, align="bottom")
    Rect(
        200,
        pyramid.top + blockHeight,
        180,
        5,
        fill="darkGoldenrod",
        border="black",
        align="bottom",
    )
    Rect(
        200,
        pyramid.top + blockHeight,
        180,
        5,
        fill="darkGoldenrod",
        border="black",
        align="top",
    )

    # mist
    mist = Group(
        Star(150, 345, 50, 600, opacity=40, fill="white"),
        Star(175, 351, 48, 600, opacity=30, fill="white"),
        Star(200, 350, 52, 600, opacity=30, fill="white"),
        Star(225, 347, 47, 600, opacity=30, fill="white"),
        Star(250, 353, 51, 600, opacity=40, fill="white"),
    )
    mist.width = 600
