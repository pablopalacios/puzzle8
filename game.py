from collections import deque
from time import sleep
from tkinter import *
from tkinter.messagebox import showinfo

from puzzle8.constants import NULL
from puzzle8.bfs import bfs
from puzzle8.utils import make_board, swap_tiles, is_solved


ALL = N + S + E + W


class App(Frame):

    def __init__(self):
        super().__init__(master=Tk())
        self.state = make_board()
        self._tiles = []
        self._draw_tiles()
        self._draw_menu()
        self.mainloop()

    def _draw_tiles(self):
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        for i in range(3):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)
        self.grid(sticky=ALL)
        for index, value in enumerate(self.state):
            self._tiles.append(Tile(index, value, self._on_click, self))

    def _draw_menu(self):
        menu = Menu(self)
        game_menu = Menu(menu)
        menu.add_cascade(label='Game', menu=game_menu)
        game_menu.add_command(label='New game', command=self._new_game)
        game_menu.add_command(label='Solve with BFS', command=self._solve_with_bfs)
        game_menu.add_command(label='Exit', command=self.quit)
        self.master.config(menu=menu)

    def _new_game(self):
        self.state = make_board()
        self._update()

    def _update(self):
        for value, tile in zip(self.state, self._tiles):
            tile.update(value)

    def _solve_with_bfs(self):
        solution = bfs(self.state)
        self.after(0, self._swap_tiles_with_delay, deque(solution))

    def _swap_tiles_with_delay(self, solution):
        if not solution:
            return
        self._swap_tiles(self._tiles[solution.popleft()])
        self.after(500, self._swap_tiles_with_delay, solution)

    def _swap_tiles(self, tile):
        self.state = swap_tiles(self.state, tile.index)
        self._update()

    def _on_click(self, tile):
        self._swap_tiles(tile)
        if is_solved(self.state):
            showinfo('Game Over', 'Well done!')
            self._new_game()


class Tile(Button):

    VALUE_TO_STR = {
        0: '1',
        1: '2',
        2: '3',
        3: '4',
        4: '5',
        5: '6',
        6: '7',
        7: '8',
        8: '',
    }

    def __init__(self, index, value, on_click, master):
        super().__init__(master=master)
        self.index = index
        row, column = divmod(self.index, 3)
        self.grid(row=row, column=column, sticky=ALL)
        self.config(
            activeforeground='#EEEEEE',
            borderwidth=0,
            command=lambda: on_click(self),
            fg='#EEEEEE',
            font='Sans',
            highlightbackground='#1B2021',
            highlightthickness=1,
        )
        self.update(value)

    def update(self, value):
        self.config(
            activebackground='#242424' if value == NULL else '#4A86CF',
            bg='#242424' if value == NULL else '#3A4040',
            text=self.VALUE_TO_STR[value],
        )


if __name__ == '__main__':
    App()
