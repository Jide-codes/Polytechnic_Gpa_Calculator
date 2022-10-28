score = []
course_unit = []
quality_point = []
total_course_unit = []



def find_standard_gp(user_score):

    standard_grade_point = {'A':4.00, 'AB':3.50, 'B':3.25, 'BC':3.00, 'C':2.75,
                             'CD':2.50, 'D':2.25, 'E':2.00, 'F':0.00, }

    if user_score > 75:
        return standard_grade_point['A']
        
        
    elif user_score <= 75 and user_score >= 70:
        return standard_grade_point['AB']
       

    elif user_score <= 69 and user_score >= 65:
        return standard_grade_point['B']
        

    elif user_score <= 64 and user_score >= 60:
       return standard_grade_point['BC']
        

    elif user_score <= 59 and user_score >= 55:
        return standard_grade_point['C']
        

    elif user_score <= 54  and user_score >= 50:
        return standard_grade_point['CD']
        

    elif user_score <= 49 and user_score >= 45:
        return standard_grade_point['D']
        

    elif user_score <= 44 and user_score >= 40:
         return standard_grade_point['E']
        

    else:
        return standard_grade_point['F']



init_count = 1
total_number_of_course = int(input('Enter total number of course: '))
while init_count <= total_number_of_course:
    user_course_score = int(input('\nEnter exam score: '))
    user_course_unit = int(input('Enter course unit: '))
    score.append(find_standard_gp(user_course_score))
    course_unit.append(user_course_unit)
    choice = input("enter 'q' to quit: ")
    if choice == 'q':
        break
    init_count+=1


    



def get_quality_point(appended_score_point, appended_course_unit):

    quality = [x*y for x,y in  zip(appended_score_point, appended_course_unit)]
    quality_point = sum(quality)
    return quality_point
quality_point = get_quality_point(score, course_unit)



def get_total_course_unit(total_course_units):
    total_course_unit = sum(total_course_units)
    return total_course_unit
total_course_unit = get_total_course_unit(course_unit)


def gpa_calculator(quality_point, total_course_point):
    gpa = quality_point / total_course_point
    my_gpa = round(gpa, 2)
    return my_gpa
my_gpa = gpa_calculator(quality_point, total_course_unit)

print(f"your gpa: {my_gpa}")


    

