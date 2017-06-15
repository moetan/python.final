from random import randint

class Dice:
        def die(num):
            die = randint(1, num)
            return die

class Character(object):
    def __init__(self, name):
        self.name = name
        self.hp = randint(8,17)
        self.sp = randint(8,17)
    def __str__(self):
        rep = self.name
        return rep

class Player(Character):
    def __init__(self):
        super(Player, self).__init__(player_name)
        self.name = player_name
        self.hp = randint(8,17)
        self.sp = randint(8,17)

class Troll(Character):
    def __init__(self):
        super(Troll, self).__init__('Troll')
        self.hp = randint(8,17)
        self.sp = randint(8,17)

class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__('Goblin')
        self.hp = randint(8,17)
        self.sp = randint(8,17)

def random_Monster(num):
    if num == 1:
        return Troll()
    else:
        return Goblin()

def Attack():
    roll = Dice.die(6)
    if roll > 3:
        print('You hit the monster')
        print('You dealt', roll, 'damages')
        monster.hp -= roll
        print('the', monster.name, 'has', monster.hp, 'hp left')
    else:
        print('miss')

def Defence():
    roll = Dice.die(6)
    if roll < 3:
        print('Monster deals', roll, 'damage')
        player.hp -= roll
        print(player.name, 'has', player.hp, 'hp left.')
    else:
        print('The', monster.name, 'missed his mark.')

def Actions():
    roll = Dice.die(6)
    if roll != 4:
        print("press f to fight", '\n', "press p to pass")
        command = input()
        if command == "f":
            Attack()
        elif command == "p":
            pass
        else:
            print('not a valid input')
    if roll == 4:
        if player.sp >= 3:
            print("press f to fight",
                  '\n', "press p to pass", "press h to heal")
            command = input()
            if command == "f":
                Attack()
            elif command == "p":
                pass
            elif command == "h":
                player.hp += 2
                player.sp -= 3
                print(Player.name, 'has', Player.hp, 'hp left, and',
                      '\n', Player.sp, 'sp left.')
            else:
                print('not a valid input')
        else:
            print("press f to fight", '\n', "press p to pass")
            command = input()
            if command == "f":
                Attack()
            if command == "p":
                pass
            else:
                print('not a valid input')

#Intro to game
print("Welcome to my game. What is your name?")
player_name = input()
print("Hello,", player_name, "let's go on an adventure!")

while True:
    die = Dice
    monster = random_Monster(Dice.die)
    player = Player()
    if monster.hp <= 0:
        print('The', monster.name, 'is dead!')
        hero.sp += monster.sp
        Monster = random_Monster
    if player.hp <= 0:
        print(Player.name, "died!!! duhduhduh~~")
        print("press any key to end game")
        end = input()
        if end == a:
            sys.exit()
        else:
            sys.exit()   
    print("\n")
    print("you walk along a path")
    print("as you are walking, you encounter a", monster)
    Actions()
    print("It is the monster's turn")
    Defence()
    

        


