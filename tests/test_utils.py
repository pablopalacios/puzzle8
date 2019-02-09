from puzzle8.constants import NULL as X
from puzzle8.utils import (
    get_total_permutations,
    is_solvable,
    is_solved,
    get_available_paths,
    swap_tiles,
)

# Cases from:
# http://www.cs.princeton.edu/courses/archive/fall12/cos226/assignments/8puzzle.html


def test_is_solvable_returns_True_if_solvable():
    cases = (
        (X, 0, 2, 3, 1, 4, 6, 7, 5),
        (0, X, 2, 3, 1, 4, 6, 7, 5),
        (0, 1, 2, 3, X, 4, 6, 7, 5),
        (0, 1, 2, 3, 4, X, 6, 7, 5),
        (0, 1, 2, 3, 4, 5, 6, 7, X),
    )
    for case in cases:
        assert is_solvable(case)


def test_is_solvable_returns_False_if_unsolvable():
    cases = (
        (0, 1, 2, 3, 4, 7, 6, 5, X),
        (0, 1, 2, 3, 4, 5, 7, 6, X),
        (0, 1, 2, 3, 4, 5, 7, X, 6),
        (0, 1, 2, 3, X, 5, 7, 4, 6),
        (0, 1, 2, X, 3, 5, 7, 4, 6),
        (0, 1, 2, 3, 5, 6, 7, 4, X),
    )
    for case in cases:
        assert not is_solvable(case)


def test_get_total_permutations():
    cases = (
        ((X, 0, 2, 3, 1, 4, 6, 7, 5), 4),
        ((0, X, 2, 3, 1, 4, 6, 7, 5), 4),
        ((0, 1, 2, 3, X, 4, 6, 7, 5), 2),
        ((0, 1, 2, 3, 4, X, 6, 7, 5), 2),
        ((0, 1, 2, 3, 4, 5, 6, 7, X), 0),
        ((0, 1, 2, 3, 4, 5, 7, 6, X), 1),
        ((0, 1, 2, 3, 4, 5, 7, X, 6), 1),
        ((0, 1, 2, 3, X, 5, 7, 4, 6), 3),
        ((0, 1, 2, X, 3, 5, 7, 4, 6), 3),
        ((0, 1, 2, 3, 5, 6, 7, 4, X), 3),
    )
    for case, expected in cases:
        assert get_total_permutations(case) == expected


def test_is_solved_returns_True_if_solved():
    game = (0, 1, 2, 3, 4, 5, 6, 7, X)
    assert is_solved(game)


def test_can_get_available_paths():
    game = (0, 1, 2,
            3, 4, 5,
            6, 7, X)
    paths = get_available_paths(game)
    assert paths == (5, 7)


def test_can_swap_tiles():
    game = (0, 1, 2,
            3, 4, 5,
            6, 7, X)
    new_game = swap_tiles(game, 5)
    expected = (0, 1, 2,
                3, 4, X,
                6, 7, 5)
    assert new_game == expected


def test_cannot_swap_tiles_that_are_not_swappable():
    game = (0, 1, 2,
            3, 4, 5,
            6, 7, X)
    new_game = swap_tiles(game, 4)
    assert new_game == game
