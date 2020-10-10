def check_matrix_to_end_game(matrix) -> bool:
    if matrix[0][0] == matrix[0][1] and matrix[0][1] == matrix[0][2]:
        return True
    elif matrix[2][0] == matrix[2][1] and matrix[2][1] == matrix[2][2]:
        return True
    elif matrix[1][0] == matrix[1][1] and matrix[1][1] == matrix[1][2]:
        return True
    elif matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
        return True
    elif matrix[2][0] == matrix[1][1] and matrix[1][1] == matrix[2][0]:
        return True
    elif matrix[0][0] == matrix[1][0] and matrix[1][0] == matrix[2][0]:
        return True
    elif matrix[0][1] == matrix[1][1] and matrix[1][1] == matrix[2][1]:
        return True
    elif matrix[0][2] == matrix[1][2] and matrix[1][2] == matrix[2][2]:
        return True
    else:
        return False
