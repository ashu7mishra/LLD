import threading_module


class FooBar:
    def __init__(self, n):
        # TODO: Initialize semaphores here
        self.n = n
        self.sem_foo = threading_module.Semaphore(1)
        self.sem_bar = threading_module.Semaphore(0)

    def foo(self):
        # TODO: Implement synchronization to ensure "foo" is printed before "bar"
        for i in range(self.n):
            self.sem_foo.acquire()
            print("foo", end='')
            self.sem_foo.release()

    def bar(self):
        # TODO: Implement synchronization to ensure "bar" is printed after "foo"
        for i in range(self.n):
            self.sem_bar.acquire()
            print("bar", end='')
            self.sem_bar.release()


def test_foobar():
    n = 5
    fb = FooBar(n)

    def foo():
        fb.foo()

    def bar():
        fb.bar()

    threads = [threading_module.Thread(target=foo), threading_module.Thread(target=bar)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    test_foobar()
