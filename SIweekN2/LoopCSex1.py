n=1
eq=0
while n<200:
    eq+=n**2
    n+=1
print(n,eq)

n=10
word="madafaka"
while n>0:
    x=input("Guess a letter in the word dummie: ")
    if x in word:
        print(f"You guessed right, {x} is in the word")
    else:
        print(f"Sorry, but {x} is not in the word")
    n-=1
    print(f"{n} tries left.")