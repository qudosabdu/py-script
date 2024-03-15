# File hanling

# Open a file
# Open the file in read mode ("r")
# file = open("test.txt", "r")

# Read the contents of the file
# content = file.read()

# Print the content to the console
# print(content)

# Close the file
# file.close()

# Write to a file
# file.write("Hello World")


# import os module
import os
import os.path
# os.makedirs("test_01")

# # list all files in the directory
# print(os.listdir())

# # view the current directory
# print(os.listdir('.'))

# # check if a file exists
# print(os.path.exists('test.txt'))
# print(os.path.exists('test_01'))


# # remove a file directory
# os.rmdir('test_01')

# # remove a file
# os.remove('test.txt')



#list methods

# append() - Adds an element at the end of the list
# clear() - Removes all the elements from the list
# copy() - Returns a copy of the list
# count() - Returns the number of elements with the specified value
# extend() - Add the elements of a list (or any iterable), to the end of the current list
# index() - Returns the index of the first element with the specified value
# insert() - Adds an element at the specified position
# pop() - Removes the element at the specified position
# remove() - Removes the item with the specified value
# reverse() - Reverses the order of the list
# sort() - Sorts the list


my_list = [1, 2, 3, 4, 5]
print(my_list)


# append() - Adds an element at the end of the list
my_list.append(6)
print(my_list)


# clear() - Removes all the elements from the list
my_list.clear()
print(my_list)


# copy() - Returns a copy of the list  
my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
print(new_list)


# count() - Returns the number of elements with the specified value
my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(my_list.count(1))


# extend() - Add the elements of a list (or any iterable), to the end of the current list
my_list = [1, 2, 3, 4, 5]
new_list = [6, 7, 8, 9, 10]
my_list.extend(new_list)
print(my_list)


# index() - Returns the index of the first element with the specified value
my_list = [1, 2, 3, 4, 5]
print(my_list.index(3))



# insert() - Adds an element at the specified position
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)  
print(my_list)


# pop() - Removes the element at the specified position
my_list = [1, 2, 3, 4, 5]
my_list.pop(2)
print(my_list)


# remove() - Removes the item with the specified value
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)


# reverse() - Reverses the order of the list
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)


# sort() - Sorts the list
my_list = [5, 2, 3, 4, 1]
my_list.sort()
print(my_list)

# # list comprehension
# # [expression for item in iterable]

# # create a list of squares
squares = [i * i for i in range(10)]  # 0 1 4 9 16 25 36 49 64 81
print(squares)

# # create a list of even numbers
even_numbers = [i for i in range(10) if i % 2 == 0]  # 0 2 4 6 8
print(even_numbers)


# # create a list of odd numbers
odd_numbers = [i for i in range(10) if i % 2 != 0]  # 1 3 5 7 9
print(odd_numbers)


## create a list of prime numbers
prime_numbers = [i for i in range(2, 20) if all(i % j != 0 for j in range(2, i))]
print(prime_numbers)





