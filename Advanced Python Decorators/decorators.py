# def hello(func):
#     func()


# def greet():
#     print('still here!')


# a = hello(greet)
# print(a)

# Higher Order Function HOC
def greet(func):  # function accepts inside other function
    func()


def greet2():  # function returns other function
    def func():
        return 5
    return func
