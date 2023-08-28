# OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        self.name = name  # attributes
        self.age = age

    def run(self):
        return self

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Tom', 10)
print(player1.run())

# player3 = PlayerCharacter.adding_things(2, 3)
# print(player3.age)
