dictDirectory={"Jane Doe": "+27 555 5367","John Smith": "+27 555 6254","Bob Stone": "+27 555 5689"}

dictDirectory["Jane Doe"]= "+27 555 1024"

dictDirectory["Anna Cooper"]="+27 555 3237"

if "Bob Stone" in dictDirectory:
    print(dictDirectory["Bob Stone"])
else:
    print("None")
print(dictDirectory.keys())
print(dictDirectory.values())
print(dictDirectory.items())