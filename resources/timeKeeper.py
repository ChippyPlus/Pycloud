from time import sleep, ctime
import threading


class channel:
    def __init__(self):
        self.lock = threading.Lock()
        self.counter = 0

    def increment(self):
        with self.lock:
            self.counter += 1

    def get(self):
        with open("logs/tasks.log", 'a') as f:
            f.write(f"{ctime()} [TIME] EXECUTED, GET\n")

        with self.lock:
            return self.counter


counter = channel()


def count():
    while True:
        counter.increment()
        sleep(1)
