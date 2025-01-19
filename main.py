from ct_controllers.controller import Controller


def launch_chess_tournament_manager(name):
    print(f'Hi, {name}')
    controller = Controller()
    controller.start()


if __name__ == '__main__':
    launch_chess_tournament_manager('user')

