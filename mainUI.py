# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShareScriptUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 848)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(550, 0))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.Share_Tab = QWidget()
        self.Share_Tab.setObjectName(u"Share_Tab")
        self.gridLayout_2 = QGridLayout(self.Share_Tab)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Share_Tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(500, 71))
        self.frame_2.setMaximumSize(QSize(16777215, 120))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.SenderName = QComboBox(self.frame_2)
        self.SenderName.setObjectName(u"SenderName")
        self.SenderName.setMinimumSize(QSize(253, 0))

        self.horizontalLayout_5.addWidget(self.SenderName)

        self.horizontalSpacer = QSpacerItem(19, 14, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.ShareButton = QPushButton(self.frame_2)
        self.ShareButton.setObjectName(u"ShareButton")
        self.ShareButton.setMinimumSize(QSize(111, 0))
        self.ShareButton.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_5.addWidget(self.ShareButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 51))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_13)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 9, 0, 9)
        self.label_2 = QLabel(self.frame_13)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 64))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(10)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(37, 37, 37);")
        self.label_2.setLineWidth(0)

        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_13)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(500, 400))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.frame_6.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.frame_7.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Receivedlabel = QLabel(self.frame_7)
        self.Receivedlabel.setObjectName(u"Receivedlabel")

        self.verticalLayout_2.addWidget(self.Receivedlabel)

        self.ReceivedList = QTableWidget(self.frame_7)
        self.ReceivedList.setObjectName(u"ReceivedList")
        self.ReceivedList.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ReceivedList.setAcceptDrops(False)
        self.ReceivedList.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.ReceivedList.setDragEnabled(True)
        self.ReceivedList.setDragDropOverwriteMode(True)
        self.ReceivedList.setDragDropMode(QAbstractItemView.DragOnly)
        self.ReceivedList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ReceivedList.setShowGrid(False)

        self.verticalLayout_2.addWidget(self.ReceivedList)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Sentlabel_2 = QLabel(self.frame_8)
        self.Sentlabel_2.setObjectName(u"Sentlabel_2")

        self.verticalLayout_3.addWidget(self.Sentlabel_2)

        self.SentList = QTableWidget(self.frame_8)
        self.SentList.setObjectName(u"SentList")
        self.SentList.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.SentList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.SentList.setShowGrid(False)

        self.verticalLayout_3.addWidget(self.SentList)


        self.horizontalLayout_3.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(500, 85))
        self.frame_4.setMaximumSize(QSize(16777215, 120))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Pastebutton = QPushButton(self.frame_4)
        self.Pastebutton.setObjectName(u"Pastebutton")

        self.horizontalLayout_4.addWidget(self.Pastebutton)

        self.Refreshbutton = QPushButton(self.frame_4)
        self.Refreshbutton.setObjectName(u"Refreshbutton")

        self.horizontalLayout_4.addWidget(self.Refreshbutton)


        self.verticalLayout.addWidget(self.frame_4)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Share_Tab, "")
        self.Fav_tab = QWidget()
        self.Fav_tab.setObjectName(u"Fav_tab")
        self.gridLayout_3 = QGridLayout(self.Fav_tab)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.Fav_tab)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 100))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_12)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_12)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(37, 37, 37);")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_11)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Fav_Table = QTableWidget(self.frame_11)
        self.Fav_Table.setObjectName(u"Fav_Table")
        font2 = QFont()
        font2.setPointSize(10)
        self.Fav_Table.setFont(font2)
        self.Fav_Table.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.Fav_Table.setShowGrid(False)

        self.gridLayout_4.addWidget(self.Fav_Table, 1, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_11)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 100))
        self.frame_10.setMaximumSize(QSize(16777215, 100))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Fav_Paste = QPushButton(self.frame_10)
        self.Fav_Paste.setObjectName(u"Fav_Paste")

        self.horizontalLayout_6.addWidget(self.Fav_Paste)

        self.Fav_delete = QPushButton(self.frame_10)
        self.Fav_delete.setObjectName(u"Fav_delete")

        self.horizontalLayout_6.addWidget(self.Fav_delete)


        self.gridLayout_4.addWidget(self.frame_10, 2, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_11)


        self.gridLayout_3.addWidget(self.frame_9, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Fav_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ShareButton.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Caution :  Sent and received scripts are Storing in temporary Database,\n"
"                  So the scripts are Automatically delete after Two days, \n"
"                  If you want to store perminantly Right-click on the row and click on add to Favourites", None))
        self.Receivedlabel.setText(QCoreApplication.translate("MainWindow", u"RECEIVED", None))
        self.Sentlabel_2.setText(QCoreApplication.translate("MainWindow", u"SENT RECENTLY", None))
        self.Pastebutton.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.Refreshbutton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Share_Tab), QCoreApplication.translate("MainWindow", u"Script-Share", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Favourite scripts are permanent scripts.\n"
" You can  DELETE the scripts from database by using the DELETE button in the below of panel", None))
        self.Fav_Paste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.Fav_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Fav_tab), QCoreApplication.translate("MainWindow", u"Favourites", None))
    # retranslateUi

