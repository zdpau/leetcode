# 递推,即备忘录法，与斐波那契基本一样
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
def cnk(n,k):
    if k==0: return 1
    if n==0: return 0
    return cnk(n-1,k)+cnk(n-1,k-1)

cnk(10,7)

# 迭代
from collections import defaultdict

def f(n,k):
    c[n,k] = defaultdict(int)
    for row in range(n+1):
        c[row,0]=1
        for col in range(1,k+1):
            c[row,col] = c[row-1, col-1]+ c[row-1, col]
    print(c[n,k])
        
f(10,7)
