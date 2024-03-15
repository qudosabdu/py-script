# function


# def add(a, b):
#     return a + b

# print(add(1, 2))


# def multiply(a, b):
#     return a * b

# print(multiply(3, 2))

# def your_name(name):
#     return 'Hello' + ' ' + name

# print(your_name('John'))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(15)) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610


def reverse_number(n):
    rev = 0
    while n > 0:
        rem = n % 10 # 12345 % 10 = 5
        rev = rev * 10 + rem # 0 * 10 + 5 = 5
        n = n // 10 # 12345 // 10 = 1234
    return rev

print(reverse_number(12345)) # 54321

def reverse_string(s):
    return s[::-1] # slicing

print(reverse_string('hello')) # olleh

def reverse_list(l):
    return l[::-1]

print(reverse_list([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]


def reverse_tuple(t):
    return t[::-1]

print(reverse_tuple((1, 2, 3, 4, 5))) # (5, 4, 3, 2, 1)


def reverse_dictionary(d):
    return {v: k for k, v in d.items()}

print(reverse_dictionary({1: 'one', 2: 'two', 3: 'three'})) # {'one': 1, 'two': 2, 'three': 3}


