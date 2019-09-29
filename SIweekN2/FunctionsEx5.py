def calculator(x,y,z):
    poss=["+","-","/",":","*","x"]
     
    if z in poss:
        if z=="+":
            r=x+y
        if z=="-":
            r=x-y
        if z=="/" or z==":":
            r=x/y
        if z=="*" or z=="x":
            r=x*y
            
    else:
        raise ValueError("Numbers must be higher than 0.\nUsable operators: '+', '-' ,'/' ,':' ,'*' ,'x'.")
    return r
    
    
    
print(calculator(2,3.0,"+"))
print(int(calculator(2,3.0,"+")))
print(calculator(2,3.0,"/"))
print(int(calculator(2,3.0,"/")))
