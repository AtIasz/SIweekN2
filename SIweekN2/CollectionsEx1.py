a=[]
b=[]
n=1
while len(a)!=3:
    if n%2!=0:
        a.append(n)
    n+=1
n=1
while len(b)!=3:
    if n%2==0:
        b.append(n)
    n+=1
#1-2
c=a+b
#3
d=sorted(c)
d.reverse()
#4
c[3]=42
#5
d.append(10)
#6
c.extend([7,8,9])
#7
print(c[0],c[1],c[2])
print(d[-1])
print(len(d))