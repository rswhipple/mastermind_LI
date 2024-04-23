# utils/timer.py
import time

class GameTimer:
    def __init__(self):
        self.start_t = None
        self.end_t = None
        self.dur = None

    def start(self):
        self.start_t = time.perf_counter()

    def stop(self):
        self.end_t = time.perf_counter()
        if self.start_t is not None:
            self.dur = self.end_t - self.start_t

    def get_duration(self):
        if self.dur is None:
            return "Duration: Not available."
        return f"Duration: {self.dur:.2f} seconds."

