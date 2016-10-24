# Follows tutorial from tutorialspoint adapted for self study

import sys
from PyQt4 import QtGui

class Sudoku(QtGui.QWidget):
    def __init__(self):
        super(Sudoku,self).__init__()
        grid=QtGui.QGridLayout()
        self.setLayout(grid)
        positions = [(i,j) for i in range(10) for j in range(10)]
        for pos in positions:
            button = QtGui.QPushButton(" ")
            button.setMaximumWidth(30)
            button.setMaximumHeight(30)
            grid.addWidget(button, *pos)

        self.move(300,150)
        self.setWindowTitle('Sudoku Solver')
        self.show()

# def b1_clicked():
#    d = QDialog()
#    b1 = QPushButton("ok",d)
#    b1.move(50,50)
#    d.setWindowTitle("Button one")
#    d.setWindowModality(Qt.ApplicationModal)
#    d.exec_()
#
# def b2_clicked():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#
#    msg.setText("This is a message box")
#    msg.setInformativeText("This is additional information")
#    msg.setWindowTitle("Button two")
#    msg.setDetailedText("The details are as follows:")
#    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()

def msgbtn(i):
    print "value of pressed message box button:", i.text()

if __name__ == '__main__':
   app = QtGui.QApplication(sys.argv)
   sudoku = Sudoku()
   sys.exit(app.exec_())
