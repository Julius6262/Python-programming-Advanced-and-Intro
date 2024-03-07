from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(course_attempts: list):
    return reduce(lambda sum_credits, item: sum_credits + item.credits, course_attempts, 0 )

def sum_of_passed_credits(course_attempts: list):
    passed = filter(lambda attempt: attempt.grade >= 1, course_attempts)
    return reduce(lambda sum_credits, item: sum_credits + item.credits, passed, 0)

def average(course_attempts: list):
    passed = list(filter(lambda attempt: attempt.grade >= 1, course_attempts))
    return reduce(lambda sum_grades, item: sum_grades + (item.grade/len(passed)), passed, 0)

s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
ag = average([s1, s2, s3])
print(ag)