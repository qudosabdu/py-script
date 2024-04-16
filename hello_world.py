
# multiple arguments
# def funargs(normal, *args):
#     for name in args:
#         print(normal)
#         print(name, end=", ")

# normal = "This is normal argument"
# har = ["abdul qudoos", 'saad', 'essa khan']
# funargs(normal, *har)


#***** Multiple args, kwargs ****#
# def funargs(normal, *args, **kwargs):
#     print(normal)
#     for name in args:
#         print(name, end=", ")
#     for key , value in kwargs.items():
#         print(f"{key} is a {value}")
        

# normal = "This is normal argument"
# har = ["abdul qudoos", 'saad', 'essa khan']
# kw = {"Abdul":"Developer", "Uzair":"Student", "Asif":"Teacher"}

# funargs(normal, *har, **kw)


# TIME Module
# "Extract execution time"
# import time

# initial = time.time()

# i = 0;
# while (i<10):
#     print("This is abdul qudoos")
#     i += 1

# print("for loop ran in", time.time()- initial)

# initial2 = time.time()
# for i in range(10):
#     print("This is abdul qudoos")
#     time.sleep(2)
    
# print("While loop ran in", time.time()- initial)

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)


# Enumerate function
# i = 1
# list1 = ["Bhindi","Aloo", "chopsticks","chowmein"]
# for item in list1:
#     if i%2 != 0:
#         print(item)
#     i += 1
 
# for index, item in enumerate(list1):
#     if index % 2 == 0:
#         print(item)


# JOIN FUNCTION
# list_names = ["John", "cena", "Randy", "ortan", "Sheamus", "Khali"]
# for item in list_names:
#     print(item, "and", end=" ")

# a = " and ".join(list_names)
# print(a)


# MAP Function Filter

# numbers = ["3","34", "64"]

# for item in range(len(numbers)):
#     numbers[item] = int(numbers[item])
# numbers[2] = numbers[2] + 1
# print(numbers[2])   

# now use map function
# numbers = list(map(int, numbers) )
# numbers[2] = numbers[2] + 1
# print(numbers[2]) 

# num = [2,3,4,5,6,23,45,11]
# def is_greater_5(nums):
#     return nums > 5
# is_greater_5 = list(filter(is_greater_5, num))
# print(is_greater_5)



# DECORATOR 

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return int
# a = funcret(0)
# print(a)

# def dec1(func1):
#     def nowexec():
#         print("Executing now")
#         func1()
#         print("Executed")
#     return nowexec

# def who_is_abdul():
#     print("Abdul is a Developer")

# who_is_abdul = dec1(who_is_abdul)
# who_is_abdul()

# the above is decorator but there is another method to write
# "who_is_abdul = dec1(who_is_abdul)" as below

# def dec1(func1):
#     def nowexec():
#         print("Executing now")
#         func1()
#         print("Executed")
#     return nowexec

# @ dec1
# def who_is_abdul():
#     print("Abdul is a Developer")

# # who_is_abdul = dec1(who_is_abdul)
# who_is_abdul()


# CLASSES

# class Employee:
#     no_of_leaves = 8
#     pass

# abdul = Employee()
# hashim = Employee()

# abdul.name = "Qudoos"
# abdul.salary = 4000
# abdul.role = "Developer"

# hashim.name = "Hashim Khan"
# hashim.salary = 3000
# hashim.role = "Teacher"

# print(abdul.name)
# print(abdul.no_of_leaves)
# print(Employee.__dict__)


# class Employee:
#     no_of_leaves = 8
#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role
#     def print_details(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

# abdul = Employee("Abdul Qudoos", 4000, "Developer")
# hashim = Employee("Hashim Khan", 3000, "Teacher")


# *We will use constructor(to give argument to class Employee)* instead declearin variables
# abdul.name = "Qudoos"
# abdul.salary = 4000
# abdul.role = "Developer"

# hashim.name = "Hashim Khan"
# hashim.salary = 3000
# hashim.role = "Teacher"

# print(abdul.name)
# print(abdul.no_of_leaves)
# print(abdul.print_details())  #Name is Qudoos. Salary is 4000 and role is Developer


# ** Class Methods ** #

# class Employee:
#     no_of_leaves = 8
#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role
#     def print_details(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
#     @classmethod # class method
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

# abdul = Employee("Abdul Qudoos", 4000, "Developer")
# hashim = Employee("Hashim Khan", 3000, "Teacher")

# # Employee.no_of_leaves = 89
# abdul.change_leaves(34)
# print(abdul.no_of_leaves)


# ** class method vs alternative constructor** #
# class Employee:
#     no_of_leaves = 8
#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role
#     def print_details(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
#     @classmethod # class method
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#     @classmethod
#     def from_dash(cls, string):
#         param = string.split("-")
#         return cls(param[0], param[1], param[2])
    

# abdul = Employee("Abdul Qudoos", 4000, "Developer")
# hashim = Employee("Hashim Khan", 3000, "Teacher")
# essa = Employee.from_dash("Essa-480-Student")

# Employee.no_of_leaves = 89
# abdul.change_leaves(34)
# print(abdul.no_of_leaves)
# print(essa.name)



# ** Static method ** #

# class Employee:
#     no_of_leaves = 8
#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role
#     def print_details(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
#     @classmethod # class method
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#     @classmethod
#     def from_dash(cls, string):
#         param = string.split("-")
#         return cls(param[0], param[1], param[2])
#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)
#         return "Khatm"
    

# abdul = Employee("Abdul Qudoos", 4000, "Developer")
# hashim = Employee("Hashim Khan", 3000, "Teacher")
# essa = Employee.from_dash("Essa-480-Student")

# print(essa.printgood("Abdul"))


# ** Abstraction and Encapsulation ** #
# ** Inheritance ** #

# class Employee:
#     no_of_leaves = 8
#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role
#     def print_details(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
# class Programmer(Employee):
#     def __init__(self, name, salary, role, languages):
#         self.name = name
#         self.salary = salary
#         self.role = role
#         self.languages = languages
        
        
#     def printprog(self):
#         return f"Programmer's name is {self.name}. Salary is {self.salary} and role is {self.role} and the languages are {self.languages}"
    
# abdul = Programmer("Abdul Qudoos", 4000, "Developer",['javascript','python','sql'])
# print(abdul.printprog())


# ** Multiple Inheritance ** #

# class Employee:
#     no_of_leaves = 8
#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role
#     def print_details(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


# class Player:
#     no_of_game = 4
#     def __init__(self, name, game):
#         self.name = name
#         self.game = game
    
#     def printdetails(self):
#         return f"The name is {self.name} and Game is"
        
        
# class CoolProgrammer(Employee, Player):
#     language = "C++"
#     def printlanguage(self):
#         print(f"the programming languages are {self.language}")

# employee1 = Employee("Abdul Qudoos", 2000, "Dev")

# player1 = Player("Sajid Khan", ["Cricket"])
# programmer = CoolProgrammer("Shoib", 4000, "coool programmer")

# details = programmer.printdetails()
# print(details)
# print(player1.name)
# print(programmer.name)
# print(programmer.salary)
# programmer.printlanguage()


# ** Multilevel Inheritance ** #

class Dad:
    basketball = 1

class Son(Dad):
    dance = 3
    basketball = 3
    def isdance(self):
        return f"Yes I dance {self.dance}"

class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"Jackson Yeah "\
            f"Yes I dance very awesome..."
            

darry = Dad()
larry = Son()
merry = Grandson()
print(merry.isdance())
print(merry.basketball)