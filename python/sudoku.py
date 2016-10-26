from operator import itemgetter
import sys

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

    def Print(self):
        for row in self.board:
            for num in row:
                print num, ", ",
            print

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
                try:
                    possi.remove(i)
                except KeyError:
                    pass

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
                    possi.remove(item)
                except KeyError:
                    pass

        return list(possi)

    def SubMatrixItems(self, row, col):
        # Returns all 9 elements of the submatrix based on row col
        items = []
        subr = row / 3
        subc = col / 3
        # print subr, subc
        rows = range(subr * 3, subr*3 + 3)
        cols = range(subc * 3, subc*3 + 3)
        # print rows, cols

        for arow in itemgetter(*rows)(self.board):
            for item in itemgetter(*cols)(arow):
                items.append(item)
        return items

    def __getitem__(self, index):
        return self.board[index]

    def NextEmpty(self, i, j):
        # returns r, c for next empty cell or None, None otherwise
        if self.board[i][j] == 0:
            return i, j

        empty = False
        idx = i * 9 + j
        while idx < 9*9:
            r = idx / 9
            c = idx % 9
            # print i, j, r, c, self.board[r][c]
            if self.board[r][c] == 0:
                empty = True
                break
            idx = idx + 1
        if empty:
            return r, c
        else:
            return None, None

    def Solve(self, i=0, j=0):
        if self.isBoardFull():
            print "Board Full"
            return True

        # Find next empty:
        r, c = self.NextEmpty(i, j)

        if r is None:
            print "No empty at ", (i,j)
            return True

        possi = self.Possibilities(r,c)
        print "Checking at", (r,c), "with", possi

        if len(possi) == 0:
            # No possibilities for r, c
            print "Backtrack at ", (i, j)
            self.board[i][j] = 0
            self.Print()
            # sys.exit(0)
        else:
            for apos in possi:
                print "Trying ", apos, "at", (r, c), "for", (i, j)
                self.board[r][c] = apos
                if self.Solve(r, c):
                    return True
                else:
                    self.board[r][c] = 0

        print "Done with", (i, j)
        return False
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
        [7, 0, 1,    0, 0, 0,    4, 0, 0],
        [0, 0, 0,    0, 0, 0,    0, 1, 8],
        [0, 0, 0,    8, 5, 0,    0, 3, 0],

        [9, 0, 0,    0, 0, 2,    0, 6, 0],
        [0, 0, 0,    7, 4, 6,    0, 0, 0],
        [0, 6, 0,    9, 0, 0,    0, 0, 4],

        [0, 2, 0,    0, 6, 5,    0, 0, 0],
        [4, 9, 0,    0, 0, 0,    0, 0, 0],
        [0, 0, 3,    0, 0, 0,    8, 0, 1],
        ]

    s = Sudoku(board)
    assert(s.isBoardFull() == False)
    print s.Possibilities(2, 0)
    print s.Possibilities(2, 1)
    print s.Possibilities(1, 4)
    print s.Possibilities(1, 2)
    s.Solve()
    s.Print()

def test_nextempty():
    board = [
        [7, 0, 1,    0, 0, 0,    4, 0, 0],
        [0, 0, 0,    0, 0, 0,    0, 1, 8],
        [0, 0, 0,    0, 8, 5,    0, 3, 0],

        [9, 0, 0,    0, 0, 2,    0, 6, 0],
        [0, 0, 0,    7, 4, 6,    0, 0, 0],
        [0, 6, 0,    9, 0, 0,    0, 0, 4],

        [0, 2, 0,    0, 6, 5,    0, 0, 0],
        [4, 9, 0,    0, 0, 0,    0, 0, 0],
        [0, 0, 3,    0, 0, 0,    8, 0, 1],
        ]
    s = Sudoku(board)
    print 'Next Empty'
    print s.NextEmpty(0,0)
    print s.NextEmpty(2,4)
    print "----"


test_nextempty()
test_full()
test_possi()
