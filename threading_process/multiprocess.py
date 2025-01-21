import multiprocessing
import concurrent.futures as futures
import time


def hello(t):
    time.sleep(t)
    print(f'hello from {multiprocessing.current_process().name}')

process1 = multiprocessing.Process(target=hello, args=(4,), name='process1')
process2 = multiprocessing.Process(target=hello, args=(3,), name='process2')
process3 = multiprocessing.Process(target=hello, args=(2,), name='process3')

process1.start()
process2.start()
process3.start()
