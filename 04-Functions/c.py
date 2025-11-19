###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
# def triangle_area(a,b,c):
#     ..
#     return ...

# print('The area of ​​a triangle with sides ... is ...')
# print('The area of ​​a triangle with sides ... is ...')
# print('The area of ​​a triangle with sides ... is ...')


import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    result = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return result

side_a = 2
side_b= 3
side_c=4

area = triangle_area(a=side_a,b=side_b, c= side_c)
print(f'For triangle with sides {side_a}, {side_b}, {side_c} the area is {area}')

#triangle_area(2,3,4)
#print(f'The area of a triangle with sides {a}, {b}, {c} is {triangle_area[area])}')
