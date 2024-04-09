# Generator in Python

# def gen():
#     yield 1
#     yield 2
#     yield 3
# gen_num = gen()

# print(next(gen_num))
# print(next(gen_num))
# print(next(gen_num))


def gen():
    i = 1
    while i < 5:
        yield i
        i += 1
gen_num = gen()

# print(next(gen_num))
# print(next(gen_num))
# print(next(gen_num))
# print(next(gen_num))

# try:
#     print(x) # x is not defined
# except:
#     print("There is an error")
    
#zFill method
# x = "5"
# y = x.zfill(2)
# print(y) #05



