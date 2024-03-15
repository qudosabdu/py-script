# loop 

# for loop
for i in range(10):
    print(i, end=' ')  # end=' ' is used to print the output in a single line

# while loop
i = 0
while i < 10:
    print(i, end=' ')
    i += 1

# nested loop 
for i in range(5):
    for j in range(5):
        print('*', end=' ') 
    print()


# # break statement 
# for i in range(10):
    # if i == 5:
        # break  # terminate the loop
    # print(i, end=' ')

# # continue statement
# for i in range(1, 11):
    # if i == 5:
        # continue # skip the rest of the code inside the loop for the current iteration
    # print(i, end=' ')

# # pass statement
# for i in range(1, 11):
#     if i == 5:
#         pass # do nothing
#     print(i, end=' ')
    

my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i, end=' ')


# # for loop with else
for i in range(10):
    print(i, end=' ')
else:
    print('All done!')

# # while loop with else
i = 0
while i < 10:
    print(i, end=' ')
    i += 1
else:
    print('All done!')

# # nested loop with else
for i in range(5):
    for j in range(5):
        print('*', end=' ') 
    print()
else:
    print('All done!')

