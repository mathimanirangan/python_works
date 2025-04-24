class Cat:
    species = 'mammal'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
cat1 = Cat("mathi",10)
cat2 = Cat("mani",55)
cat3 = Cat("Rang",40)

def oldestcat():
    if cat1.age > cat2.age:
        if cat1.age > cat3.age:
            print(f'The oldest cat is {cat1.age} years old')
    elif cat3.age > cat2.age:
        print(f'The oldest cat is {cat3.age} years old')
    else:
        print(f'the oldest cat is {cat2.age} years old')
        
oldestcat()

