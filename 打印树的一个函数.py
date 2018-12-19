'''
     深度 前空格 元素间空格
     1     7       0
     2     3       7
     3     1       3
     4     0       1
'''

import math

def print_tree(array): #打印堆排序使用
    # first=[0]
    # first.extend(array)
    # array=first
    index = 1
    depth = math.ceil(math.log2(len(array))) # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1), end='')
        line = array[index:index + offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')
        index += offset
        print()

print_tree([1,2,3,4,5,5,6,6,6,5])
