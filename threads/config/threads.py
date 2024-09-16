import threading


# Define the Adder class that inherits from threading.Thread
class Adder(threading.Thread):
    # TODO: Implement the logic to print "I am the Adder class"
    def __init__(self):
        super().__init__()
        print("I am the Adder class")

# Define the Subtractor class that inherits from threading.Thread
class Subtractor(threading.Thread):
    # TODO: Implement the logic to print "I am the Subtractor class"
    def __init__(self):
        super().__init__()
        print("I am the Subtractor class")

# Define the Client class with a static main method to manage thread execution
class Client:
    @staticmethod
    def main():
        # TODO: Print "I am the main class"
        # TODO: Initialize and start instances of Adder and Subtractor threads
        # TODO: Ensure that the main method waits for both threads to complete
        print("I am the main class")

        thread1 = Adder()
        thread2 = Subtractor()
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()



if __name__ == "__main__":
    Client.main()
