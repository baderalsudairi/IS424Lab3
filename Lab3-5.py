
x = int(input("Enter a number of repetitions: "))


def repeat_decorator(func):
    def wrapper():
        for _ in range(x):
            func()
    return wrapper


@repeat_decorator
def hello():
    print('Hello')


hello()
