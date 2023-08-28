a = 1


def parent():
    def confusion():
        return sum
    return confusion()


print(parent())  # 5
print(a)  # 1

# 1 - start with local
# 2 - parent local scope
# 3 - global
# 4 - built in python functions
