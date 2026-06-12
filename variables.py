#  the Student Report Card:
# - Student Name        → str
# - Age                 → int
# - College             → str
# - CGPA                → float
# - Is Passed           → bool
# - Result              → None first, then "Pass"

# Print each variable WITH its type.




# Student Report Card
# Author: Anirudh Negi

# Creating variables
student_name = "Anirudh Negi"
age = 19
college = "CGC University"
cgpa = 8.5
is_passed = True
result = None

# Printing with types
print("===== Student Report Card =====")

print("Name:", student_name, "     | Type:", type(student_name))
print("Age:", age, "              | Type:", type(age))
print("College:", college, "| Type:", type(college))
print("CGPA:", cgpa, "            | Type:", type(cgpa))
print("Is Passed:", is_passed, "      | Type:", type(is_passed))
print("Result:", result, "          | Type:", type(result))

# Now change result from None to "Pass"
result = "Pass"
print("Result:", result, "           | Type:", type(result))

print("================================")