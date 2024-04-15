# Polymorpism

class Cricket:
    def play(self, game):
        print(f"I am playing {game}")

class Football(Cricket):
    pass
    def play(self, game):
        print(f"I am playing {game}.....")  



p2: Cricket = Football()
p2.play("Football")