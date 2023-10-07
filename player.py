class Player:
    def __init__(self, name, hp, attack_damage):
        self.name = name
        self.hp = hp
        self.attack_damage = attack_damage

    def print_info(self):
        print (self.name)
        print (self.hp)
        print (self.attack_damage)


joe = Player("Joe", 100, 13)
jane = Player("Jane", 50, 25)

print print_info(joe)