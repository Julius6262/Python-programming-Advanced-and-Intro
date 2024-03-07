from datetime import datetime, timedelta

def get_user_input():
    first_data =[]
    date_time_data = []
    total_screen_time = []
    total_minutes = 0

    file_name = input("file_name: ")  # text file
    user_date = input("Starting date (dd.mm.yyyy): ")  # dd.mm.yyyy
    amount_of_days = input("How many days: ")  # numbers to count forward
    print("Please type in screen time in minutes on each day (TV computer mobile):")

    try:
        user_date = datetime.strptime(user_date, "%d.%m.%Y")
        show_user_date = user_date.strftime("%d.%m.%Y")
        start_date = show_user_date  # for the end file to have the start and end date to show Time period

        for day in range(int(amount_of_days)):
            screen_time_on_date = input(f"Screen time {show_user_date}: ")
            
            # Split at whitespace and Append to a list, to calculate the sum later
            list_screen_time_on_date = screen_time_on_date.split(" ")
            total_screen_time.append(list_screen_time_on_date)

            # Getting the date and time on the right format and append to list, to collect them all
            form_time = screen_time_on_date.replace (" ", "/")
            form_date_time = f"{show_user_date}: {form_time}"
            date_time_data.append(form_date_time)

            if day < int(amount_of_days):
                # Convert the show_user_date to a datetime object
                show_user_date_dt = datetime.strptime(show_user_date, "%d.%m.%Y")
                
                # Add one day to the show_user_date_dt
                show_user_date_dt += timedelta(days=1)
                
                # Update show_user_date for the next iteration
                show_user_date = show_user_date_dt.strftime("%d.%m.%Y")

        show_user_date_dt -= timedelta(days=1)  # To encounter for the loop going the last time, and end up with the right end date
        show_user_date = show_user_date_dt.strftime("%d.%m.%Y")

        time_period = f"Time period: {start_date}-{show_user_date}"
        first_data.append(time_period)

        for time in total_screen_time:
            for num in time:
                total_minutes += int(num)
        first_data.append(f"Total minutes: {total_minutes}")

        average_minutes = total_minutes/int(amount_of_days)
        first_data.append(f"Average minutes: {average_minutes}")
        
        
        return file_name , first_data, date_time_data

    except ValueError:
        print("Invalid date format. Please use dd.mm.yyyy.")
        return

    


def load_data_to_file(file_name: str, first_data: list, date_time_data: list):
    with open(file_name,"w") as file:
        for values in first_data:
            file.write(f"{values}\n")

        for dt in date_time_data:
            file.write(f" {dt}\n")
    
    return


file_name, first_data, date_time_data = get_user_input()
load_data_to_file(file_name, first_data, date_time_data)