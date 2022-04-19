# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Enter the lengths of three sides of a triangle: ")
side_a = int(input("a: "))
side_b = int(input("b: "))
side_c = int(input("c: "))

if side_a == side_b and side_a == side_c:
    triangle_type = "equalateral"
elif side_a == side_b or side_a == side_c or side_b == side_c:
    triangle_type = "isosceles"
else:
    triangle_type = "scalene"

if triangle_type == "equalateral" or triangle_type == "isoscleles":
    print(f"A triangle with sides of {side_a}, {side_b}, and {side_c} is an {triangle_type} triangle")
else:
    print(f"A triangle with sides of {side_a}, {side_b}, and {side_c} is a {triangle_type} triangle")
