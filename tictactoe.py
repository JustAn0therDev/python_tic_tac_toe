from Player import Player
from InputHandler import InputHandler
from constants import EMPTY_SPOT_VALUE
from PlayerFactory import PlayerFactory
from MatrixHandler import MatrixHandler
from TerminalHandler import TerminalHandler

matrix = [list(EMPTY_SPOT_VALUE * 3), list(EMPTY_SPOT_VALUE * 3), list(EMPTY_SPOT_VALUE * 3)]

terminal_handler = TerminalHandler()

winner = None
player_one = PlayerFactory.create_player('x', input("Please enter the first player's nickname: "))
player_two = PlayerFactory.create_player('o', input("Now the second player's nickname: "))
current_player = player_one

try:
    while (not winner):
        terminal_handler.print_current_turn(current_player)
        terminal_handler.print_matrix(matrix)
        selected_indexes = InputHandler.get_player_input(matrix)

        if current_player.symbol == 'x':
            matrix[selected_indexes[0]][selected_indexes[1]] = 'x'
        else:
            matrix[selected_indexes[0]][selected_indexes[1]] = 'o'

        match_ended = MatrixHandler.match_ended(matrix, current_player.symbol)

        if (match_ended):
            winner = current_player
        elif not match_ended and MatrixHandler.no_spots_left(matrix):
            break
        else:
            if current_player.symbol == 'x':
                current_player = player_two
            else:
                current_player = player_one
except Exception as error_message:
    print('Something went wrong! Error: {}'.format(str(error_message)))

terminal_handler.print_end_game(winner, matrix)