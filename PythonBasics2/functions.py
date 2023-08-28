# parameters
# default parameters
def say_hello(name='Darth Vader', emoji='😀'):
    print(f'hellllooooo {name} {emoji}')


# positional arguments
say_hello('🥰', 'Andrei')
say_hello('Dan', '🥰')
say_hello('Emily', '🥰')

# keyword arguments
say_hello(name='Bibi', emoji='🥰')
say_hello()
say_hello("Timmy")
