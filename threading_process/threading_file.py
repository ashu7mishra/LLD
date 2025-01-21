import concurrent
import threading
import concurrent.futures as futures
from time import sleep


def hello(t):
    while True:
        sleep(t)
        return f'hello from {threading.current_thread()}'

# thread1 = threading.Thread(target=hello, args=[4], name='thread1')
# thread2 = threading.Thread(target=hello, args=[3], name='thread2')
# thread3 = threading.Thread(target=hello, args=[2], name='thread3')
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# thread1.join()
# thread2.join()
# thread3.join()

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    f1 = executor.submit(hello, 4)
    f2 = executor.submit(hello, 3)
    f3 = executor.submit(hello, 2)

    result1 = f1.result()
    result2 = f2.result()
    print(result2)
    result3 = f3.result()

    print(result1)
    # print(result2)
    print(result3)


