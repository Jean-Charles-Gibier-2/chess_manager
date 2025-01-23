import sys
from json import dumps
from ct_models.player import Player
from ct_models.tournament import Tournament
from ct_views.tournament_view import TournamentView
from data_manager import DataManager
from tools import readline

class PlayerView:

    def create(self):
        ime = readline("ime :")
        name = readline("name :")
        surname = readline("surname :")
        birth = readline("surname :")
        rank = readline("rank :")
        player = Player(
            ime=ime,
            name=name,
            surname=surname,
            birth=birth,
            rank=rank
        )
        return player

    def display(self, player: Player):
        print(dumps(player.serialize()))

    def save(self, player: Player):
        serialized_value = player.serialize()
        DataManager.read()
        players = DataManager.json_values.get("players", {})

        if player.ime in players.keys():
            response = readline(
                f"Le player {player.ime} est déjà enregistré. "
                "tapez 'R' pour remplacer ou 'A' lettre pour abandonner:"
            )
            if response.upper().startswith('A'):
                return

        players[serialized_value["name"]] = serialized_value
        DataManager.json_values["players"] = players
        DataManager.write()

    def get(self, ime):
        return DataManager.object_values.get("players", {}).get(ime)

    def add_in_tournament(self):
        player_ime = readline("Selectionnez l'ime du joueur :")
        player = self.get(player_ime)
        tournoi_name = readline("Selectionnez le nom du tournois :")
        tournoi = TournamentView.get(tournoi_name)
        tournoi.add_player(player)
