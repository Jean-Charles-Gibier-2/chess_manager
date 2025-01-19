import  sys

from ct_models.player import Player
from ct_models.tournament import Tournament
from data_manager import DataManager


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
            date=date
        )
        return tournament

    def display(self):
        pass

    def add_player(self, tournament: Tournament, player: Player):

        if not tournament:
            print(f"Entrez le nom du tournois:")
            tournament_name = sys.stdin.readline().strip()
            tournament_json = DataManager.json_values.get("tournaments", {}).get(tournament_name)
            tournament = Tournament(**tournament_json)

        if not player:
            print(f"Entrez le n° ime du jouer:")
            player_ime = sys.stdin.readline().strip()
            player_json = DataManager.json_values.get("players", {}).get(player_ime)
            player = Tournament(**player_json)




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

    def get(self):
        pass