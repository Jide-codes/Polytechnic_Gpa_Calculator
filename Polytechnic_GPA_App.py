# INSTEAD OF WRITTING A VERY LONG CODE, I SAVE THE OTHER PY FILE IN A FOLDER AND NAMED IT My_gpa 
# I IMPORTED IT TO THIS NEW FILE AND CALL THE FUNCTION WHICH MAKES:
# MY CODE CLEAN
# UNDERSTANDABLE 
# EASY TO IMPLEMENT 
# AND EASY TO READ  

import My_gpa.GPA_J_codes as gp

score = []
course_unit = []
quality_point = []
total_course_unit = []


init_count = 1
total_number_of_course = int(input('Enter total number of course: '))
while init_count <= total_number_of_course:
    user_course_score = int(input('Enter exam score: '))
    user_course_unit = int(input('Enter course unit: '))
    score.append(gp.find_standard_gp(user_course_score))
    course_unit.append(user_course_unit)
    choice = input("enter 'q' to quit: ")
    if choice == 'q':
        break
    init_count+=1

gp.find_standard_gp()

quality_point = gp.get_quality_point(score, course_unit)

total_course_unit = gp.get_total_course_unit(course_unit)

my_gpa = gp.gpa_calculator(quality_point, total_course_unit)
print(f"your GPA: {my_gpa}")