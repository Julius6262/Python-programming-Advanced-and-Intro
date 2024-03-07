import csv
from datetime import datetime, timedelta

def final_points():
    start_times = {}
    submissions = {}

    # Read start times
    with open("start_times.csv") as start_file:
        for row in csv.reader(start_file, delimiter=";"):
            name, start_time_str = row[0], row[1]
            start_times[name] = datetime.strptime(start_time_str, "%H:%M")

    # Read submissions
    with open("submissions.csv") as submissions_file:
        for row in csv.reader(submissions_file, delimiter=";"):
            name, task, points_str, time_str = row[0], row[1], row[2], row[3]
            submission_time = datetime.strptime(time_str, "%H:%M")

            # Check if submission is within 3 hours of start time
            if submission_time - start_times[name] > timedelta(hours=3):
                continue

            # Update submissions dictionary with the highest points for each task
            if name not in submissions:
                submissions[name] = {}

            if task not in submissions[name] or int(points_str) > submissions[name][task]:
                submissions[name][task] = int(points_str)

    # Calculate total points for each student
    total_points = {}
    for name, tasks in submissions.items():
        total_points[name] = sum(tasks.values())

    return total_points
