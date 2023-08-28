# Try: This block will test the excepted error to occur
# Except:  Here you can handle the error
# Else: If there is no exception then this block will be executed
# Finally: Finally block always gets executed either exception is generated or not


while True:
    try:
        age = int(input('What is your age? '))
        10 / age
        raise ValueError('hey cut it out')
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you!')
    finally:
        print('ok, i am finally done')
    print('can you hear me?')
