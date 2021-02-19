# import sys
# from PyQt5 import QtCore, QtWidgets
#
# class Dialog(QtWidgets.QDialog):
#     def __init__(self, parent=None):
#         super(Dialog, self).__init__()
#         self.listWidget = QtWidgets.QListWidget()
#         self.button = QtWidgets.QTableWidget()
#         self.listWidget.addItems('One Two Three'.split())
#         self.listWidget.installEventFilter(self)
#         self.button.installEventFilter(self)
#         layout = QtWidgets.QVBoxLayout(self)
#         layout.addWidget(self.listWidget)
#         layout.addWidget(self.button)
#
#     def eventFilter(self, source, event):
#         if (event.type() == QtCore.QEvent.ContextMenu and
#             source is self.button):
#             menu = QtWidgets.QMenu()
#             menu.addAction('Open Window')
#             if menu.exec_(event.globalPos()):
#
#                 #item = source.itemAt(event.pos())
#                 print('item')
#             return True
#         return super(Dialog, self).eventFilter(source, event)
#
#
# if __name__ == '__main__':
#
#     app = QtWidgets.QApplication(sys.argv)
#     window = Dialog()
#     window.setGeometry(600, 100, 300, 200)
#     window.show()
#     sys.exit(app.exec_())



# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
#
# app = QApplication([])
# listwidget = QListWidget()
# tableWidget = QTableWidget()
# tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
# layout = QVBoxLayout()
# layout.addWidget(listwidget)
# layout.addWidget(tableWidget)
#
#
# def openMenu(position):
#
#     menu = QMenu()
#
#     quitAction = menu.addAction("Quit")
#
#     action = menu.exec_(tableWidget.mapToGlobal(position))
#
#     if action == quitAction:
#         qApp.quit()
#
#
# tableWidget.customContextMenuRequested.connect(openMenu)
#
# listwidget.show()
#
# sys.exit(app.exec_())



import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class main(QWidget):
    def __init__(self):
        super(main, self).__init__()

        self.listWidget = QListWidget()
        self.tableWidget = QTableWidget()

        layout = QVBoxLayout(self)
        layout.addWidget(self.listWidget)
        layout.addWidget(self.tableWidget)

        self.listWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)

        quitAction = QAction("Quit", None)
        quitAction.triggered.connect(qApp.quit)
        self.tableWidget.addAction(quitAction)
        self.listWidget.addAction(quitAction)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec_())


def contextMenuEvent(self, event):
    self.menu = QtGui.QMenu(self)
    renameAction = QtGui.QAction('Rename', self)
    renameAction.triggered.connect(lambda: self.renameSlot(event))
    self.menu.addAction(renameAction)
    # add other required actions
    self.menu.popup(QtGui.QCursor.pos())
    ...

def renameSlot(self, event):
    print "renaming slot called"
    # get the selected row and column
    row = self.tableWidget.rowAt(event.pos().y())
    col = self.tableWidget.columnAt(event.pos().x())
    # get the selected cell
    cell = self.tableWidget.item(row, col)
    # get the text inside selected cell (if any)
    cellText = cell.text()
    # get the widget inside selected cell (if any)
    widget = self.tableWidget.cellWidget(row, col)
