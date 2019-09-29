person = {}

for prop in ["name", "surname", "age", "height", "weight"]:
    if prop=="name" or prop=="surname":
        person[prop] = input("Please enter your %s: " % prop)
    elif prop=="age":
        person[prop] = int(input("Please enter your %s: " % prop))
    elif prop=="height" or prop=="weight":
        person[prop] = float(input("Please enter your %s: " % prop))
    
