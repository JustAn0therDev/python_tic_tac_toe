import unittest
from testutils import map_absolute_path

map_absolute_path(num_of_directories_to_go_up=1)

from utils import Utils
from constants import EMPTY_SPOT_VALUE
from InputValidator import InputValidator

# For some reason the Python unittest module keeps putting a "." in front of
# literal int values inside the list when some method is called for testing.
# So a parsing of a literal value list is made before calling it, just to make sure
# the argument values are correct.
class Tests(unittest.TestCase):

    def testIndexes(self):
        assert InputValidator.input_indexes_are_valid(Utils.parse_testing_int_list([2,2])) == True
        assert InputValidator.input_indexes_are_valid(Utils.parse_testing_int_list([3,4])) == False
        assert InputValidator.input_indexes_are_valid(Utils.parse_testing_int_list([1,3])) == False
        assert InputValidator.input_indexes_are_valid(Utils.parse_testing_int_list([5,3])) == False
        assert InputValidator.input_indexes_are_valid(Utils.parse_testing_int_list([0,0])) == True

    def testMatrixSpotIsValid(self):
        user_input = Utils.parse_testing_int_list([1,1])

        matrix = [list(EMPTY_SPOT_VALUE * 3), ['?', 'x', '?'], list(EMPTY_SPOT_VALUE * 3)]
        assert InputValidator.matrix_index_is_not_taken(user_input, matrix) is False

        user_input = Utils.parse_testing_int_list([0,0])
        assert InputValidator.matrix_index_is_not_taken(user_input, matrix) is True

        user_input = Utils.parse_testing_int_list([2,1])
        assert InputValidator.matrix_index_is_not_taken(user_input, matrix) is True