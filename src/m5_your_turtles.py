"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Sreekar Manyam.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
print("Turtle Race")
slow_turtle = rg.SimpleTurtle('turtle')
slow_turtle.pen = rg.Pen('black', 5)
slow_turtle.speed = 5
slow_turtle.pen_up()
slow_turtle.backward(100)
slow_turtle.pen_down()

fast_turtle = rg.SimpleTurtle('turtle')
fast_turtle.pen = rg.Pen('red', 5)
fast_turtle.speed = 10
fast_turtle.pen_up()
fast_turtle.backward(100)
fast_turtle.left(90)
fast_turtle.forward(50)
fast_turtle.right(90)
fast_turtle.pen_down()

crazy_turtle = rg.SimpleTurtle('turtle')
crazy_turtle.pen = rg.Pen('purple', 5)
crazy_turtle.speed = 7.5
crazy_turtle.pen_up()
crazy_turtle.backward(100)
crazy_turtle.right(90)
crazy_turtle.forward(100)
crazy_turtle.left(135)
crazy_turtle.pen_down()

for k in range(12):
    slow_turtle.forward(5)
    fast_turtle.forward(30)
    crazy_turtle.right(90)
    crazy_turtle.forward(20)
    crazy_turtle.left(90)
    crazy_turtle.forward(20)

window.close_on_mouse_click()
