# player = Player(name, old, score)

class Player:
    # player = Player(name, old, score)
    # name - имя игрока (строка); old - возраст игрока (целое число);
    # score - набранные очки в игре (целое число)
    def __init__(self, name, old, score):
        self.name = name
        self.old = int(old)
        self.score = int(score)
    
    def __repr__(self) -> str:
        return f"Player={self.name}: {self.score};"
    
    def __bool__(self):
        return True if self.score > 0 else False


lst_in = ['Балакирев; 34; 2048',
'Mediel; 27; 0',
'Влад; 18; 9012',
'Nina P; 33; 0']

players = []
for el in lst_in:
    x = Player(*el.split(';'))
    players.append(x)

# print(players)
players_filtered = list(filter(bool, players))
# print(players_filtered)


        