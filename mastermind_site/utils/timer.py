import time

class GameTimer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.duration = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.end_time = time.perf_counter()
        if self.start_time is not None:
            self.duration = self.end_time - self.start_time

    def get_duration(self):
        return self.duration if self.duration is not None else 0

    def __str__(self):
        """Provide a string representation of the duration."""
        return f"Duration: {self.get_duration():.2f} seconds."
