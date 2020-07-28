from functools import partial, update_wrapper


def wrapped_partial(func, *args, **kwargs):
    partial_func = partial(func, *args, **kwargs)
    print(partial_func())
    update_wrapper(partial_func, func)
    return partial_func


def addition(x, y, check):
    ans = x + y
    if ans == check:
        return True
    return False


wrapped_partial(addition, 2, 3, 5)
