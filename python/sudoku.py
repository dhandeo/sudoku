

class Sudoku(object):
    def __init__(self, board):
        self.board = board

    def isBoardFull(self):
        full = True
        for row in self.board:
            for num in row:
                if num == 0:
                    full = False
                    break

        return full

    def Possibilities(self, row, col):
        possi = []
        if self.board[row][col] != 0:
            return possi

        return possi

    def __getitem__(self, index):
        return self.board[index]


def test_full():
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
        ]
    assert(Sudoku(board).isBoardFull() == False)

    board = [
        [1, 2, 3, 4],
        [3, 4, 1, 2],
        [2, 3, 4, 1],
        [4, 1, 2, 3]
        ]
    assert(Sudoku(board).isBoardFull() == True)

    board = [
        [1, 2, 3, 4],
        [3, 4, 1, 2],
        [2, 3, 4, 1],
        [4, 0, 2, 3]
        ]
    s = Sudoku(board)
    assert(s.isBoardFull() == False)
    print s[0]
    print s[2][2]

test_full()
