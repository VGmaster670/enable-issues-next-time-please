def threeStripeFlag(country, color1, color2, color3):
    # Fix the label so it uses the function parameter: country.
    ### Fix Your Code Here ###
    Label(country, 200, 60, size=40, bold=True)

    # Draw the rectangles and use the correct function parameters for each one!
    ### Place Your Code Here ###
    Rect(50, 100, 100, 200, fill=color1)
    Rect(150, 100, 100, 200, fill=color2)
    Rect(250, 100, 100, 200, fill=color3)
