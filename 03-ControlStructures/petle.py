###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#
university = 'Krakow University of Economics'
space = ' '
university_expanded = ""


for char in university:
    university_expanded += char + space

print(university) # original university name
print(university_expanded) # expanded university name
