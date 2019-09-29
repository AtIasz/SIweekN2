F=False
while F==False:
    try:
        T_f=float(input("Give me the temperature in Fahrenheit: "))
        F=True
    except ValueError:
        print("Only numbers are acceptable.")
T_c=(5/9)*(T_f-32)
print("The temperature in Celsius is: "+str(T_c))