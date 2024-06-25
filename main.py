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
    def __init__(self, cells):
        super().__init__(cells)
        # self.rows = rows
        # self.cols = cols


class Board:
    def __init__(self):
        self.game = self.initialise()
        self.rows = self.extract_rows(self.game)
        self.cols = self.extract_cols(self.game)
        self.blocks = self.extract_blocks(self.game)

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
        blocks = []
        for block_row in range(0, 9, 3):
            for block_col in range(0, 9, 3):
                block_cells = []
                for i in range(3):
                    for j in range(3):
                        block_cells.append(game_board[block_row + i][block_col + j])
                blocks.append(Block(block_cells))
        return blocks

    def val_in_row(self, row_idx, value):
        for cell in self.rows[row_idx].cells:
            if cell.value == value:
                return True
        return False

    def val_in_col(self, col_idx, value):
        for cell in self.cols[col_idx].cells:
            if cell.value == value:
                return True
        return False

    # def pick_val(self, row_idx, col_idx, values):
    #     for val in values:
    #         if not self.val_in_col(col_idx, val) and not self.val_in_row(row_idx, val):
    #             values.remove(val)
    #             return val
    #     return 0

    def pick_val(self, col_idx, values):
        for val in values:
            if not self.val_in_col(col_idx, val):
                values.remove(val)
                return val
        return 0

    # randomly shuffle list of values, pop value if valid
    # TODO: validity checks
    def populate(self):

        for row in range(len(self.game)):
            numbers = [1,2,3,4,5,6,7,8,9]
            random.shuffle(numbers)
            for col in range(len(self.game[row])):
                cell = self.game[row][col]
                if cell.value == 0:
                    # cell.value = self.pick_val(row, col, numbers)
                    cell.value = self.pick_val(col, numbers)

def main():

    b = Board()

    b.populate()
    b.update()

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

