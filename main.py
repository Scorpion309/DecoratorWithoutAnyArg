def get_args_for_decorator(start):
    def decorator(func):
        def wrapper(*args):
            func(args[start:])

        return wrapper

    return decorator

def args_without_first_arg(args_from_decorator):
    print(args_from_decorator)

if __name__ == '__main__':
    args_without_first_arg = get_args_for_decorator(3)(args_without_first_arg)



    args_without_first_arg(1, 2, 3, 4, 5, 6)
