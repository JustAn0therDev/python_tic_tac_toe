from get_player_input import get_player_input
from player import Player
from match_ended import match_ended
from print_matrix import print_matrix

matrix = [['?', '?', '?'], ['?', '?', '?'], ['?', '?', '?']]

# player 1 -> player 1 should go first
# player 2 -> then player 2

print_matrix(matrix)
turn = Player.PLAYER_1
player_has_won = False

# handle invalid input exceptions -> done
# handle array out of bounds exceptions -> should be in the same validate_input function or something similar
try:
    while (not player_has_won):
        selected_indexes = get_player_input()

        if turn == Player.PLAYER_1:
            matrix[selected_indexes[0]][selected_indexes[1]] = 'x'
            turn = Player.PLAYER_2
        else:
            matrix[selected_indexes[0]][selected_indexes[1]] = 'o'
            turn = Player.PLAYER_1
        # player_has_won = check_matrix_to_end_game(matrix)
        print_matrix(matrix)
except:
    pass