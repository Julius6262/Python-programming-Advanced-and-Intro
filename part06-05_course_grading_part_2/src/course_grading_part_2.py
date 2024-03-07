# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students2.csv"
    exercise_data = "exercises2.csv"
    exam_points = "exam_points2.csv"

def handle_student_info():
    student_info_dict = {}
    with open(student_info) as student_info_file:
        for line in student_info_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            
            if parts[0] == "id":
                continue
            id_ = int(parts[0])
            student_info_dict[id_] = parts[1:]
    return student_info_dict

def handle_exercise_data():

    exercise_data_dict = {}

    with open(exercise_data) as exercise_data_file:
        for line in exercise_data_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            
            if parts[0] == "id":  # Ignore the header
                continue

            id_ = int(parts[0])

            num_list = []

            for num in parts[1:]:  # Convert all nums to int and put them on a list
                num = int(num)
                num_list.append(num)

            exercise_data_dict[id_] = num_list  # Making the dictionary

    return exercise_data_dict

def handle_exam_points():
    exam_points_dict = {}

    with open(exam_points) as exam_points_file:
        for line in exam_points_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            
            if parts[0] == "id":  # Ignore the header
                continue

            id_ = int(parts[0])

            num_list = []

            for num in parts[1:]:  # Convert all nums to int and put them on a list
                num = int(num)
                num_list.append(num)

            exam_points_dict[id_] = num_list  # Making the dictionary

    return exam_points_dict

def cal_grade(exercise_data_dict: dict, exam_points_dict: dict):
    grade_dict = {}
    
    for pic, exercise_p in exercise_data_dict.items():
        if pic in exam_points_dict:
            total_exercise_p = sum(exercise_p)
            
            # Calculate exercise points based on the percentage of completed exercises
            percentage_completed = (total_exercise_p / 40) * 100
            exercise_points = min(int(percentage_completed / 10), 10)
            
            sum_ = sum(exam_points_dict[pic])
            total_points = sum_ + exercise_points  # exercise and exam points added together
            
            grade = 0
            for p in range(14, 28, 3):  # Calculate the grade
                if total_points > p:
                    grade += 1
            
            grade_dict[pic] = grade

    return grade_dict




def student_completed_exercise(student_info_dict : dict, grade_dict : dict):
    for pic, name in student_info_dict.items():
        if pic in grade_dict:
            
        
            first_name = name [0]
            last_name =name [1]
            grade = grade_dict[pic]
            print(first_name,last_name,grade)


student_completed_exercise(handle_student_info(),cal_grade(handle_exercise_data(),handle_exam_points()))
#handle_exam_points()
cal_grade(handle_exercise_data(),handle_exam_points())