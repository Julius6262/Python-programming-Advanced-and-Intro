def add_student(students: dict, name: str):
    students[name] = []  # Initialize courses as an empty list

def print_student(students: dict, name: str):
    if name in students:
        print(f"{name}:")
        
        courses = students.get(name, [])
        if courses:
            print(f" {len(courses)} completed courses:")  # Get number of courses

            sum_grade = 0
            for course in courses:
                print(f"  {course[0]} {course[1]}")  # Print courses and grade
                sum_grade += course[1]

            avg_grade = sum_grade / len(courses)
            print(f" average grade {avg_grade}")
        else:
            print(" no completed courses")
    else:
        print(f"{name}: no such person in the database")

def add_course(students: dict, name: str, course: tuple):
    if name not in students and course[1] > 0:
        students[name] = [course]
    
    else:
        # Extract course name and grade
        course_name, course_grade = course

        # Check if the course is already in the student's information
        course_found = False
        for i in range(len(students[name])):
            existing_course = students[name][i]
            if existing_course[0] == course_name:
                # Update the grade in place
                students[name][i] = (course_name, max(course_grade, existing_course[1]))
                course_found = True
                break

        if not course_found and course_grade > 0:
            # Course is not present, and the grade is positive, add the course
            students[name].append(course)

def summary(students: dict):
    # most courses completed number and name
    most_courses = " "
    number_courses = 0
    for key, value in students.items():
        print(value)
        if len(value) > number_courses:
            number_courses = len(value)
            most_courses = key

    # best average grade average grade and name
    avg_name = ""
    biggest_so_far = 0
    
    for student, courses in students.items():
        sum_grade = 0

        for course in courses:
            sum_grade += course[1]

        avg_grade = sum_grade / len(courses)

        if avg_grade > biggest_so_far:
            biggest_so_far = avg_grade
            avg_name = student

    print(f"students {len(students)}")
    print(f"most courses completed {number_courses} {most_courses}")
    print(f"best average grade {biggest_so_far} {avg_name}")

