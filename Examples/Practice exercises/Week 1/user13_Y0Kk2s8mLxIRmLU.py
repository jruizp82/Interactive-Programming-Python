# Compute the distance between the points (x0, y0) and (x1, y1).

###################################################
# Distance formula
# Student should enter function on the next lines.
def point_distance(x0, y0, x1, y1):
    """Returns the Euclidian distance between two points (x0,y0) and (x1,y1)."""
    
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
# Hint: You need to use the power operation ** .


###################################################
# Tests
# Student should not change this code.

def test(x0, y0, x1, y1):
    """Tests the point_distance function."""
    
    print "The distance from (" + str(x0) + ", " + str(y0) + ") to",
    print "(" + str(x1) + ", " + str(y1) + ") is",
    print str(point_distance(x0, y0, x1, y1)) + "."

test(2, 2, 5, 6)
test(1, 1, 2, 2)
test(0, 0, 3, 4)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The distance from (2, 2) to (5, 6) is 5.
#The distance from (1, 1) to (2, 2) is 1.4142135623730951.
#The distance from (0, 0) to (3, 4) is 5.
