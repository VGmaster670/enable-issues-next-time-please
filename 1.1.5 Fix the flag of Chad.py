# This code 'looks right', but it contains an error: the blue rectangle is too
# large! The autograder will not accept it until the blue rectangle is not
# overlapped by the yellow and red rectangles.
### Fix Your Code Here ###
Rect(50, 100, 100, 200, fill="blue")

# This correctly draws the yellow and red rectangles.
### (HINT: To see the problem using the canvas, try commenting the two lines of
#          code below using a '#' mark and running the code so that only the blue
#          rectangle is drawn. Be sure to uncomment the lines when you want to
#          draw the whole flag again!)
Rect(150, 100, 100, 200, fill="yellow")
Rect(250, 100, 100, 200, fill="red")
