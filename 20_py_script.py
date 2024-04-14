
#Multi inheritance classes in python


#Parent classs
class Persion():
    def __init__(self, name):
        self.name = name
    def welcome(self):
        print("Welcom from Person class>>>")
class Game():
    def __init__(self, game):
        self.game = game
    def welcome(self):
        print("Helo from Game class")

# child class

class Student(Persion,Game):
    def __init__(self, name, age, game):
        Persion.__init__(self, name)
        Game.__init__(self, game)
        self.age = age
        
s1 = Student("Abdul Qudoos", 22, "Football")
print(s1.name)
print(s1.age)
print(s1.game)
s1.welcome() #Welcom from Person class>>>

        
