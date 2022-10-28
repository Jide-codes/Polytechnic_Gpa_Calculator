score = []
course_unit = []
quality_point = []
total_course_unit = []


# THIS FIND STANDARD GP WILL TAKE IN THE USERCORE AND ASSIGN A STANDARD GP TO IT 

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



# THE WHILE LOOP HERE GET THE COURSE SCORE AND THE UNIT OF THE COURSE FROM THE USER AND APPEND IT TO DIFFERENT LIST
# COURSE SCORE AND COURSE UNIT
# BUT THERE IS A LOGIC THERE, THE LOGIC THERE IS THAT SYSTEM IS NOT ONLY GETTING THE COURSE SCORE
# IT GETS THE SCORE, ASSIGN A STANDARD GP AND THEN APPEND IT TO A LIST

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



# THIS GET QUALITY POINT FUNCTION WILL TAKE IN THE APPENDED STANDARD GP AND ALSO THE APPENDED COURSE UNIT
# THEN MULTIPLY EVERY SINGLE ITEM IN THE APPENDED COURSE UNIT WITH EVERY SINGLE ITEM IN THE APPENDED GP
# AND THAT WILL RETURN TO US OUR QUALITY POINT

def get_quality_point(appended_score_point, appended_course_unit):

    quality = [x*y for x,y in  zip(appended_score_point, appended_course_unit)]
    quality_point = sum(quality)
    return quality_point
quality_point = get_quality_point(score, course_unit)


# GET_TOTAL_COURSE_UNIT FUNCTION GET THE APPENDED COURSE UNIT LIST THEN SUM IT UP AND RETURN THE TOTAL COURSE UNIT

def get_total_course_unit(total_course_units):
    total_course_unit = sum(total_course_units)
    return total_course_unit
total_course_unit = get_total_course_unit(course_unit)


# THE FINAL STEP IS THE GPA_CALCULATOR IT SELF, THIS FUNCTION GET THE QUALITY POINT AND THE TOTAL COURSE UNIT
# THE DIVIDE QUALITY POINT BY TOTAL COURSE UNI TO PROVIDE THE GPA

def gpa_calculator(quality_point, total_course_unit):
    gpa = quality_point / total_course_unit
    my_gpa = round(gpa, 2)
    return my_gpa
my_gpa = gpa_calculator(quality_point, total_course_unit)

print(f"your gpa: {my_gpa}")


    

