# interable
# iterate
# generators (iterable)


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i * 2)
#     return result

# yield pauses the function and come back to it when we do something to it, which was called 'next'
def generator_function(num):
    for i in range(num):
        yield i * 2


# g = generator_function(100)
# print(g)
# next(g)
# next(g)
# print(next(g))

# print(next(g))

for item in generator_function(1000):
    print(item)
