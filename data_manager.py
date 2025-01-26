import json
import os

from ct_models.player import Player
from ct_models.tournament import Tournament


class DataManager:
    json_values = {}
    object_values = {}
    filename = 'c:\\tmp\\chess_manager.json'

    @staticmethod
    def write():
        # delete and rewrite
        if os.path.isfile(DataManager.filename):
            os.remove(DataManager.filename)
        # Write the JSON string to a file
        with open(DataManager.filename, 'w') as json_file:
            json.dump(DataManager.json_values, json_file, indent=4)


    @staticmethod
    def read():
        # Read a file to json
        if os.path.isfile(DataManager.filename):
            with open(DataManager.filename) as f:
                DataManager.json_values = json.load(f)
        else:
            DataManager.json_values = {}

    # matchs are missing
    @staticmethod
    def json_to_objects():
        DataManager.read()
        json_players = DataManager.json_values.get("players", {})
        DataManager.object_values["players"] = {}
        for ime, player in json_players.items():
            DataManager.object_values["players"].update({ime: Player.deserialize(player)})

        json_tournaments = DataManager.json_values.get("tournaments", {})
        DataManager.object_values["tournaments"] = {}
        for name, tournament in json_tournaments.items():
            DataManager.object_values['tournaments'].update({name: Tournament.deserialize(tournament)})
            DataManager.object_values['tournaments'][name].players = []
            for player_ime in json_tournaments[name].get('players', []):
                try:
                    player = DataManager.object_values['players'][player_ime]
                    DataManager.object_values['tournaments'][name].add_player(player)
                except KeyError:
                    print(f"Could not find player {player_ime}")
        return True


    @staticmethod
    def objects_to_json():
        object_players = DataManager.object_values.get("players", {})
        DataManager.json_values['players'] = {}
        for ime, player in object_players.items():
            DataManager.json_values['players'][ime] = Player.serialize(player)

        objects_tournaments = DataManager.object_values.get("tournaments")
        DataManager.json_values['tournaments'] = {}
        for name, tournament in objects_tournaments.items():
            DataManager.json_values['tournaments'][name] = Tournament.serialize(tournament)
            DataManager.write()
