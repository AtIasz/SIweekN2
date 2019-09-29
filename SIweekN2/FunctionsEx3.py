import math
def hypotenuse(a,b):
    if type(a)==int and type(b)==int:
        x=a**2
        y=b**2
        z=x+y
        return math.sqrt(z)
    else:
        return None
print(hypotenuse("r","e"))