NULL = 8

# 0 1 2
# 3 4 5
# 6 7 8


PATHS = {
    0: (1, 3),
    2: (1, 5),
    6: (3, 7),
    8: (5, 7),

    1: (0, 2, 4),
    3: (0, 4, 6),
    5: (2, 4, 8),
    7: (4, 6, 8),

    4: (1, 3, 5, 7),
}


SOLVED_GAME = (
    0, 1, 2,
    3, 4, 5,
    6, 7, NULL,
)
