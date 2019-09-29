a=[1,1,2,3]
tuple(a)
print(a)
b=list(a)
print(len(b))
c=set(b)
print(len(c))
d=list(c)
print(len(d))
e=[]
e.append(list(range(1,10)))
print(e)
#1-2-3-4-5
dictDirectory={"Jane Doe": "+27 555 5367","John Smith": "+27 555 6254","Bob Stone": "+27 555 5689"}
t=[]
t.append(dictDirectory.items())
print(len(t[0]))
v=list(dictDirectory.values())
k=list(dictDirectory.keys())
s="antidisestablishmentarianism"
s2=""
sC=sorted(s)
for i in range(len(sC)):
    s2+=(sC[i])
print(s2)
w=[]
stringe="the quick brown fox jumped over the lazy dog"
w.append(stringe.split(" "))
print(w)
#6-7-8-9-10