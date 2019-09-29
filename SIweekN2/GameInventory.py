'''
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def display_inventory(kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
       

display_inventory(inv)
#1
''' 
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def display_inventory(kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
       

def add_to_inventory(*args,**kwargs):
    dictOfWords = {"",1}
    for i in range(len(args)):
        dictOfWords ={args[i],1}
        
    print(dictOfWords.values())


display_inventory(inv)
print(inv)
add_to_inventory(*dragon_loot,**inv)