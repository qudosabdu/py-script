# Function
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)
    
# print(factorial(5))

# sum of n number.....
def sum_natural(n):
    return sum_natural(n+1) + 1

print(sum_natural(5))