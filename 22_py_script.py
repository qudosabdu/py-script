# Method Overide

class Cricket:
    def play(self, game):
        print(f"I am playing {game}")

class Football(Cricket):
    pass
    def play(self, game):
        print(f"I am playing {game}.....")  

p1= Cricket()
p2 = Football()

p1.play("Cricket")
p2.play("Football")