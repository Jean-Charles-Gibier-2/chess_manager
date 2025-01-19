import  sys
from ct_models.player import Player
from ct_models.tournament import Tournament
from data_manager import DataManager


class PlayerView:

    def create(self):
        def readline():
            return sys.stdin.readline().strip()
        print("ime :")
        ime = readline()
        print("name :")
        name = readline()
        print("surname :")
        surname = readline()
        print("birth :")
        birth = readline()
        print("rank :")
        rank = readline()
        player = Player(
            ime=ime,
            name=name,
            surname=surname,
            birth=birth,
            rank=rank
        )
        return player

    def display(self):
        pass

    def save(self, player: Player):
        serialized_value = player.serialize()
        DataManager.read()
        players = DataManager.json_values.get("players", {})

        if player.ime in players.keys():
            print(f"Le player {player.ime} est déjà enregistré. tapez 'R' pour remplacer ou 'A' lettre pour abandonner:")
            response = sys.stdin.readline().strip()
            if response.upper().startswith('A'):
                return

        players[serialized_value["name"]] = serialized_value
        DataManager.json_values["players"] = players
        DataManager.write()

    def get(self, ime):
        json_player = DataManager.json_values.get("players", {}).get(ime)
        if json_player:
            return Player(**json_player)

    def add_in_tournament(self, tournament: Tournament):
        pass