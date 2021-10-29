import unittest
from minimax import search_best_move
from x_o import GameSign, GameGrid
from x_o_grid import Move


class MinimaxTestCase(unittest.TestCase):
    def test_win_one_move(self):
        win_one_position: list[GameSign] = [GameSign.X, GameSign.O, GameSign.X,
                                            GameSign.X, GameSign.N, GameSign.O,
                                            GameSign.N, GameSign.N, GameSign.O]
        test_grid1: GameGrid = GameGrid(win_one_position, GameSign.X)
        answer1: Move = search_best_move(test_grid1)
        self.assertEqual(answer1, 6)

    def test_prevent_win(self):
        prevent_position: list[GameSign] = [GameSign.X, GameSign.N, GameSign.N,
                                            GameSign.N, GameSign.N, GameSign.O,
                                            GameSign.N, GameSign.X, GameSign.O]
        test_grid2: GameGrid = GameGrid(prevent_position, GameSign.X)
        answer2: Move = search_best_move(test_grid2)
        self.assertEqual(answer2, 2)

    def test_win_two_moves(self):
        win_two_position: list[GameSign] = [GameSign.X, GameSign.N, GameSign.N,
                                            GameSign.N, GameSign.N, GameSign.O,
                                            GameSign.O, GameSign.X, GameSign.N]
        test_grid3: GameGrid = GameGrid(win_two_position, GameSign.X)
        answer3: Move = search_best_move(test_grid3)
        self.assertEqual(answer3, 1)


if __name__ == '__main__':
    unittest.main()
