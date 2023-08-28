# formatted strings

name = 'Johnny'
age = 55

print(f'hi {name}. You are {age} years old')

print('hi {new_name}. You are {age} years old'.format(
    new_name='sally', age=100))
print('hi {}. You are {} years old'.format("Cindy", 50))
print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))
