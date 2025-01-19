import sys
from types import FunctionType
from ct_controllers.actions import (
    list_tournaments,
    register_tournament,
    suppress_tournament,
    modify_tournament,
    register_player,
    modify_player,
    suppress_player,
    list_players, add_player_in_tournament
)
from ct_models.tournament import Tournament


class Menu:
    def __init__(self, label="<empty>", label_choices=None, action_choices=None, controller=None):
        self.label = label
        self.label_choices = label_choices or []
        self.action_choices = action_choices or []
        if len(label_choices) != len(action_choices):
            raise "menu incohérent"

    def print_menu(self):
        print(f"-------[{self.label}]-------")
        for number_choice, label_choice in enumerate(self.label_choices, start=1):
            print(f"{number_choice} - {label_choice}")
        print(f"0 - Sortie du programme")
        print(f"9 - Menu principal")
        print(f"-------[Choisissez le N° du menu]-------")

    def start(self):
        response = None
        while response is None:
            self.print_menu()
            response = self.get_response()
            if response == 0:
                sys.exit(0)
            elif response != 9:
                action = self.action_choices[response-1]
                if isinstance(action, Menu):
                    response = action.start()
                elif isinstance(action, FunctionType):
                    response = action(self)
            if response == 9 and self.label == "Main menu":
                response = None
        return response

    def get_response(self):
        nb_choices = len(self.label_choices)
        try:
            response = int(sys.stdin.readline().strip())
            if int(response) in range(0, nb_choices +1) or response == 9:
                return response
        except Exception:
            pass
        print(f"Erreur, choisissez un option de 0 à {nb_choices} ou 9 pour sortir.")


class Controller:

    def __init__(self):
        self.menu = Menu(
            "Main menu",
            [
                "Gestion des tournois",
                "Gestions des joueurs"
            ],
            [
                Menu(
                    "Gestion des tournois",
                    [
                        "Enregistrer un tournoi",
                        "Modifier un tournoi",
                        "Supprimer un tournoi",
                        "Lister les tournois ",
                        "ajouter un joueur a un tournois"
                    ],
                    [
                        register_tournament,
                        modify_tournament,
                        suppress_tournament,
                        list_tournaments,
                        add_player_in_tournament
                    ]
                ),
                Menu(
                    "Gestion des Joueurs",
                    [
                        "Enregistrer un joueur",
                        "Modifier un joueur",
                        "Supprimer un joueur",
                        "Lister les joueurs",
                    ],
                    [
                        register_player,
                        modify_player,
                        suppress_player,
                        list_players
                    ]
                )
            ],
            self
        )

    def start(self):
        # print("Controller start")
        self.menu.start()
