# format method 
words = 'I am {}, my age is {}'.format('abdul Qudoos', 23) 
# print(words)


words = 'I am {1}, my age is {0}'.format('abdul Qudoos', 23)

# print(words) # I am 23, my age is abdul Qudoos

words = 'I am {0}, my age is {1}'.format('abdul Qudoos', 23)
# print(words) # I am abdul Qudoos, my age is 23

words = 'I am {0} and my age is {1} and my habby is {2} '.format('abdul Qudoos', 23, "footbal")
# print(words) # 


# Lists
mys_list = ["abdul", "Engineerr", 23, "Pakistan", "Karachi"]
# print(mys_list)
# print(mys_list[-5:-2])

my_list2 = ["Work", "Experience"]
mys_list.extend(my_list2)
#print(mys_list) # ['abdul', 'Engineerr', 23, 'Pakistan', 'Karachi', 'Work', 'Experience']


# Tuple
my_touple = ("abdul", "Engineer", 23, "Pakistan", "Karachi")
# print(my_touple)
# print(my_touple[3:])


a = ("a",) # tuple with single element
b = ("a") # string not a tuple
# print(type(a)) # <class 'tuple'>
# print(type(b)) # <class 'str'>

# Now create tuple through constructor

abc = tuple(("a","b","c"))
# print(abc)

# Identity operator

name1 = "Abdul Qudoos"
name2 = "Abdul Qudoos"

# print(id(name1))
# print(id(name2))
# print(name1 == name2) #Return True It Match by value


list1 = ["a", "b", "c"]
list2 = ["a", "b", "c"]


# print( list== list2) #Return False It Match by ID
# print(id(list1)) #3218771147776
# print(id(list2)) #3218771144000

# Use method Sort and Reverse
list_sort = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
list_sort.sort()

# print(list_sort) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list_sort.reverse()
print(list_sort) #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

list_names = ["Abdul", "Qudoos", "Ali", "Ahmed", "Zain", "Zohaib","Abdul"]
count = list_names.count("Abdul")

print(count)









