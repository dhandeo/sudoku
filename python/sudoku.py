

class Sudoku(object):
    def __init__(self, board):
        # Board is expected to be 9x9
        self.board = board
        self.nums = len(self.board[0])

    def isBoardFull(self):
        full = True
        for row in self.board:
            for num in row:
                if num == 0:
                    full = False
                    break

        return full

    def Possibilities(self, row, col):
        # expects board to be initialized correctly
        possi = set(range(1,self.nums+1))
        if self.board[row][col] != 0:
            raise Exception("location already filled")

        # Remove the items that are in that row
        # print self.board[row]
        # print self.board[row]
        # print possi
        for i in self.board[row]:
            if i != 0:
                possi.remove(i)

        # Remove the items that are in the col
        for arow in self.board:
            if arow[col] != 0:
                try:
                    possi.remove(arow[col])
                except KeyError:
                    pass

        # Remove the items that are in the submatrix
        for item in self.SubMatrixItems(row, col):
            if item != 0:
                try:
                    possi.remove(arow[col])
                except KeyError:
                    pass

        return possi

    def SubMatrixItems(self, row, col):
        # Returns all 9 elements of the submatrix based on row col
        items = []
        subr = row / 3
        subc = col / 3
        print subr, subc
        rows = range(subr * 3, subr*3 + 3)
        cols = range(subc * 3, subc*3 + 3)
        print rows, cols

        from operator import itemgetter
        for arow in itemgetter(*rows)(self.board):
            for item in itemgetter(*cols)(arow):
                items.append(item)
        return items

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
    assert(s[2][2] == 4)

def test_possi():
    board = [
        [1, 2, 3,    4, 5, 6,    7, 8, 9],
        [4, 0, 0,    0, 0, 0,    0, 0, 0],
        [0, 8, 0,    5, 6, 7,    0, 0, 0],

        [0, 0, 0,    0, 0, 0,    0, 0, 0],
        [9, 0, 0,    0, 0, 0,    0, 0, 0],
        [2, 0, 0,    0, 0, 0,    0, 0, 0],

        [0, 0, 0,    0, 0, 0,    0, 0, 0],
        [0, 0, 0,    0, 0, 0,    0, 0, 0],
        [0, 0, 0,    0, 0, 0,    0, 0, 0],
        ]
    s = Sudoku(board)
    assert(s.isBoardFull() == False)
    print s.Possibilities(2, 0)

test_full()
test_possi()
