from time import sleep
import threading

class channel:
    def __init__(self):
        self.lock = threading.Lock()
        self.counter = 0

    def increment(self):
        with self.lock:
            self.counter += 1

    def get(self):
        with self.lock:
            return self.counter

def count():
    while True:
        counter.increment()
        sleep(1)

counter = channel()

