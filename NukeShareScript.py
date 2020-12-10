'''
SCRIPT AUTHOR : RAMESHKANNA

'''
import sys

sys.path.append('F:/PYTHON/Python calculator/venv/Lib/site-packages')


from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
#import nuke
import getpass,datetime,os
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


        artistNames = ['kanna','Bunny','kiran','Bujji','DELL']
        self.completer = QCompleter(artistNames)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.SenderName.addItems(artistNames)
        self.SenderName.setEditable(True)
        self.SenderName.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.SenderName.setInsertPolicy(QComboBox.NoInsert)
        self.SenderName.setCompleter(self.completer)


        self.ReceivedNameEdit.setText(username)

        self.SentNameEdit.setText(username)

        self.Pastebutton.clicked.connect(self.pasteScript)

        self.Refreshbutton.clicked.connect(self.refreshPanel)



    def insertData(self):


        NukeScriptName = nuke.root().knob('name').value()
        ScriptName = os.path.basename(NukeScriptName)
        if NukeScriptName == "":
            ScriptName = 'From - '+username
        else :
            pass
        self.Sending_To = self.SenderName.currentText()
        nuke.nodeCopy("%clipboard%")
        script = QApplication.clipboard().text()
        NukeData = {'ScriptName':ScriptName, 'Send_To': self.Sending_To,'SenderName':username,'date':date,'script':script}
        COLLECTION.insert_one(NukeData)



    def pasteScript(self):

        clipboardScript = COLLECTION.find_one({})

        PasteScript = clipboardScript['script']

        QApplication.clipboard().setText(PasteScript)

        nuke.nodePaste('%clipboard%')
        pass



    def receivedScriptList(self):

        nukedata = COLLECTION.find({'Send_To':username}).sort("date", -1)
        self.ReceivedList.setRowCount(nukedata.count())

        for i in enumerate(nukedata):
            Table_data = COLLECTION.find({'Send_To': username})
            print(Table_data)
            # ScriptName = Table_data['ScriptName']
            # SenderName = Table_data['SenderName']
            # Date = str(Table_data['date'])

            # self.ReceivedList.setItem(QTableWidgetItem(i,0,ScriptName))
            # self.ReceivedList.setItem(QTableWidgetItem(i,1,SenderName))
            # self.ReceivedList.setItem(QTableWidgetItem(i,2,Date))




    def refreshPanel(self):
        self.receivedScriptList()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())