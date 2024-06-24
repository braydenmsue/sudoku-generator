import tkinter as tk

class Cell:
    def __init__(self, row: str, col: str):
        self.value = 0
        self.revealed = False
        self.row = row
        self.col = col

    def set_cell_value(self, val):
        self.value = val

class Board:
    def __init__(self):
        # self.game = {''}
        pass

    def create_puzzle(self):
        board = []
        rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

        for row in rows:
            result = []
            for col in cols:
                result.append(Cell(row, col))
            board.append(result)

        return board

def main():

    b = Board()
    game = b.create_puzzle()

    for row in game:
        for cell in row:
            print(cell.value, end=' ')
        print()
    # root = tk.Tk()
    # root.title("SUDOKU!")
    # root.mainloop()


if __name__ == "__main__":
    main()

