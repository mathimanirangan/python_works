class PlayerCharacter:
    membership = True
    def __init__(self, name='anonymous',age=0):
        if(age>18):
            self.name = name
            self.age = age
    
    def shout():
        print(f'my name is {self.name}')
        return 'done'
    

player1 = PlayerCharacter('Tom',20)

print(player1.shout())