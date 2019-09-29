
n=99
a=0
print("odd nums do nothing, even numbers get printed out, number'99' exits the program")
while a!=n: 
    try:
        a=int(input())
    except ValueError:
        pass
    if a%2==0:
        print(str(a))

#1
avg=0
a=1
nOt=0
while a>=0: 
    try:
        a=int(input())
        if a>0:
            avg+=a
            nOt+=1
    except ValueError:
        print("Give me positive numbers, or one negative to finish")
print(avg/nOt)
#2

print('''-- Calculator Menu --
0. Quit
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers'''
)
n=5
while n>0:
    try:
        n=int(input())
        if n==1:
            try:
                a=int(input("(Summation)First number: "))
                b=int(input("Second number: "))
                print()
                print(f"{a}+{b}="+str(a+b))
                      
            except ValueError:
                print("Only numbers please")
                print('''-- Calculator Menu --
0. Quit
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers'''
)  
        if n==2:
            try:
                a=int(input("(Subtraction)First number: "))
                b=int(input("Second number: "))
                print()
                print(f"{a}-{b}="+str(a-b))
                      
            except ValueError:
                print("Only numbers please")
                print('''-- Calculator Menu --
0. Quit
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers'''
) 
        if n==3:
            try:
                a=int(input("(Multiply)First number: "))
                b=int(input("Second number: "))
                print()
                print(f"{a}x{b}="+str(a*b))
                      
            except ValueError:
                print("Only numbers please")
                print('''-- Calculator Menu --
0. Quit
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers'''
) 
        if n==4:
            try:
                a=int(input("(Divide)First number: "))
                b=int(input("Second number: "))
                print()
                print(f"{a}/{b}="+str(a/b))
                      
            except ValueError:
                print("Only numbers please")
                print('''-- Calculator Menu --
0. Quit
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers'''
)                  
    except ValueError:
        print("Give me positive numbers (0-4)")
    print()
    if n!=0:
        print('''-- Calculator Menu --
    0. Quit
    1. Add two numbers
    2. Subtract two numbers
    3. Multiply two numbers
    4. Divide two numbers'''
    )
#3