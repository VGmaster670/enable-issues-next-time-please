# Draw the background.
### Place Your Code Here ###
Rect(0, 0, 400, 400, fill=gradient("turquoise", "paleTurquoise"))
# Draw the glass and the orange juice.
### Place Your Code Here ###
Rect(110, 100, 180, 250, fill="azure")
Rect(120, 150, 160, 190, fill=gradient("gold", "yellow", start="bottom"))
# Draw the ice cubes.
### Place Your Code Here ###
Rect(130, 170, 40, 40, fill=rgb(255, 255, 200))
Rect(190, 200, 30, 30, fill=rgb(255, 255, 200))
# Draw the straw.
### (HINT: The straw uses 2 rectangles that only overlap on the edges.)
### Place Your Code Here ###
Rect(240, 50, 50, 10, fill="red")
Rect(
    240, 60, 10, 270, fill=gradient("orange", "orange", "orange", "red", start="bottom")
)
