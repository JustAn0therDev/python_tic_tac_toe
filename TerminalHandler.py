class TerminalHandler:

    def __init__(self):
        print('Welcome to TicTacToe!')

    def print_current_turn(self, player):
        print('CURRENT TURN: {}'.format(player.nickname))

    def print_matrix(self, matrix) -> None:
        print('  1|2|3')
        for i, list in enumerate(matrix):
            print("{}|{}".format(i + 1 ,'|'.join(list)))
    
    def print_end_game(self, winner, matrix):
        self.print_matrix(matrix)
        if winner:
            print("And this game's winner is: {}".format(winner.nickname))
        else:
            print("It's a draw!")