'''
SCRIPT AUTHOR : RAMESHKANNA

'''
import sys

sys.path.append('F:/PYTHON/Python calculator/venv/Lib/site-packages')


from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtUiTools import QUiLoader
#import nuke
import getpass,datetime,os
import pymongo
from bson import ObjectId
from mainUI import Ui_MainWindow


#####   Connecting Mongodb server    #######

SERVER = pymongo.MongoClient('localhost',27017)
DB = SERVER['NukeShare']
COLLECTION = DB['NukeData']

now = datetime.datetime.now()
username = getpass.getuser()



class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.receivedScriptList()
        self.sentRecent()
        self.favList()
        #self.autoDelete()
        self.show()

        self.ShareButton.clicked.connect(self.insertData)

        artistNames = ['Kanna','ramesh','bunny','alex','jack','DELL']
        self.completer = QCompleter(artistNames)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.SenderName.addItems(artistNames)
        self.SenderName.setEditable(True)
        self.SenderName.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.SenderName.setInsertPolicy(QComboBox.NoInsert)
        self.SenderName.setCompleter(self.completer)


        self.ReceivedList.setHorizontalHeaderLabels(['Script-Name', 'Sender', 'Time   '])
        self.ReceivedList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ReceivedList.hideColumn(3)
        self.ReceivedList.itemClicked.connect(self.clickedReceivedList)
        self.ReceivedList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ReceivedList.customContextMenuRequested.connect(self.addFavourites)

        self.SentList.setHorizontalHeaderLabels(['Script-Name', 'Sent-To', 'Time   '])
        self.SentList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SentList.hideColumn(3)
        self.SentList.itemClicked.connect(self.clickedSentList)
        self.SentList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.SentList.customContextMenuRequested.connect(self.addFavourites)

        self.Fav_Table.setHorizontalHeaderLabels(['Script-Name', 'Sent-To', 'Time   '])
        self.Fav_Table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Fav_Table.hideColumn(3)
        self.Fav_Table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Fav_Table.customContextMenuRequested.connect(self.removeFavourites)



        self.Fav_Paste.clicked.connect(self.pasteScript)

        self.Fav_delete.clicked.connect(self.deleteFav)

        self.ReceivedNameEdit.setText(username)

        self.SentNameEdit.setText(username)

        self.Pastebutton.clicked.connect(self.pasteScript)

        self.Refreshbutton.clicked.connect(self.refreshApp)


    def clickedReceivedList(self):

        self.SentList.clearSelection()
        self.RL = True


    def clickedSentList(self):

        self.ReceivedList.clearSelection()
        self.RL = False


    def insertData(self):

        NukeScriptName = nuke.root().knob('name').value()
        ScriptName = os.path.basename(NukeScriptName)
        if NukeScriptName == "":
            ScriptName = 'untitled'
        else :
            pass
        Sending_To = self.SenderName.currentText()
        nuke.nodeCopy("%clipboard%")
        script = QApplication.clipboard().text()

############# Inserting in Sent Username ############

        var = COLLECTION.find_one({'user': username})
        sentlen = len(var['Sent']) - 1
        sentlen = 1 + sentlen

        COLLECTION.update_one({'user':username},{'$set':{'Sent.{}'.format(sentlen):{'Send-To':Sending_To,'ScriptName':ScriptName,'script':script,'date':now,'_id':ObjectId()}}})

