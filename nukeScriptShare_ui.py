# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nukeScriptShare_ui.ui'
#
# Created: Wed Mar 31 18:04:34 2021
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_NukeScriptShare(object):
    def setupUi(self, NukeScriptShare):
        NukeScriptShare.setObjectName("NukeScriptShare")
        NukeScriptShare.resize(656, 708)
        self.centralwidget = QtWidgets.QWidget(NukeScriptShare)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Favourites = QtWidgets.QTabWidget(self.centralwidget)
        self.Favourites.setObjectName("Favourites")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 133, 133, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_3.addLayout(self.verticalLayout, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Pastebutton = QtWidgets.QPushButton(self.tab)
        self.Pastebutton.setObjectName("Pastebutton")
        self.horizontalLayout_3.addWidget(self.Pastebutton)
        self.Refreshbutton = QtWidgets.QPushButton(self.tab)
        self.Refreshbutton.setObjectName("Refreshbutton")
        self.horizontalLayout_3.addWidget(self.Refreshbutton)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 8, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ReceivedList = QtWidgets.QTableWidget(self.tab)
        self.ReceivedList.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ReceivedList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ReceivedList.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed)
        self.ReceivedList.setDragEnabled(True)
        self.ReceivedList.setDragDropOverwriteMode(True)
        self.ReceivedList.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.ReceivedList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ReceivedList.setShowGrid(False)
        self.ReceivedList.setGridStyle(QtCore.Qt.SolidLine)
        self.ReceivedList.setObjectName("ReceivedList")
        self.ReceivedList.setColumnCount(4)
        self.ReceivedList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ReceivedList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReceivedList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReceivedList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReceivedList.setHorizontalHeaderItem(3, item)
        self.ReceivedList.horizontalHeader().setVisible(True)
        self.ReceivedList.horizontalHeader().setHighlightSections(False)
        self.ReceivedList.verticalHeader().setVisible(False)
        self.ReceivedList.verticalHeader().setHighlightSections(False)
        self.horizontalLayout_2.addWidget(self.ReceivedList)
        self.SentList = QtWidgets.QTableWidget(self.tab)
        self.SentList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.SentList.setShowGrid(False)
        self.SentList.setGridStyle(QtCore.Qt.SolidLine)
        self.SentList.setObjectName("SentList")
        self.SentList.setColumnCount(4)
        self.SentList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.SentList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SentList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.SentList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.SentList.setHorizontalHeaderItem(3, item)
        self.SentList.horizontalHeader().setVisible(True)
        self.SentList.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.SentList)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SenderName = QtWidgets.QComboBox(self.tab)
        self.SenderName.setObjectName("SenderName")
        self.horizontalLayout.addWidget(self.SenderName)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ShareButton = QtWidgets.QPushButton(self.tab)
        self.ShareButton.setObjectName("ShareButton")
        self.horizontalLayout.addWidget(self.ShareButton)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Receivedlabel = QtWidgets.QLabel(self.tab)
        self.Receivedlabel.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.Receivedlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.Receivedlabel.setObjectName("Receivedlabel")
        self.horizontalLayout_5.addWidget(self.Receivedlabel)
        self.Sentlabel_2 = QtWidgets.QLabel(self.tab)
        self.Sentlabel_2.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.Sentlabel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Sentlabel_2.setObjectName("Sentlabel_2")
        self.horizontalLayout_5.addWidget(self.Sentlabel_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.Favourites.addTab(self.tab, "")
        self.Favourites01 = QtWidgets.QWidget()
        self.Favourites01.setObjectName("Favourites01")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Favourites01)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.Favourites01)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 133, 133, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.Favourites01)
        self.label_3.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.Fav_Table = QtWidgets.QTableWidget(self.Favourites01)
        self.Fav_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Fav_Table.setTabKeyNavigation(True)
        self.Fav_Table.setObjectName("Fav_Table")
        self.Fav_Table.setColumnCount(4)
        self.Fav_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Fav_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Fav_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Fav_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Fav_Table.setHorizontalHeaderItem(3, item)
        self.Fav_Table.horizontalHeader().setVisible(False)
        self.Fav_Table.horizontalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_2.addWidget(self.Fav_Table)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Fav_Paste = QtWidgets.QPushButton(self.Favourites01)
        self.Fav_Paste.setObjectName("Fav_Paste")
        self.horizontalLayout_4.addWidget(self.Fav_Paste)
        self.Fav_delete = QtWidgets.QPushButton(self.Favourites01)
        self.Fav_delete.setObjectName("Fav_delete")
        self.horizontalLayout_4.addWidget(self.Fav_delete)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.Favourites.addTab(self.Favourites01, "")
        self.gridLayout_2.addWidget(self.Favourites, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        NukeScriptShare.setCentralWidget(self.centralwidget)

        self.retranslateUi(NukeScriptShare)
        self.Favourites.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NukeScriptShare)

    def retranslateUi(self, NukeScriptShare):
        NukeScriptShare.setWindowTitle(QtWidgets.QApplication.translate("NukeScriptShare", "NukeScriptShare", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("NukeScriptShare", "Caution :  Sent and received scripts are Storing in temporary Database,\n"
"                  So the scripts are Automatically delete after Two days,\n"
"                  If you want to store perminantly Right-click on the row and click on add to Favourites", None, -1))
        self.Pastebutton.setText(QtWidgets.QApplication.translate("NukeScriptShare", "Paste", None, -1))
        self.Refreshbutton.setText(QtWidgets.QApplication.translate("NukeScriptShare", "Refresh", None, -1))
        self.ReceivedList.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("NukeScriptShare", "Script-Name", None, -1))
        self.ReceivedList.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("NukeScriptShare", "Sender", None, -1))
        self.ReceivedList.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("NukeScriptShare", "Time", None, -1))
        self.ReceivedList.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("NukeScriptShare", "id", None, -1))
        self.SentList.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("NukeScriptShare", "Script-Name", None, -1))
        self.SentList.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("NukeScriptShare", "Sender", None, -1))
        self.SentList.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("NukeScriptShare", "Time", None, -1))
        self.SentList.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("NukeScriptShare", "id", None, -1))
        self.ShareButton.setText(QtWidgets.QApplication.translate("NukeScriptShare", "Share", None, -1))
        self.Receivedlabel.setText(QtWidgets.QApplication.translate("NukeScriptShare", "RECEIVED", None, -1))
        self.Sentlabel_2.setText(QtWidgets.QApplication.translate("NukeScriptShare", "SENT", None, -1))
        self.Favourites.setTabText(self.Favourites.indexOf(self.tab), QtWidgets.QApplication.translate("NukeScriptShare", "Scripts", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("NukeScriptShare", "Favourite scripts are permanent scripts.\n"
" You can  DELETE the scripts from database by using the DELETE button in the below of panel", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("NukeScriptShare", "Favourites List", None, -1))
        self.Fav_Table.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("NukeScriptShare", "Script-Name", None, -1))
        self.Fav_Table.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("NukeScriptShare", "Sender", None, -1))
        self.Fav_Table.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("NukeScriptShare", "Time", None, -1))
        self.Fav_Table.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("NukeScriptShare", "id", None, -1))
        self.Fav_Paste.setText(QtWidgets.QApplication.translate("NukeScriptShare", "Paste", None, -1))
        self.Fav_delete.setText(QtWidgets.QApplication.translate("NukeScriptShare", "Delete", None, -1))
        self.Favourites.setTabText(self.Favourites.indexOf(self.Favourites01), QtWidgets.QApplication.translate("NukeScriptShare", "Favourites", None, -1))
