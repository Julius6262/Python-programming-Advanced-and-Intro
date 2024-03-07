class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0

    def __str__(self):
        formatted_minutes = f"0{self.minutes}" if self.minutes < 10 else f"{self.minutes}"
        formatted_seconds = f"0{self.seconds}" if self.seconds < 10 else f"{self.seconds}"
        return f"{formatted_minutes}:{formatted_seconds}"


watch = Stopwatch()
for _ in range(3600):
    print(watch)
    watch.tick()