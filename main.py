import tkinter as tk
import random

r_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
c_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

class Cell:
    def __init__(self, row: str, col: str):
        self.value = 0
        self.revealed = False
        self.row = row
        self.col = col

    # possibly redundant
    def set_cell_value(self, val):
        self.value = val


class Group:
    def __init__(self, cells):
        self.cells = cells


class Row(Group):
    def __init__(self, cells, row: str):
        super().__init__(cells)
        self.row = row


class Column(Group):
    def __init__(self, cells, col: str):
        super().__init__(cells)
        self.col = col


class Block(Group):
    def __init__(self, cells, rows: list, cols: list):
        super().__init__(cells)
        self.rows = rows
        self.cols = cols


class Board:
    def __init__(self):
        self.game = self.initialise()
        self.rows = self.extract_rows(self.game)
        self.cols = self.extract_cols(self.game)

    # Returns a 9x9 2D array of 0-valued Cell objects with row/col categorical labels
    def initialise(self):
        game_board = []

        for row in r_labels:
            result = []
            for col in c_labels:
                result.append(Cell(row, col))
            game_board.append(result)

        return game_board

    def update(self):
        self.rows = self.extract_rows(self.game)
        self.cols = self.extract_cols(self.game)

    def extract_rows(self, game_board):
        rows = []
        for i, row in enumerate(game_board):
            rows.append(Row(row, r_labels[i]))

        return rows

    # for each col, extract the index from each row
    def extract_cols(self, game_board):
        cols = []
        for i in range(len(c_labels)):
            column = [row[i] for row in game_board]
            cols.append(Column(column, c_labels[i]))

        return cols

    def extract_blocks(self, game_board):
        pass

    # def pick_val(self, col_idx, values):
    #     for val in values:
    #         for



    # randomly shuffle list of values, pop value if valid
    # TODO: validity checks
    def populate(self):
        for row in self.game:
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(numbers)

            i = 0
            for cell in row:
                cell.value = numbers[i]
                i += 1



def main():

    b = Board()

    b.populate()
    b.update()

    for row in b.game:
        for cell in row:
            print(cell.value, end=' ')
        print()

    print("\nfirst row:")
    for cell in b.rows[0].cells:
        print(cell.value, end=' ')
    print()
    print("\nfirst col:")
    for cell in b.cols[0].cells:
        print(cell.value, end=' ')
    # root = tk.Tk()
    # root.title("SUDOKU!")
    # root.mainloop()


if __name__ == "__main__":
    main()

