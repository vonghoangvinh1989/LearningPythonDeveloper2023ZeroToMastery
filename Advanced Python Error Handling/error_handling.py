# Error Handling
def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum(1, '2'))

# while True:
#     try:
#         age = int(input('What is your age? '))
#         10 / age
#     except ValueError:
#         print('please enter a number')
#     except ZeroDivisionError:
#         print('please enter age higher than 0')
#     else:
#         print('thank you!')
#         break
