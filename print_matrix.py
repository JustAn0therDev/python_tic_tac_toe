def print_matrix(matrix):
    print('  1|2|3')
    for i, list in enumerate(matrix):
        print("{}|{}".format(i + 1 ,'|'.join(list)))