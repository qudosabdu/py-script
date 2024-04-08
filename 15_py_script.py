# Map and Filter FUntion

# Map
my_list = [n for n in range(1,21)]

def add_func(x):
    return x + 10

new_list = list(map(add_func,my_list))
# print(new_list)

# Filter
def add_func(x):
    return x > 10

new_list = list(filter(add_func,my_list))
# print(new_list)

mul_func = lambda a: a * 2

mul_list = list(map(mul_func,my_list))
# print(mul_list)


a = [x for x in range(1,11)]
b = [x for x in range(11,21)]

def calc(x,y):
    return x,y

new_list = list(map(calc,a,b))
#print(new_list) #[(1, 11), (2, 12), (3, 13), (4, 14), (5, 15), (6, 16), (7, 17), (8, 18), (9, 19), (10, 20)]

