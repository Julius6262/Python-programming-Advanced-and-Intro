class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        # Initialize the stopwatch with 0 minutes and 0 seconds
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def tick(self):
        # Increment the time by one second
        self.seconds += 1

        # If 60 seconds have passed, reset seconds to 0 and increment minutes
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

            # If 60 minutes have passed, reset minutes to 0
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1

                if self.hours == 24:
                    self.hours = 0

    def set(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        # Return a formatted string representation of the current time
        formatted_hours = f"0{self.hours}" if self.hours < 10 else f"{self.hours}"
        formatted_minutes = f"0{self.minutes}" if self.minutes < 10 else f"{self.minutes}"
        formatted_seconds = f"0{self.seconds}" if self.seconds < 10 else f"{self.seconds}"
        return f"{formatted_hours}:{formatted_minutes}:{formatted_seconds}"

