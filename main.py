import math


def plus(a,b):
    res = math.pow(a,b)
    return res

def minus(a,b):
    return a-b

if __name__ == '__main__':
    print(plus(2,3))
    print(minus(8,3))