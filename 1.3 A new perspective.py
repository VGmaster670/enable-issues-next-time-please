# background
Rect(0, 0, 400, 400, fill=gradient("white", "navy"))

# Draw the perspective lines next.
### Place Your Code Here ###
Line(0, 400, 100, 250, lineWidth=2)
Line(100, 0, 100, 250, lineWidth=2)
Line(100, 250, 300, 250, lineWidth=2)
Line(300, 0, 300, 250, lineWidth=2)
Line(300, 250, 400, 400, lineWidth=2)
# Draw the ninja here.
### Place Your Code Here ###
Oval(200, 315, 100, 30)
Circle(200, 200, 70, fill=gradient("lightBlue", "royalBlue"))
Oval(200, 195, 140, 50)
Oval(175, 195, 30, 40, fill="white")
Oval(225, 195, 30, 40, fill="white")
Circle(178, 195, 10)
Circle(222, 195, 10)
Line(160, 165, 190, 170, lineWidth=3)
Line(210, 170, 240, 165, lineWidth=3)
Polygon(270, 195, 290, 190, 280, 180)
