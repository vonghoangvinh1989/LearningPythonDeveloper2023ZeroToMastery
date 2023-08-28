# Decorators
def my_decorator(input_function):
    def wrap_function(*args, **kwargs):
        input_function(*args, **kwargs)
    return wrap_function


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


# hello('hiiiii')
hello('hiiiii', ':)')

# what decorator does under the hood
# my_decorator(hello)()
