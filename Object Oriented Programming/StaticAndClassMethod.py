class Player:
    class_attribute = 'unchangeable'

    def __init__(self, name):
        self._name = name  # _name means, this variable should be read as private, but it doesn't make it so

    @classmethod
    def do_something(cls, name):
        return cls(name)

    @staticmethod
    def do_something_static(name):
        print(f'my name is {name}')

    def do_something_regular(self):
        print(f'my name is {self._name}')


player1 = Player.do_something('Bart')
player2 = Player('Cart')
Player.do_something_static('No Name')
player2.do_something_regular()
