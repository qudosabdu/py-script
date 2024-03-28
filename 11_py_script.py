# Enumerate Function
#It Takes A collection (e.g tuple) and return it as an enumerate object

abc = ["a", "b", "c", "d"]
index = 10
b = enumerate(abc,index) # make an object and will start indexing from 10
#print(list(b)) #[(10, 'a'), (11, 'b'), (12, 'c'), (13, 'd')] # return list of tuple

# Now i want tuple
#print(tuple(b)) #((10, 'a'), (11, 'b'), (12, 'c'), (13, 'd'))

# Now i want Dictionary
# print(dict(b)) #{10: 'a', 11: 'b', 12: 'c', 13: 'd'}

tuple_abc = ["a", "b", "c", "d"]
tuple_obj = enumerate(tuple_abc,5)
# print(list(tuple_obj)) #[(5, 'a'), (6, 'b'), (7, 'c'), (8, 'd')]

