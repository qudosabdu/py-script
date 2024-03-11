# File hanling

# Open a file
# Open the file in read mode ("r")
file = open("test.txt", "r")

# Read the contents of the file
content = file.read()

# Print the content to the console
# print(content)

# Close the file
file.close()

# Write to a file
file.write("Hello World")


# import os module
import os
import os.path
os.makedirs("test_01")

# list all files in the directory
print(os.listdir())

# view the current directory
print(os.listdir('.'))

# check if a file exists
print(os.path.exists('test.txt'))
print(os.path.exists('test_01'))


# remove a file directory
os.rmdir('test_01')

# remove a file
os.remove('test.txt')



