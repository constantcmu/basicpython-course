class One:
    name = 'Aood'

    def __init__(self,name):
        self.name = name 
    
    def walk(self):
        print('ฉันเดินได้')

class Two:
    nickname = 'aoo'
    
    def __init__(self,name,nickname):
        super().__init__(name)
        self.nickname = nickname

class Three(One):

    def eat(self):
        print('ฉันกินได้')

class Four(One,Two):
    def fly(self):
        print('ฉันบินได้')

if __name__ == '__main__':
    three = Three('aaaa')
    print(three.name)

    three.eat()
    three.walk()