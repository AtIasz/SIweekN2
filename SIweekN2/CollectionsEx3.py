a=set()
b=set()
n=1
while len(a)!=4:
    a.add(n)
    n+=1
n=1
while len(b)!=4:
    if n%2!=0:
        b.add(n)
    n+=1

print(a)
print(b)
c=set(a.union(b))
print(c)
d=set(a)
d.difference_update(b)
print(d)
e=set(b)
e.difference_update(a)
print(e)
f=set()
f.update(a,b)
print(f)
print(len(c))