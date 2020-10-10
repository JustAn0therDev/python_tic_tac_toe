from player import Player
from check_matrix_to_end_game import check_matrix_to_end_game
from print_matrix import print_matrix

matrix = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]

# player 1 -> player 1 should go first
# player 2 -> then player 2

print_matrix(matrix)
turn = Player.PLAYER_1
player_has_won = False

try:
    while (not player_has_won):
        selected_indexes = list(map(lambda x: int(x), input('Please select row and column, separated by commas (,): ').split(',')))
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