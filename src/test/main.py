import threading
from time import sleep

class SharedCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.num = 0

    def increment(self):
        with self.lock:
            self.num += 1

    def get_value(self):
        with self.lock:
            return self.num


counter = SharedCounter()  # Create a shared counter instance


def work():
    while True:
        counter.increment()


def get_count():
    return counter.get_value()


# Create and start threads
thread1 = threading.Thread(target=work)
thread2 = threading.Thread(target=work)

thread1.start()
thread2.start()
current_count = get_count()
print(current_count)
sleep(5)
current_count = get_count()
print(current_count)
sleep(2)
current_count = get_count()
print(current_count)
