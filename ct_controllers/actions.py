from ct_views.player_view import PlayerView
from ct_views.tournament_view import TournamentView


# create
def register_tournament(controller):
    tournament_view = TournamentView()
    tournament = tournament_view.create()
    tournament_view.save(tournament)


def modify_tournament(controller):
    tournament_view = TournamentView()
    tournament = tournament_view.update()
    tournament_view.save(tournament)


def suppress_tournament(controller):
    print("suppress_tournament")


def list_tournaments(controller):
    tournament_view = TournamentView()
    tournament_view.list()


def add_player_in_tournament(controller, tournament=None, player=None):
    tournament_view = TournamentView()
    return tournament_view.add_player(tournament, player)


def sup_player_from_tournament(controller, tournament=None, player=None):
    tournament_view = TournamentView()
    return tournament_view.sup_player(tournament, player)

def register_player(controller):
    player_view = PlayerView()
    player = player_view.create()
    player_view.save(player)


def modify_player(controller):
    print("modify_player")


def suppress_player(controller):
    print("suppress_player")


def list_players(controller):
    player_view = PlayerView()
    player_view.list()
