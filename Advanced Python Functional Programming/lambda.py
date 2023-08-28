from functools import reduce
# lambda expressions
# lambda params: expression

my_list = [1, 2, 3]

# multiple by 2
print(list(map(lambda item: item * 2, my_list)))

# only odd
print(list(filter(lambda item: item % 2 != 0, my_list)))

# reduce accumulate all item in list
print(reduce(lambda acc, item: acc + item, my_list, 0))
print(my_list)
