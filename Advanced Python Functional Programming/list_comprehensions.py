# list / set / dictionary comprehension
# my_list = [param for param in iterable]

# my_list = [char for char in 'hello']
# my_list2 = [number for number in range(0, 100)]
# my_list3 = [number ** 2 for number in range(0, 100)]
# my_list4 = [number ** 2 for number in range(0, 100) if number % 2 == 0]
# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)

# set
# my_set = {char for char in 'hello'}
# my_set2 = {number for number in range(0, 100)}
# my_set4 = {number ** 2 for number in range(0, 100) if number % 2 == 0}

# print(my_set)
# print(my_set2)
# print(my_set4)

# dict
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k: v ** 2 for k, v in simple_dict.items() if v % 2 == 0}
my_dict2 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict)
print(my_dict2)
