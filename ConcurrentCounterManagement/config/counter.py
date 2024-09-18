import threading

# TODO: Implement the methods of Counter class
class Counter:
    def __init__(self, initial_count):
        # code here
        self.initial_count = initial_count

    def incValue(self, offset):
        # TODO: method to increase the value of counter by `offset`
        self.initial_count += offset

    def getValue(self):
        # TODO: method to get the current value of counter by
        return self.initial_count

    def decValue(self, offset):
        # TODO: method to decrease the value of counter by `offset`
        self.initial_count -= offset



# Function for concurrent increment operation
def concurrent_inc(counter, offset):
    for _ in range(1000):
        counter.incValue(offset)


# Function for concurrent decrement operation
def concurrent_dec(counter, offset):
    for _ in range(1000):
        counter.decValue(offset)


# Create a Counter instance with initial value 0
counter = Counter(0)

# Create and start multiple threads for concurrent increment and decrement
threads = []
for _ in range(10):
    thread_inc = threading.Thread(target=concurrent_inc, args=(counter, 1))
    thread_dec = threading.Thread(target=concurrent_dec, args=(counter, 1))
    threads.append(thread_inc)
    threads.append(thread_dec)
    thread_inc.start()
    thread_dec.start()

# TODO: Wait for all threads to complete
for thread in threads:
    # code here
    # thread.start()
    thread.join()

# Check the final value of the counter
print("Final counter value:", counter.getValue())