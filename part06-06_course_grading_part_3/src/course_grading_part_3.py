# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"

# Handle student info

student_info_dict = {}
with open(student_info) as student_info_file:
    for line in student_info_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        
        if parts[0] == "id":
            continue
        id_ = int(parts[0])
        student_info_dict[id_] = parts[1:]
    

# handle exercise data

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


#  Handle exam points
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


#  Calculate grade

grade_dict = {}
name = "name"
# Print the header
print(f"{'name':<30} {'exec_nbr':<10} {'exec_pts.':<10} {'exm_pts.':<10} {'tot_pts.':<10} {'grade':<10}")


for pic, exercise_p in exercise_data_dict.items():
    if pic in exam_points_dict:
        total_exercise_p = sum(exercise_p)
        
        # Calculate exercise points based on the percentage of completed exercises
        percentage_completed = (total_exercise_p / 40) * 100
        exercise_points = min(int(percentage_completed / 10), 10)
        
        sum_exam_points = sum(exam_points_dict[pic])
        total_points = sum_exam_points + exercise_points  # exercise and exam points added together
        
        grade = 0
        for p in range(14, 28, 3):  # Calculate the grade
            if total_points > p:
                grade += 1
        
        grade_dict[pic] = grade


        
        for pic, name in student_info_dict.items():
            if pic in grade_dict:
                    
                
                first_name = name [0]
                last_name =name [1]
                full_name = f"{first_name} {last_name}"
                grade = grade_dict[pic]   
                
         print(f"{full_name:<30} {total_exercise_p:<10} {exercise_points:<10} {sum_exam_points:<10} {total_points:<10} {grade:<10}")
                

