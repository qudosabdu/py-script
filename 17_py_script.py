# Decorator 
# can add new functionality to the object with any changes

def deco(func):
    def inner():
        print("Inner function of deco")
        func()
        print("Inner function of deco")
    return inner

@deco
def hello():
    print("Hello")
    
hello()