#
# Count vowels
#

def count_vowels(str):
    counter = str.count('a')
    counter += str.count('e')
    counter += str.count('i')
    counter += str.count('o')
    counter += str.count('u')
    
    return counter

print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))