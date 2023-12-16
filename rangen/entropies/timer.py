import random

import time

class Timer:
    def __init__(self):
        self.kof = lambda: random.uniform(-1000, 1000)
        self.mult_or_div = lambda: random.choice(['*', '/'])
        self.add_or_sub = lambda: random.choice(['+', '-'])
        self.timestamp = eval(f'{time.perf_counter()} {self.mult_or_div()} {self.kof()}')

    def off(self):
        timestamp_after_operation = eval(f'{time.perf_counter()} {self.mult_or_div()} {self.kof()}')
        return abs(eval(f'{timestamp_after_operation} {self.add_or_sub()} {self.timestamp}'))
