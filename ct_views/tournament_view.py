import sys
from json import dumps
from ct_models.player import Player
from ct_models.tournament import Tournament
from data_manager import DataManager
from tools import readline


class TournamentView:

    def create(self):
        def readline():
            return sys.stdin.readline().strip()
        print("name :")
        name = readline()
        print("address :")
        address = readline()
        print("city :")
        city = readline()
        print("country :")
        country = readline()
        print("date :")
        date = readline()
        tournament = Tournament(
            name=name,
            address=address,
            city=city,
            country=country,
            date=date,
            players=[]
        )
        return tournament

    def display(self, tournament: Tournament):
        print(dumps(tournament.serialize()))


    def list(self):
        for tournament in DataManager.object_values.get("tournaments", {}).values():
            self.display(tournament)

    def add_player(self, tournament: Tournament = None, player: Player = None):

        if not tournament:
            tournament_name = readline("Entrez le nom du tournois :")
            tournament = DataManager.object_values.get("tournaments", {}).get(tournament_name)

        if not player:
            player_ime = readline(f"Entrez le n° ime du joueur:")
            player = DataManager.object_values.get("players", {}).get(player_ime)

        if player and tournament:
            tournament.add_player(player)


    def save(self, tournament: Tournament):
        serialized_value = tournament.serialize()
        DataManager.read()
        tournaments = DataManager.json_values.get("tournaments", {})

        if tournament.name in tournaments.keys():
            print(f"Le tournois {tournament.name} est déjà enregistré. tapez 'R' pour remplacer ou 'A' lettre pour abandonner:")
            response = sys.stdin.readline().strip()
            if response.upper().startswith('A'):
                return

        tournaments[serialized_value["name"]] = serialized_value
        DataManager.json_values["tournaments"] = tournaments
        DataManager.write()

    def get(self, name):
        return DataManager.object_values.get("tournaments", {}).get(name)
