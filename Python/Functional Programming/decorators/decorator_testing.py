# Testing Different types of Decorators

print('\nDecorator with no arguments\n')
def decorator(func):
    def wrapper(*args, **kwargs):
        print('decorator')
        return func(*args, **kwargs)
    return wrapper

@decorator
def test():
    print('test')

test()

print('\nDecorator with arguments\n')

def decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('decorator')
            print(arg1)
            print(arg2)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_args('arg1', 'arg2')
def test():
    print('test')

test()

print('\nDecorator with arguments and function arguments\n')

def decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('decorator')
            print(arg1)
            print(arg2)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_args('arg1', 'arg2')
def test(arg1, arg2):
    print('test')
    print(arg1)
    print(arg2)

test('arg1', 'arg2')


print('\nRepetition Decorator\n')

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                print('decorator')
                func(*args, **kwargs)
        return wrapper
    return decorator#

def decorator(func, num_times):
    def wrapper(*args, **kwargs):
        for _ in range(num_times):
            print('decorator')
            func(*args, **kwargs)
    return wrapper

@repeat(4)
def test():
    print('test')

test()

def test2():
    print('test2')

test2 = repeat(4)(test2) # Currying the function - passing the function to the decorator and then passing the result of the decorator to the function
test2()

def test3():
    print('test3')

@decorator(test3, 4)
def test3():
    print('test3')

test3 = decorator(test3, 4)
# == test3 = wrapper(*args, **kwargs)
# == test3 = test3(*args, **kwargs)

test3()