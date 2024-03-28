# conditional statement

# if-else statement
# x = 10
# if x > 5:
#     print('x is greater than 5')
# else:
#     print('x is less than 5')

# if-elif-else statement

# x = int(input('Enter a number: '))

# if x > 5:
#     print('x is greater than 5')
# elif x < 5:
#     print('x is less than 5')
# else:
#     print('x is equal to 5')


#find the given number is prime number or not

num = int(input("Enter your number: "))
prime = True

for i in range(2, num):
    if(num % i == 0):
        prime = False;
        break;
if prime:
    print("The given number is prime")
else:
    print("The given number is not Prime number")

