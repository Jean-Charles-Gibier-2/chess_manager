from ct_models.player import Player

class Tournament:
    def __init__(self, name, address, city, country, date):
        self.name = name
        self.address = address
        self.city = city
        self.country = country
        self.date = date
        self.players = []

    def __str__(self):
        pass

    def serialize(self):
        return {
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "country": self.country,
            "date": self.date,
            "players": [player.ime for player in self.players]
        }

    @staticmethod
    def deserialize(json_value):
        return Tournament(**json_value)

    def add_player(self, player: Player):
        self.players.append(player)