# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

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


def student_completed_exercise(student_info_dict : dict, exercise_data_dict : dict):
    for pic, name in student_info_dict.items():
        if pic in exercise_data_dict:
            
        
            first_name = name [0]
            last_name =name [1]
            total = sum(exercise_data_dict[pic])
            print(first_name,last_name,total)


student_completed_exercise(handle_student_info(),handle_exercise_data())