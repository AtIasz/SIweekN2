def my_gen(n):
    while n > 0:
        yield n
        n-=1
my_gen(9)
for x in my_gen(5):
    print(x)