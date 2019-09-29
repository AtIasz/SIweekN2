months=["January","February","March","Aperil","May","June","July","September","October","November","December"]
d=[31,28,31,30,31,30,31,31,30,31,30,31]
dictMonths={}
for i in range(len(months)):
    dictMonths[months[i]]=d[i]
print(dictMonths)
#a
Months={}
r=0
while r<len(months):
    Months[months[r]]=d[r]
    r+=1
print(Months)
#b