############### Inserting in Received Username ##########

        var = COLLECTION.find_one({'user': Sending_To})
        receivedlen = len(var['Received']) - 1
        receivedlen = 1 + receivedlen

        COLLECTION.update_one({'user':Sending_To},{'$set':{'Received.{}'.format(receivedlen):{'Sender-name':username,'ScriptName':ScriptName,'script':script,'date':now,'_id':ObjectId()}}})

        # NukeData = {'ScriptName':ScriptName, 'Send_To': self.Sending_To,'SenderName':username,'date':now,'script':script,'tmp':'Data'}
        # COLLECTION.insert_one(NukeData)


    def receivedScriptList(self):

        nukedata = COLLECTION.find({'Send_To':username}).sort('date',-1)
        self.ReceivedList.setRowCount(nukedata.count())
        self.ReceivedList.setColumnCount(4)

        for x,i in enumerate(nukedata):

            ScriptName = i['ScriptName']
            SenderName = i['SenderName']
            time = self.time_difference(i['date'])
            id = str(i['_id'])

            self.ReceivedList.setItem(x,0,QTableWidgetItem(ScriptName))
            self.ReceivedList.setItem(x,1,QTableWidgetItem(SenderName))
            self.ReceivedList.setItem(x,2,QTableWidgetItem(time))
            self.ReceivedList.setItem(x,3,QTableWidgetItem(id))


    def sentRecent(self):

        nukedata = COLLECTION.find({'SenderName':username}).sort('date',-1)
        self.SentList.setRowCount(nukedata.count())
        self.SentList.setColumnCount(4)

        for x,i in enumerate(nukedata):

            ScriptName = i['ScriptName']
            Send_To = 'Sent-'+i['Send_To']
            time = self.time_difference(i['date'])
            id = str(i['_id'])

            self.SentList.setItem(x,0,QTableWidgetItem(ScriptName))
            self.SentList.setItem(x,1,QTableWidgetItem(Send_To))
            self.SentList.setItem(x,2,QTableWidgetItem(time))
            self.SentList.setItem(x,3,QTableWidgetItem(id))


    def pasteScript(self):

        if self.RL == True:
            row = self.ReceivedList.currentRow()
            CurrentId = self.ReceivedList.item(row,3).text()
            allItems = COLLECTION.find({'SenderName':username})
            for x,i in enumerate(allItems):
                id = str(i['_id'])
                if id == str(CurrentId):
                    item = i['script']


        else:
            row = self.SentList.currentRow()
            CurrentId = self.SentList.item(row,3).text()
            allItems = COLLECTION.find({'SenderName':username})
            for x,i in enumerate(allItems):
                id = str(i['_id'])
                if id == str(CurrentId):
                    item = i['script']

        QApplication.clipboard().setText(item)
        nuke.nodePaste('%clipboard%')


    def time_difference(self, date):

        delta = datetime.datetime.today() - date
        if delta.days:
            return "%s day(s)" % delta.days
        seconds = delta.seconds
        if seconds < 60:
            return "A few seconds ago"
        elif seconds < 3600:
            return "%s minute(s) ago" % int(seconds/60)
        elif seconds < 86400:
            return "%s hours(s) ago" % int(seconds/3600)


    def autoDelete(self):


        item = COLLECTION.find({})
        for x,i in enumerate(item):
            Document_Date = i['date']
            diffence = datetime.datetime.now() - Document_Date
            date = int(diffence.days)

            if  date >= 2:
                COLLECTION.delete_one(i)


    def addFavourites(self,pos):

        menu = QMenu()
        fav = menu.addAction('add fav')
        action = menu.exec_(self.ReceivedList.mapToGlobal(pos))

        selectedRow = self.ReceivedList.currentRow()
        item = self.ReceivedList.item(selectedRow,3).text()
        collectId = COLLECTION.find_one({'_id':ObjectId(item)})
        COLLECTION.update_one({'_id':collectId['_id']},{'$set':{'favourites': 'True'}})


    def removeFavourites(self,pos):

        menu = QMenu()
        remfav = menu.addAction('RemoveFavourites')
        action = menu.exec_(self.Fav_Table.mapToGlobal(pos))

        Delrow = self.Fav_Table.currentRow()
        self.Fav_Table.removeRow(int(Delrow))
        self.favList()


    def favList(self):

        favItems = COLLECTION.find({'favourites':'True'}).sort('date',-1)

        self.Fav_Table.setRowCount(favItems.count())

        colcnt = self.Fav_Table.setColumnCount(4)

        for x,i in enumerate(favItems):

            ScriptName = i['ScriptName']
            Send_To = 'Sent-'+i['Send_To']
            time = self.time_difference(i['date'])
            id = str(i['_id'])

            self.Fav_Table.setItem(x,0,QTableWidgetItem(ScriptName))
            self.Fav_Table.setItem(x,1,QTableWidgetItem(Send_To))
            self.Fav_Table.setItem(x,2,QTableWidgetItem(time))
            self.Fav_Table.setItem(x,3,QTableWidgetItem(id))


    def deleteFav(self):

        selectedRow = self.Fav_Table.currentRow()
        item = self.Fav_Table.item(selectedRow,3).text()
        collectId = COLLECTION.find_one({'_id':ObjectId(item)})
        COLLECTION.delete_one(collectId)
        self.favList()


    def refreshApp(self):

        self.receivedScriptList()
        self.sentRecent()
        self.favList()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())