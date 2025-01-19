from ct_models.player import Player

class Match:
    def __init__(self, player1: Player, player2: Player, score):
        self.player1 = player1
        self.player2 = player2
        self.score = score
        self.players = []
