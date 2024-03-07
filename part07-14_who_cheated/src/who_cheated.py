def cheaters() -> list:
    import csv
    from datetime import datetime, timedelta

    start_dic = {}
    submissions_dic = {}
    cheater_list = []

    # Read start times
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            start_dic[line[0]] = line[1]

    # Read submissions
    with open("submissions.csv") as submissions_file:
        for line in csv.reader(submissions_file, delimiter=";"):
            name, task, points, time_str = line[0], line[1], line[2], line[3]
            submission_time = datetime.strptime(time_str, "%H:%M")

            if name not in submissions_dic:
                submissions_dic[name] = {'task': task, 'points': points, 'time': submission_time}
            else:
                if submissions_dic[name]['time'] < submission_time:
                    submissions_dic[name] = {'task': task, 'points': points, 'time': submission_time}

    # Check for cheaters
    for name in start_dic:
        if name in submissions_dic:
            start_time_str = start_dic[name]
            start_time = datetime.strptime(start_time_str, "%H:%M")

            end_time_str = submissions_dic[name]['time'].strftime("%H:%M")
            end_time = datetime.strptime(end_time_str, "%H:%M")

            time_difference = end_time - start_time
            threshold_difference = timedelta(hours=3)

            if time_difference > threshold_difference:
                cheater_list.append(name)

    return cheater_list
