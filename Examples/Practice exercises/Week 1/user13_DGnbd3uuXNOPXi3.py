# Compute the area of a circle, given the length of its radius.

###################################################
# Circle area formula
# Student should enter function on the next lines.
import math
def circle_area(radius):
    """Returns the area of a circle of the given radius."""
    
    return math.pi * radius ** 2


###################################################
# Tests
# Student should not change this code.

def test(radius):
    """Tests the circle_area function."""
    
    print "A circle with a radius of " + str(radius),
    print "inches has an area of",
    print str(circle_area(radius)) + " square inches."

test(8)
test(3)
test(12.9)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has an area of 201.06192982974676 square inches.
#A circle with a radius of 3 inches has an area of 28.274333882308138 square inches.
#A circle with a radius of 12.9 inches has an area of 522.7924334838775 square inches.
