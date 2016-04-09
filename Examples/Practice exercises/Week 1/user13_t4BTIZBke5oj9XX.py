# Compute the circumference of a circle, given the length of its radius.

###################################################
# Circle circumference formula
# Student should enter function on the next lines.
import math
def circle_circumference(radius):
    """Returns the circumference of a circle of the given radius."""
    
    return 2 * math.pi * radius


###################################################
# Tests
# Student should not change this code.

def test(radius):
    """Tests the circle_circumference function."""
    
    print "A circle with a radius of " + str(radius),
    print "inches has a circumference of",
    print str(circle_circumference(radius)) + " inches."

test(8)
test(3)
test(12.9)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has a circumference of 50.26548245743669 inches.
#A circle with a radius of 3 inches has a circumference of 18.84955592153876 inches.
#A circle with a radius of 12.9 inches has a circumference of 81.05309046261667 inches.
