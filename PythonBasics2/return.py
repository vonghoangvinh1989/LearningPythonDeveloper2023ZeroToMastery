def sum(num1, num2):
    def another_function(n1, n2):
        return n1 + n2
    return another_function(num1, num2)

# should do one thing really well.
# should return something.


total = sum(10, 20)
print(total)
