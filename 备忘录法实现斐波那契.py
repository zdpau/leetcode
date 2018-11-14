from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args] # 之前加了else这一逻辑，其实不对。
    return wrap

@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i-1)+fib(i-2)

fib(100)
