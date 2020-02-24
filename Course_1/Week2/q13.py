"""
Template - Compute and print powerball numbers.
"""

import random

###################################################
# Powerball function
# Student should enter function on the next lines.
def powerball():
    print("Today's numbers are "
          + str(random.randint(1,59)) + ", "
          + str(random.randint(1,59)) + ", "
          + str(random.randint(1,59)) + ", "
          + str(random.randint(1,59)) + ", and "
          + str(random.randint(1,59)) + ".")
    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()

###################################################################
# Some sample output appears below.  Note that numbers need not match
#Today's numbers are 46, 25, 49, 54, and  8. The Powerball number is 26.
#Today's numbers are 14, 11, 17, 6, and  30. The Powerball number is 16.
#Today's numbers are 58, 59, 39, 2, and  29. The Powerball number is 19.