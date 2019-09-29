summ=0
for i in range(1,10):
    summ+=i
print(summ)
#1
#2 Yes, using while
factoriall=5
fsum=1
for i in range(1,6):
    fsum*=i
print(fsum)
#3
fn=(1.9,0.5,3.8,4.4,5.23,6.2,7.74,3.11,8.3,9.11)
summ=0
prod=1
avg=0
for i in range(len(fn)):
    summ+=fn[i]
    prod*=fn[i]
avg=summ/len(fn)
print(summ,prod,avg)
    
