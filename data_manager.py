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
        json_players = DataManager.json_values.get("players", {})
        for ime, player in enumerate(json_players):
            DataManager.object_values['players'][ime] = Player.serialize(**player)

        json_tournaments = DataManager.json_values.get("tournaments")
        for name, tournament in enumerate(json_tournaments):
            DataManager.object_values['tournaments'] = Tournament.serialize(**tournament)
            for player_ime in tournament['players']:
                player = DataManager.object_values['players'][player_ime]
                DataManager.object_values['tournaments'].players.append(player)


    @staticmethod
    def objects_to_json():
        object_players = DataManager.object_values.get("players", {})
        for ime, player in enumerate(object_players):
            DataManager.json_values['players'][ime] = Player.deserialize(player)

        objects_tournaments = DataManager.object_values.get("tournaments")
        for name, tournament in enumerate(objects_tournaments):
            DataManager.json_values['tournaments'] = Tournament.deserialize(**tournament)
            # for player_ime in tournament['players']:
            #     player = DataManager.json_values['players'][player_ime]
            #     DataManager.object_values['tournaments']
