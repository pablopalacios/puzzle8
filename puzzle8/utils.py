from random import shuffle

from .constants import PATHS, NULL, SOLVED_GAME


def make_board():
    game = list(range(9))
    while is_solved(game) or not is_solvable(game):
        shuffle(game)
    return tuple(game)


def swap_tiles(game, tile):
    null_index = game.index(NULL)
    if null_index not in PATHS[tile]:
        return game
    lst = list(game)
    lst[null_index] = game[tile]
    lst[tile] = NULL
    return tuple(lst)


def is_solved(game):
    for i, j in zip(game, SOLVED_GAME):
        if i != j:
            return False
    return True


def is_solvable(board):
    permutations = get_total_permutations(board)
    return not (permutations % 2)


def get_total_permutations(lst):
    permutations = 0
    lst = [elm for elm in lst if elm != NULL]
    for index, elm in enumerate(lst[:-1]):
        for celm in lst[index:]:
            if elm > celm:
                permutations += 1
    return permutations


def get_available_paths(game):
    null_index = game.index(NULL)
    return PATHS[null_index]
