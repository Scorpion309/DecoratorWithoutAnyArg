def get_args_for_decorator(*args, start):
    def decorator(func):
        def wrapper():
            func(args, start)

        return wrapper

    return decorator


if __name__ == '__main__':
    @get_args_for_decorator(1, 2, 3, 5, 6, start=3)
    def args_without_first_arg(args, start):
        print(args[start:])


    args_without_first_arg()
