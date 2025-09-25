# # for x in "Chaithanya":
# #     print(x)

# # for i in [1, 2, 3, 4]:
# #     print(i)

# # command = ""
# # # while command != "quit" and command != "QUIT":
# # while command.lower() != "quit":
# #     command = input(">")
# #     print("ECHO", command)

# # num1 = 1
# # num2 = 10
# # count = 0
# # # for i in range(num1, num2):
# # for i in range(1, 10):
# #     if (i % 2) == 0:
# #         print(i)
# #         count += 1
# # print("total even numbers between 1 and 10 is", count)

# def greet():
#     print("hi Chai..!")


# greet()


# def greet_argument(fname, lname):
#     print(f"Hi {fname} {lname}")
#     print("Welcome..!")


# greet_argument("Chai", "Duvalkar")


# def increment(num, another, by=1):
#     return num+another+by


# print(increment(8, 1))


# def multiply(x, y):
#     return x*y


# print(multiply(3, 3))


# def multiply(*numbers):
#     total = 1
#     for i in numbers:
#         total *= i
#     return total


# print(multiply(2, 3, 4, 5))

def print_reverse(n):
    if n == 0:
        return
    print(n)
    print_reverse(n-1)


print_reverse(10)


def printNumbers(n):
    if n == 0:
        return
    printNumbers(n-1)
    print(n)


printNumbers(10)
