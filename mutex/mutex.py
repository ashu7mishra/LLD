import threading

shared_variable = 0

def adder():
    global shared_variable
    for i in range(1000000):
        shared_variable += 1
    # return shared_variable


def subtractor():
    global shared_variable
    for i in range(1000000):
        shared_variable -= 1
    # return shared_variable


adder()
subtractor()
print(shared_variable)

thread1 = threading.Thread(target=adder)
thread2 = threading.Thread(target=subtractor)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(shared_variable)