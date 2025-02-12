# def divide10By(num):
#     try:
#         print(10/num)
#     except ZeroDivisionError:
#         print("Division by Zero. change your input")
#         num = int(input())
#         divide10By(num)
#     except ValueError:
#         print("Input should be an integer.")
#         num = int(input())
#         divide10By(num)
#
#
#
# num = int(input())
# divide10By(num)

class TransactionFailed(Exception):
    def __init__(self, message):
        self.message = message

try:
    print("Transaction in progress.....")
    raise TransactionFailed("Failed Transaction")
except RuntimeError:
    print("Transaction Failed")
