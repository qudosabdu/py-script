
#inheritance classes in python


#Parent classs
class Persion():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def welcome(self):
        print(f"Welcome {self.name}, and your age is {self.age}")


# child class

class Student(Persion):
    def __init__(self, name, age, email):
        super().__init__(name, age)
        self.email = email
        
p1 = Persion("Abdul Qudoos", 23) 
s1 = Student("Abdul Qudoos", 22, "abc@gmail.com")
print(p1.name)
# p1.welcome()
print(s1.age)
print(s1.email)

