"""
Template - Function that swaps and capitalizes first and last names
"""


def name_swap(name_string):
    """
    Given the string name string of the form "first last", return 
    the string "Last First" where both names are now capitalized
    """
    
    # Enter code here
    index = name_string.find(" ")
    first = name_string[:index]
    last = name_string[index + 1:]
    first = first[0].upper() + first[1:]
    last = last[0].upper() + last[1:]
    
    return last + " "  + first
    
# Tests

print(name_swap("joe warren"))
print(name_swap("scott rixner"))
print(name_swap("john greiner"))


# Output

#Warren Joe
#Rixner Scott
#Greiner John