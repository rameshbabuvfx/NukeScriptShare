import sys
import nuke
import getpass
import datetime
import os
import pymongo
from bson import ObjectId
from mainUI import Ui_MainWindow
sys.path.append('F:/PYTHON/Python calculator/venv/Lib/site-packages')


from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

SERVER = pymongo.MongoClient('localhost', 27017)
DB = SERVER['NukeShare']
COLLECTION = DB['NukeData']
now = datetime.datetime.now()
username = getpass.getuser()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.create_user()
        self.auto_delete()
        # self.userList()
        self.received_script_list()
        self.sent_recent_list()
        self.favourites_list()
        self.show()
        self.ShareButton.clicked.connect(self.insert_data)
        self.artistNames = ['Alex', 'Jack', 'HP', 'DELL', 'Ramesh']
        self.completer = QCompleter(self.artistNames)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.SenderName.addItems(self.artistNames)
        self.SenderName.setEditable(True)
        self.SenderName.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.SenderName.setInsertPolicy(QComboBox.NoInsert)
        self.SenderName.setCompleter(self.completer)

        self.ReceivedList.setHorizontalHeaderLabels(['Script-Name', 'Sender', 'Time   '])
        self.ReceivedList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ReceivedList.hideColumn(3)
        self.ReceivedList.itemClicked.connect(self.clicked_received_list)
        self.ReceivedList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ReceivedList.customContextMenuRequested.connect(self.add_favourites)

        self.SentList.setHorizontalHeaderLabels(['Script-Name', 'Sent-To', 'Time   '])
        self.SentList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SentList.hideColumn(3)
        self.SentList.itemClicked.connect(self.clicked_sent_list)

        self.Fav_Table.setHorizontalHeaderLabels(['Script-Name', 'Time  '])
        self.Fav_Table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Fav_Table.hideColumn(2)

        self.Fav_Paste.clicked.connect(self.paste_fav)
        self.Fav_delete.clicked.connect(self.delete_fav)
        self.Pastebutton.clicked.connect(self.paste_script)
        self.Refreshbutton.clicked.connect(self.refresh_app)

    def clicked_received_list(self):
        self.SentList.clearSelection()
        self.rl = True

    def clicked_sent_list(self):
        self.ReceivedList.clearSelection()
        self.rl = False

    # def userList(self):
    #
    #     self.artistNames=[]
    #     list = COLLECTION.find({})
    #     for i in list:
    #         users = i['user']
    #         self.artistNames.append(users)

    @staticmethod
    def create_user():
        finduser = COLLECTION.find_one({'user': username})
        if not finduser:
            COLLECTION.insert_one({'user': username, 'Sent': [], 'Received': [], 'Favs': []})

    def insert_data(self):
        nuke_script_name = nuke.root().knob('name').value()
        script_name = os.path.basename(nuke_script_name)
        if nuke_script_name == "":
            nuke.message("Save the WorkFile before sharing")
        else:
            sending_to = self.SenderName.currentText()
            nuke.nodeCopy("%clipboard%")
            script = QApplication.clipboard().text()
            finduser = COLLECTION.find_one({'user': sending_to})
            if not finduser:
                COLLECTION.insert_one({'user': sending_to, 'Sent': [], 'Received': [], 'Favs': []})
            var = COLLECTION.find_one({'user': username})
            sentlen = len(var['Sent']) - 1
            sentlen = 1 + sentlen
            COLLECTION.update_one({'user': username}, {'$set': {
                'Sent.{}'.format(sentlen): {'Send-To': sending_to,
                                            'ScriptName': script_name, 'script':
                                                script, 'date': now, '_id': ObjectId()}}})
            var = COLLECTION.find_one({'user': sending_to})
            receivedlen = len(var['Received']) - 1
            receivedlen = 1 + receivedlen
            COLLECTION.update_one({'user': sending_to}, {'$set': {
                'Received.{}'.format(receivedlen): {
                    'SenderName': username, 'ScriptName': script_name,
                    'script': script, 'date': now, '_id': ObjectId()}}})
        self.refresh_app()

    def received_script_list(self):
        nukedata = COLLECTION.find_one({'user': username})
        reclen = len(nukedata['Received'])
        self.ReceivedList.setRowCount(reclen)
        self.ReceivedList.setColumnCount(4)
        for x, i in enumerate(nukedata['Received']):
            script_name = i['ScriptName']
            sender_name = i['SenderName']
            time = self.time_difference(i['date'])
            id = str(i['_id'])
            self.ReceivedList.setItem(x, 0, QTableWidgetItem(script_name))
            self.ReceivedList.setItem(x, 1, QTableWidgetItem(sender_name))
            self.ReceivedList.setItem(x, 2, QTableWidgetItem(time))
            self.ReceivedList.setItem(x, 3, QTableWidgetItem(id))

    def sent_recent_list(self):
        nukedata = COLLECTION.find_one({'user': username})
        sentlen = len(nukedata['Sent'])
        self.SentList.setRowCount(sentlen)
        self.SentList.setColumnCount(4)

        for x, i in enumerate(nukedata['Sent']):
            script_name = i['ScriptName']
            send_to = i['Send-To']
            time = self.time_difference(i['date'])
            id = str(i['_id'])
            self.SentList.setItem(x, 0, QTableWidgetItem(script_name))
            self.SentList.setItem(x, 1, QTableWidgetItem(send_to))
            self.SentList.setItem(x, 2, QTableWidgetItem(time))
            self.SentList.setItem(x, 3, QTableWidgetItem(id))

    def favourites_list(self):
        nukedata = COLLECTION.find_one({'user': username})
        sentlen = len(nukedata['Favs'])
        self.Fav_Table.setRowCount(sentlen)
        self.Fav_Table.setColumnCount(3)

        for x, i in enumerate(nukedata['Favs']):
            script_name = i['ScriptName']
            time = self.time_difference(i['date'])
            id = str(i['_id'])
            self.Fav_Table.setItem(x, 0, QTableWidgetItem(script_name))
            self.Fav_Table.setItem(x, 1, QTableWidgetItem(time))
            self.Fav_Table.setItem(x, 2, QTableWidgetItem(id))

    def paste_script(self):
        item = None
        if self.rl:
            row = self.ReceivedList.currentRow()
            currentid = self.ReceivedList.item(row, 3).text()
            all_items = COLLECTION.find_one({'user': username}, )
            var = all_items['Received']
            for i in var:
                if currentid == str(i['_id']):
                    item = i['script']
        elif not self.rl:
            row = self.SentList.currentRow()
            currentid = self.SentList.item(row, 2).text()
            all_items = COLLECTION.find_one({'user': username}, )
            var = all_items['Sent']
            for i in var:
                if currentid == str(i['_id']):
                    item = i['script']
        QApplication.clipboard().setText(item)
        nuke.nodePaste('%clipboard%')

    def paste_fav(self):
        item = None
        row = self.Fav_Table.currentRow()
        current_id = self.Fav_Table.item(row, 2).text()
        print(current_id)
        all_items = COLLECTION.find_one({'user': username}, )
        var = all_items['Favs']
        for i in var:
            if current_id == str(i['_id']):
                item = i['script']
        QApplication.clipboard().setText(item)
        nuke.nodePaste('%clipboard%')

    @staticmethod
    def time_difference(date):
        delta = datetime.datetime.today() - date
        if delta.days:
            return "%s day(s)" % delta.days
        seconds = delta.seconds
        if seconds < 60:
            return "A few seconds ago"
        elif seconds < 3600:
            return "%s minute(s) ago" % int(seconds / 60)
        elif seconds < 86400:
            return "%s hours(s) ago" % int(seconds / 3600)

    def add_favourites(self, pos):
        add_fav = None
        menu = QMenu()
        fav = menu.addAction('add fav')
        action = menu.exec_(self.ReceivedList.mapToGlobal(pos))
        selected_row = self.ReceivedList.currentRow()
        item = self.ReceivedList.item(selected_row, 3).text()
        rec_list = COLLECTION.find_one({'user': username})
        rec_list = rec_list['Received']
        for i in rec_list:
            if i['_id'] == ObjectId(item):
                add_fav = i
        items_list = COLLECTION.find_one({'user': username})
        favlen = len(items_list['Favs']) - 1
        favlen = 1 + favlen
        COLLECTION.update_one({'user': username}, {'$set': {'Favs.{}'.format(favlen): add_fav}})
        self.refresh_app()

    @staticmethod
    def auto_delete():
        item = COLLECTION.find({})
        for x, i in enumerate(item):
            for n in i['Sent']:
                document_date = n['date']
                diffence = datetime.datetime.now() - document_date
                date = int(diffence.days)
                if date >= 2:
                    id = n['_id']
                    if id:
                        COLLECTION.update_one({}, {'$pull': {'Sent': n}})

            for n in i['Received']:
                document_date = n['date']
                diffence = datetime.datetime.now() - document_date
                date = int(diffence.days)
                if date >= 2:
                    id = n['_id']
                    if id:
                        COLLECTION.update_one({}, {'$pull': {'Received': n}})

    def delete_fav(self):
        selected_row = self.Fav_Table.currentRow()
        item = self.Fav_Table.item(selected_row, 2).text()
        collectdoc = COLLECTION.find_one({'user': username})
        collectdoc = collectdoc['Favs']
        for i in collectdoc:
            id = i['_id']
            if id == ObjectId(item):
                COLLECTION.update_one({'user': username}, {'$pull': {'Favs': i}})
        self.refresh_app()

    def refresh_app(self):
        self.received_script_list()
        self.sent_recent_list()
        self.favourites_list()


def main():
    main.window = MainWindow()
