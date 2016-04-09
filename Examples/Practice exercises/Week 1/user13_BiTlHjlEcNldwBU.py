# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.
import random
def powerball():
    """Prints Powerball lottery numbers."""
    
    print "Today's numbers are " + str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ", and",
    print str(random.randrange(1, 60)) + ".  The Powerball number is",
    print str(random.randrange(1, 36)) + "."

    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()
