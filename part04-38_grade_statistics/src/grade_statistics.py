def get_input_():
    exam_p_list = []
    exer_list = []
    while True:
        ep_and_ec = input("Exam points and exercises completed:")
        if len(ep_and_ec) < 1:
            break

        temp_list = ep_and_ec.split()
        exam_p_list.append(int(temp_list[0]))
        exer_list.append(int(temp_list[1]))
    return exam_p_list, exer_list


def statistics(exer_list: list):
    exercise_point = []
    for points in exer_list:
        points = int(points)
        if 10 <= points < 20:
            exercise_point.append(1)
        elif 20 <= points < 30:
            exercise_point.append(2)
        elif 30 <= points < 40:
            exercise_point.append(3)
        elif 40 <= points < 50:
            exercise_point.append(4)
        elif 50 <= points < 60:
            exercise_point.append(5)
        elif 60 <= points < 70:
            exercise_point.append(6)
        elif 70 <= points < 80:
            exercise_point.append(7)
        elif 80 <= points < 90:
            exercise_point.append(8)
        elif 90 <= points < 100:
            exercise_point.append(9)
        elif points == 100:
            exercise_point.append(10)
        else:
            exercise_point.append(0)
    return exercise_point  # Complete list of exercise points


def get_result_points(exercise_point: list, exam_p_list: list):
    fail = []
    collective = []
    for i in range(len(exam_p_list)):
        if exam_p_list[i] < 10:
            fail.append(exam_p_list[i] + exercise_point[i])
        else:
            collective.append(exam_p_list[i] + exercise_point[i])
    return collective, fail  # List with pass the exam, and failed exam


def get_grade(exercise_point: list, exam_p_list: list):
    grade_list = []
    for i in range(len(exam_p_list)):
        if exam_p_list[i] < 10 or exam_p_list[i] + exercise_point[i] < 15:
            grade_list.append(0)

        elif 15 <= exam_p_list[i] + exercise_point[i] < 18:
            grade_list.append(1)

        elif 18 <= exam_p_list[i] + exercise_point[i] < 21:
            grade_list.append(2)

        elif 21 <= exam_p_list[i] + exercise_point[i] < 24:
            grade_list.append(3)

        elif 24 <= exam_p_list[i] + exercise_point[i] < 28:
            grade_list.append(4)

        elif 28 <= exam_p_list[i] + exercise_point[i] <= 30:
            grade_list.append(5)
    return grade_list


def cal_statistic(collective: list, fail: list, grade_list: list):
    point_average = (sum(collective) + sum(fail)) / (len(collective) + len(fail))

    passed_students = [grade for grade in grade_list if grade > 0]
    pass_percentage = (len(passed_students) / len(grade_list)) * 100

    return point_average, pass_percentage


def main():
    exam_points, exercise_points = get_input_()
    exercise_point = statistics(exercise_points)
    collective, fail_list = get_result_points(exercise_point, exam_points)
    grade_list = get_grade(exercise_point, exam_points)
    point_avg, pass_percentage = cal_statistic(collective, fail_list, grade_list)

    print("Statistics:")
    print(f"Points average: {point_avg:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")

    print("Grade distribution:")
    for grade in range(5, -1, -1):
        stars = '*' * grade_list.count(grade)
        print(f"  {grade}:", stars)

main()
