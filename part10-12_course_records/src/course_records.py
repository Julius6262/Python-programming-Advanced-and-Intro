class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"


class StudyRecords:
    def __init__(self):
        self.courses = {}

    def add_completion(self, course_name, grade, credits):
        if course_name in self.courses and self.courses[course_name].grade() > grade:
            return

        self.courses[course_name] = Course(course_name, grade, credits)

    def get_completion(self, course_name):
        if course_name not in self.courses:
            return None

        return self.courses[course_name]

    def get_statistics(self):
        number_of_courses = len(self.courses)
        total_credits = sum(course.credits() for course in self.courses.values())
        total_grades = sum(course.grade() for course in self.courses.values())
        grades = [0, 0, 0, 0, 0, 0, 0]

        for course in self.courses.values():
            grades[course.grade()] += 1

        average_grade = total_grades / number_of_courses if number_of_courses > 0 else 0

        return {
            "number_of_courses": number_of_courses,
            "total_credits": total_credits,
            "average_grade": average_grade,
            "grades": grades
        }


class Application:
    def __init__(self):
        self.register = StudyRecords()

    def menu(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def new_completion(self):
        course_name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.register.add_completion(course_name, grade, credits)

    def get_completion(self):
        course_name = input("course: ")
        course = self.register.get_completion(course_name)
        if course is None:
            print("no entry for this course")
        else:
            print(course)

    def statistics(self):
        stats = self.register.get_statistics()

        print(f"{stats['number_of_courses']} completed courses, a total of {stats['total_credits']} credits")
        print(f"mean {stats['average_grade']:.1f}")
        print("grade distribution")
        for i in range(5, 0, -1):
            grade_hits = stats['grades'][i]
            row = "x" * grade_hits
            print(f"{i}: {row}")

    def execute(self):
        self.menu()

        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.new_completion()
            elif command == "2":
                self.get_completion()
            elif command == "3":
                self.statistics()


Application().execute()
