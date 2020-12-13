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
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_2 = QGridLayout(self.tab_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.tab_7)
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
        self.frame_2.setMinimumSize(QSize(500, 100))
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

        self.horizontalLayout_5.addWidget(self.ShareButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame_2)

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

        self.ReceivedNameEdit = QLineEdit(self.frame_7)
        self.ReceivedNameEdit.setObjectName(u"ReceivedNameEdit")

        self.verticalLayout_2.addWidget(self.ReceivedNameEdit)

        self.ReceivedList = QTableWidget(self.frame_7)
        self.ReceivedList.setObjectName(u"ReceivedList")
        self.ReceivedList.setAcceptDrops(False)
        self.ReceivedList.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.ReceivedList.setDragEnabled(False)
        self.ReceivedList.setDragDropOverwriteMode(True)
        self.ReceivedList.setDragDropMode(QAbstractItemView.NoDragDrop)
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

        self.SentNameEdit = QLineEdit(self.frame_8)
        self.SentNameEdit.setObjectName(u"SentNameEdit")

        self.verticalLayout_3.addWidget(self.SentNameEdit)

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

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tabWidget.addTab(self.tab_8, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ShareButton.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.Receivedlabel.setText(QCoreApplication.translate("MainWindow", u"RECEIVED", None))
        self.Sentlabel_2.setText(QCoreApplication.translate("MainWindow", u"SENT RECENTLY", None))
        self.Pastebutton.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.Refreshbutton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

