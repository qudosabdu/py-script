# Static Variable and Static Method

class Person:
    count= 0 # static variable
    
    @staticmethod
    def welcome():
        print("Welcome Abdul!")
p1 = Person()
print(p1.welcome())
print(Person.welcome())