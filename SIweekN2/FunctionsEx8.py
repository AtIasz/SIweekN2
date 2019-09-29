import math
a = lambda x: x**2
a = lambda x,y: math.sqrt(x**2+y**2)
a = lambda *args: sum(args)/len(args)
a = lambda s: "".join(set(s))
def square(x):
    return x**2
def sqrt(x,y):
    return (x**2+y**2)
def avg(*args):
    return(sum(args)/(len(args)))
def uniq(s):
    return("".join(set(s)))