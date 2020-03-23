class Character():

    def __init__(self, power):
        self._power = power


class Archer(Character):
    def __init__(self, power, arrows_number):
        self._arrows_number = arrows_number
        super().__init__(power)

    def show_powers(self):
        print(f'My power is {self._power} and i have: {self._arrows_number} arrows.')


class Wizard(Character):
    def __init__(self, power, spells):
        self._spells = spells
        super().__init__(power)

    def show_powers(self):
        print(f'My power is {self._power} and i know: {self._spells} spells.')


class Game:
    @staticmethod
    def player_powers(char):
        char.show_powers()


wizard = Wizard('magic', ['Expelliarmus', 'Sectumsempra', 'Vingardium Leviosa'])
archer = Archer('shooting', 17)

wizard.show_powers()
archer.show_powers()

Game.player_powers(wizard)
Game.player_powers(archer)

print(isinstance(wizard, Wizard))
print(isinstance(wizard, Character))
print(isinstance(wizard, Archer))  # Works just fine
