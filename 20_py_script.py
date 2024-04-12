
#Multi inheritance classes in python


#Parent classs
class Persion():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def welcome(self):
        print(f"Welcome {self.name}, and your age is {self.age}")

class Game():
    def __init__(self, game):
        self.game = game

# child class

class Student(Persion,Game):
    def __init__(self, name, age, email, game):
        super().__init__(name, age, game)
        self.email = email
        
p1 = Persion("Abdul Qudoos", 23)
g1 = Game("Football") 
s1 = Student("Abdul Qudoos", 22, "abc@gmail.com", "Football")
print(p1.name)
# p1.welcome()
# print(s1.age)
# print(s1.email)
# print(g1.game)
