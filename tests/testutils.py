import sys


def map_absolute_path(num_of_directories_to_go_up):
    sys.path.append('../' * num_of_directories_to_go_up)