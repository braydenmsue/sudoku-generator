import tkinter as tk

r_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
c_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

class Cell:
    def __init__(self, row: str, col: str):
        self.value = 0
        self.revealed = False
        self.row = row
        self.col = col

    def set_cell_value(self, val):
        self.value = val


class Group:
    def __init__(self, cells):
        self.cells = cells


class Row(Group):
    def __init__(self, cells, row: str):
        super.__init__(cells)
        self.row = row


class Column(Group):
    def __init__(self, cells, col: str):
        super.__init__(cells)
        self.col = col


class Block(Group):
    def __init__(self, cells, rows: list, cols: list):
        super.__init__(cells)
        self.rows = rows
        self.cols = cols


class Board:
    def __init__(self):
        self.game = self.initialise()

    # Returns a 9x9 2D array of 0-valued Cell objects with row/col categorical labels
    def initialise(self):
        game_board = []

        for row in r_labels:
            result = []
            for col in c_labels:
                result.append(Cell(row, col))
            game_board.append(result)

        return game_board

    def extract_rows(self, game_board):
        rows = []
        for i, row in enumerate(game_board):
            rows.append(Row(row, r_labels[i]))

        return rows

    # for each col, extract the index from each row
    def extract_cols(self, game_board):
        cols = []
        for i in range(c_labels):
            column = [row[i] for row in game_board]
            cols.append(Row(column, c_labels[i]))

        return cols

    def extract_blocks(self, game_board):
        pass

# def populate(game_board):



def main():

    b = Board()
    game = b.initialise()

    for row in game:
        for cell in row:
            print(cell.value, end=' ')
        print()
    # root = tk.Tk()
    # root.title("SUDOKU!")
    # root.mainloop()


if __name__ == "__main__":
    main()

