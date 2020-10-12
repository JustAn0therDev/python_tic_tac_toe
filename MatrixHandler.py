from Player import Player
from constants import EMPTY_SPOT_VALUE


class MatrixHandler:

    @staticmethod
    def match_ended(matrix, current_player_symbol) -> bool:
        if current_player_symbol == matrix[0][0] and matrix[0][0] == matrix[0][1] and matrix[0][1] == matrix[0][2]:
            return True
        elif current_player_symbol == matrix[2][0] and matrix[2][0] == matrix[2][1] and matrix[2][1] == matrix[2][2]:
            return True
        elif current_player_symbol == matrix[1][0] and matrix[1][0] == matrix[1][1] and matrix[1][1] == matrix[1][2]:
            return True
        elif current_player_symbol == matrix[0][0] and matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
            return True
        elif current_player_symbol == matrix[2][0] and matrix[2][0] == matrix[1][1] and matrix[1][1] == matrix[0][2]:
            return True
        elif current_player_symbol == matrix[0][0] and matrix[0][0] == matrix[1][0] and matrix[1][0] == matrix[2][0]:
            return True
        elif current_player_symbol == matrix[0][0] and matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
            return True
        elif current_player_symbol == matrix[0][2] and matrix[0][2] == matrix[1][2] and matrix[1][2] == matrix[2][2]:
            return True
        else:
            return False
    
    @staticmethod
    def no_spots_left(matrix):
        for _ in matrix:
            for column in matrix:
                if len(list(filter(lambda cell: cell == EMPTY_SPOT_VALUE, column))) > 0:
                    return False
        
        return True
