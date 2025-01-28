import sys
from json import dumps
from ct_models.player import Player
from ct_models.tournament import Tournament
from ct_views.tournament_view import TournamentView
from data_manager import DataManager
from tools import readline


class PlayerView:

    def __init__(self):
        self.tournaments = DataManager.object_values.get("tournaments", {})
        self.players = DataManager.object_values.get("players", {})

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

    def list(self):
        for player in self.players.values():
            self.display(player)

    def save(self, player: Player):
        if player.ime in self.players.keys():
            response = readline(
                f"Le player {player.ime} est déjà enregistré. "
                "tapez 'R' pour remplacer ou 'A' lettre pour abandonner:"
            )
            if response.upper().startswith('A'):
                return

        self.players[player.ime] = player

    def get(self, ime):
        return self.players.get(ime)

    def add_in_tournament(self):
        player_ime = readline("Entrez le n° ime du joueur :")
        player = self.get(player_ime)
        if not player:
            print("Le nom du joueur n'existe pas")
            return None
        tournament_name = readline("Entrez le nom du tournois :")
        tournament = TournamentView.get(tournament_name)
        if not tournament:
            print("Le nom du tournois n'existe pas")
            return None

        tournament_name.add_player(player)
