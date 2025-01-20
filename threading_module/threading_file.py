import threading
from time import sleep


def hello():
    while True:
        sleep(0.2)
        print(f'hello from {threading.current_thread()}')

thread1 = threading.Thread(target=hello, name='thread1')
thread2 = threading.Thread(target=hello, name='thread2')

thread1.start()
thread2.start()

