from itertools import permutations
from random import choice

from puzzle8.bfs import bfs
from puzzle8.constants import SOLVED_GAME, NULL as X
from puzzle8.utils import is_solvable


GAMES = tuple(permutations(range(9)))
SOLVABLE = [game for game in GAMES if is_solvable(game)]
NOT_SOLVABLE = [game for game in GAMES if not is_solvable(game)]


def test_bfs_with_solved_game():
    solution = bfs(SOLVED_GAME)
    assert solution == tuple()


def test_bfs_with_unsolvable_game():
    game = choice(NOT_SOLVABLE)
    solution = bfs(game)
    assert solution is None


def test_bfs_returns_True_for_all_solvable_games():
    for _ in range(3):
        game = choice(SOLVABLE)
        solution = bfs(game)
        assert solution is not None


def test_bfs_returns_solution():
    game = (0, 1, 2,
            3, 4, 5,
            X, 6, 7)
    solution = bfs(game)
    assert solution == (7, 8)
