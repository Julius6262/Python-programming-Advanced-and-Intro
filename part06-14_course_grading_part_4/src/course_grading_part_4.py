# tee ratkaisu tänne
if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
    course_info = input("Course information: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"
    course_info = "course1.txt"

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
        student_info_dict[id_] = " ".join(student_info_dict[id_])


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


# Print the header
course_info_list = []
with open(course_info) as course_file:
    for line in course_file:
        line = line.strip("name")
        line = line.strip(":")
        line = line.strip()
        line = line.split(" ")
        course_info_list.append(line)

    course_info_list[0][-1] = course_info_list[0][-1]+","
    course_info_list[1][0] = course_info_list[1][2]
    course_info_list[1][1] = course_info_list[1][1].strip(":")
    course_info_list[1] = course_info_list[1][:-1]
    
with open("results.txt", "w") as text_file:
    count_characters = 0
    count_white_space = -1

    for dic in course_info_list:
        for word in dic:
            text_file.write(f"{word} ")
            count_characters += len(word)  # Update count_characters with the length of the word
            count_white_space += 1  # Count the space after each word

    text_file.write("\n")
    length_of_print = count_characters + count_white_space
    text_file.write(length_of_print * "=")
    text_file.write("\n")

    
    

    name = "name"
    # Print the colum name
    text_file.write(f"{'name':<30} {'exec_nbr':<10} {'exec_pts.':<10} {'exm_pts.':<10} {'tot_pts.':<10} {'grade':<10}")
    text_file.write("\n")

    grade_dict = {}
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
                        
                    full_name = name
                    grade = grade_dict[pic]   
                    
            text_file.write(f"{full_name:<30} {total_exercise_p:<10} {exercise_points:<10} {sum_exam_points:<10} {total_points:<10} {grade:<10}")
            text_file.write("\n")
    
with open("results.csv","w") as result_file:
    for pic, name in student_info_dict.items():
            if pic in grade_dict:
                result_file.write(f"{pic};{name};{grade_dict[pic]}\n")

print("Results written to files results.txt and results.csv")