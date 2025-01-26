import sys
from json import dumps
from ct_models.player import Player
from ct_models.tournament import Tournament
from data_manager import DataManager
from tools import readline
from tools import readline


class TournamentView:

    def create(self):
        name = readline("name :")
        address = readline("address :")
        city = readline("city :")
        country = readline("country :")
        date = readline("date :")
        tournament = Tournament(
            name=name,
            address=address,
            city=city,
            country=country,
            date=date,
            players=[]
        )
        return tournament

    def update(self, tournament: Tournament = None):
        if not tournament:
            tournament_name = readline("Entrez le nom du tournois :")
            tournaments = DataManager.object_values.get("tournaments", {})

            if tournament_name not in tournaments.keys():
                print(f"Le tournois {tournament_name} n'existe pas.")
                return
            tournament = tournaments[tournament_name]

        print(f"Valeurs du tournois:")
        self.display(tournament)
        print(f"Entrez les nouvelles valeurs du tournois '{tournament.name}':")
        address = readline("address :")
        city = readline("city :")
        country = readline("country :")
        date = readline("date :")
        tournament.address = address
        tournament.city = city
        tournament.country = country
        tournament.date = date
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
            if not tournament:
                print("Le nom du tournois n'existe pas")
                return None

        if not player:
            player_ime = readline(f"Entrez le n° ime du joueur:")
            player = DataManager.object_values.get("players", {}).get(player_ime)
            if not player:
                print("Le nom du joueur n'existe pas")
                return None

        if player and tournament:
            tournament.add_player(player)

    def sup_player(self, tournament: Tournament = None, player: Player = None):

        if not tournament:
            tournament_name = readline("Entrez le nom du tournois :")
            tournament = DataManager.object_values.get("tournaments", {}).get(tournament_name)
            if not tournament:
                print("Le nom du tournois n'existe pas")
                return None

        if not player:
            player_ime = readline(f"Entrez le n° ime du joueur:")
            player = DataManager.object_values.get("players", {}).get(player_ime)
            if not player:
                print("Le nom du joueur n'existe pas")
                return None

        if player and tournament:
            if tournament.sup_player(player):
                print(f"Le joueur {player.ime} n'est pas enregistré dans le tournois {tournament.name}")


    def save(self, tournament: Tournament):
        tournaments = DataManager.object_values.get("tournaments", {})

        if tournament.name in tournaments.keys() and tournaments[tournament.name] is not tournament:
            print(f"Le tournois {tournament.name} est déjà enregistré. tapez 'R' pour remplacer ou 'A' lettre pour abandonner:")
            response = sys.stdin.readline().strip()
            if response.upper().startswith('A'):
                return

        tournaments[tournament.name] = tournament

    def get(self, name):
        return DataManager.object_values.get("tournaments", {}).get(name)
