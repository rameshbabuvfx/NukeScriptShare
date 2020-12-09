'''
SCRIPT AUTHOR : RAMESHKANNA

'''
import sys

sys.path.append('F:/PYTHON/Python calculator/venv/Lib/site-packages')


from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import nuke
import getpass,datetime
import pymongo
from mainUI import Ui_MainWindow



#####   Connecting Mongodb server    #######

SERVER = pymongo.MongoClient('localhost',27017)
DB = SERVER['NukeShare']
COLLECTION = DB['NukeData']

date = datetime.datetime.now()
username = getpass.getuser()



class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()


        ReceivedPath = 'F:/SERVER/projects/rrr/ramesh'
        SenderPath = 'F:/SERVER/projects/rrr/ramesh'


        self.ShareButton.clicked.connect(self.insertData)


        artistNames = ['kanna','Bunny','kiran','Bujji']
        self.completer = QCompleter(artistNames)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.SenderName.addItems(artistNames)
        self.SenderName.setEditable(True)
        self.SenderName.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.SenderName.setInsertPolicy(QComboBox.NoInsert)
        self.SenderName.setCompleter(self.completer)

        self.ReceivedNameEdit.setText(username)

        self.SentNameEdit.setText(username)

        # self.model = QFileSystemModel()
        # self.model.setRootPath(ReceivedPath)
        # self.ReceivedList.setModel(self.model)
        # self.ReceivedList.hideColumn(1)
        # self.ReceivedList.hideColumn(2)
        # self.ReceivedList.setRootIndex(self.model.index(ReceivedPath))
        # self.ReceivedList.alternatingRowColors()








        self.SentList.addItem("wkuniw")


        # self.SentList.setModel(self.model)
        # self.SentList.hideColumn(1)
        # self.SentList.hideColumn(2)
        # self.SentList.setRootIndex(self.model.index(ReceivedPath))
        # self.SentList.alternatingRowColors()


        self.Pastebutton.clicked.connect(self.pasteScript)

        self.Refreshbutton.clicked.connect(self.refreshPanel)



    def receivedScriptList(self):

        self.ReceivedList.setRowCount(10)
        self.ReceivedList.setColumnCount(3)


    def insertData(self):

        nuke.nodeCopy("%clipboard%")
        script = QApplication.clipboard().text()
        NukeData = {'ReceiverName':'','SenderName':username,'date':date,'script':script}
        COLLECTION.insert_one(NukeData)


    def pasteScript(self):

        clipboardScript = COLLECTION.find_one({})

        PasteScript = clipboardScript['script']

        QApplication.clipboard().setText(PasteScript)

        nuke.nodePaste('%clipboard%')


    def refreshPanel(self):
        self.update()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())