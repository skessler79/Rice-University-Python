"""
Template - Function that checks whether a string can be converted to an integer
"""


def make_int(int_string):
    """
    Given the string int_string, return the associated integer if all 
    digits are decimal digits.  Other return -1.
    """
    
    if(int_string.isdigit()):
        return int(int_string)
    return -1
    
# Tests

print(make_int("123"))
print(make_int("00123"))
print(make_int("1.23"))
print(make_int("-123"))


# Output

#123
#123
#-1
#-1