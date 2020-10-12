import unittest
from testutils import map_absolute_path

map_absolute_path(num_of_directories_to_go_up=1)

from PlayerFactory import PlayerFactory


class PlayerFactoryTests(unittest.TestCase):

    def setUp(self):
        print(__name__)

    def testFactory(self):
        assert PlayerFactory.create_player('x', 'randomname') is not None
        assert PlayerFactory.create_player('0', 'anothername') is not None
        assert PlayerFactory.create_player('4', 'lookaname') is not None
        assert PlayerFactory.create_player('f', 'ohaname') is not None
        assert PlayerFactory.create_player('a', 'freshprince') is not None
