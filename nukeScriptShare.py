import nuke
import os
import datetime
import getpass
from bson import ObjectId
from pymongo import MongoClient


from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from nukeScriptShare_ui import Ui_NukeScriptShare


class NukeScriptShare(QMainWindow, Ui_NukeScriptShare):
    def __init__(self):
        super(NukeScriptShare, self).__init__()
        self.mongo = MongoClient("localhost", 27017)
        self.nuke_script_db = self.mongo["nuke_script_share"]
        self.nuke_script_collection = self.nuke_script_db["nuke_scripts"]
        self.username = getpass.getuser()
        self.now = datetime.datetime.now()
        self.setupUi(self)
        self.rl = None
        self.create_user()
        self.add_user_names_combo_box()
        self.connect_ui()
        self.auto_delete()
        self.received_script_list()
        self.sent_recent_list()
        self.favourites_list()
        self.show()

    def connect_ui(self):
        """
        Connect the signals to custom functions
        """
        self.ShareButton.clicked.connect(self.insert_data)
        self.ReceivedList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ReceivedList.verticalHeader().hide()
        self.ReceivedList.hideColumn(3)
        self.ReceivedList.itemClicked.connect(self.clicked_received_list)
        self.ReceivedList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ReceivedList.customContextMenuRequested.connect(self.add_context_menu)
        self.SentList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SentList.hideColumn(3)
        self.SentList.verticalHeader().hide()
        self.SentList.itemClicked.connect(self.clicked_sent_list)
        self.Fav_Table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Fav_Table.hideColumn(2)
        self.Fav_Paste.clicked.connect(self.paste_fav)
        self.Fav_delete.clicked.connect(self.delete_data)
        self.Pastebutton.clicked.connect(self.paste_script)
        self.Refreshbutton.clicked.connect(self.refresh_app)

    def add_user_names_combo_box(self):
        """
        Adding artist names in combobox
        """
        all_names = set()
        for i in self.nuke_script_collection.find():
            all_names.add(i['user'])
        artist_names = ["ramesh", "james", "tom"]
        all_names.update(set(artist_names))
        completer = QCompleter(list(all_names))
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.SenderName.addItems(list(all_names))
        self.SenderName.setEditable(True)
        self.SenderName.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.SenderName.setCompleter(completer)
        self.SenderName.setInsertPolicy(QComboBox.NoInsert)

    def create_user(self):
        """
        Creates user data in mongodb
        """
        find_user = self.nuke_script_collection.find_one({'user': self.username})
        if not find_user:
            self.nuke_script_collection.insert_one({'user': self.username,
                                                    'Sent': [],
                                                    'Received': [],
                                                    'Favs': []
                                                    })

    def insert_data(self):
        """
        Adding the sent nuke scripts in mongodb
        """
        end_user = self.SenderName.currentText()
        find_user = self.nuke_script_collection.find_one({'user': self.username})
        if not find_user:
            self.nuke_script_collection.insert_one({'user': end_user,
                                                    'Sent': [],
                                                    'Received': [],
                                                    'Favs': []
                                                    })
        nuke_script_name = nuke.root().knob('name').value()
        script_name = os.path.basename(nuke_script_name)
        if nuke_script_name == "":
            nuke.message("Save the WorkFile before sharing")
        else:
            sending_to = self.SenderName.currentText()
            nuke.nodeCopy("%clipboard%")
            script = QApplication.clipboard().text()
            var = self.nuke_script_collection.find_one({'user': self.username})
            sent_len = len(var['Sent']) - 1
            sent_len = 1 + sent_len
            self.nuke_script_collection.update_one({'user': self.username},
                                                   {'$set': {'Sent.{}'.format(sent_len):
                                                                 {'Send-To': sending_to,
                                                                  'ScriptName': script_name,
                                                                  'script': script,
                                                                  'date': self.now,
                                                                  '_id': ObjectId()
                                                                  }
                                                             }
                                                    }
                                                   )
            var = self.nuke_script_collection.find_one({'user': sending_to})
            received_len = len(var['Received']) - 1
            received_len = 1 + received_len
            self.nuke_script_collection.update_one({'user': sending_to},
                                                   {'$set': {'Received.{}'.format(received_len):
                                                                 {'SenderName': self.username,
                                                                  'ScriptName': script_name,
                                                                  'script': script,
                                                                  'date': self.now,
                                                                  '_id': ObjectId()
                                                                  }
                                                             }
                                                    }
                                                   )
        self.refresh_app()

    def received_script_list(self):
        """
        Displays received list of nuke scripts
        """
        nuke_data = self.nuke_script_collection.find_one({'user': self.username})
        received_data = nuke_data['Received']
        rec_len = len(received_data)
        self.ReceivedList.setRowCount(rec_len)
        self.ReceivedList.setColumnCount(4)
        for index, received_list in enumerate(reversed(received_data)):
            script_name = received_list['ScriptName']
            sender_name = received_list['SenderName']
            time = self.time_difference(received_list['date'])
            id = str(received_list['_id'])
            self.ReceivedList.setItem(index, 0, QTableWidgetItem(script_name))
            self.ReceivedList.setItem(index, 1, QTableWidgetItem(sender_name))
            self.ReceivedList.setItem(index, 2, QTableWidgetItem(time))
            self.ReceivedList.setItem(index, 3, QTableWidgetItem(id))

    def sent_recent_list(self):
        """
        Displays sent list of nuke scripts
        """
        nuke_data = self.nuke_script_collection.find_one({'user': self.username})
        sent_data = nuke_data['Sent']
        sent_len = len(sent_data)
        self.SentList.setRowCount(sent_len)
        self.SentList.setColumnCount(4)
        for index, sent_list in enumerate(reversed(sent_data)):
            script_name = sent_list['ScriptName']
            send_to = sent_list['Send-To']
            time = self.time_difference(sent_list['date'])
            id = str(sent_list['_id'])
            self.SentList.setItem(index, 0, QTableWidgetItem(script_name))
            self.SentList.setItem(index, 1, QTableWidgetItem(send_to))
            self.SentList.setItem(index, 2, QTableWidgetItem(time))
            self.SentList.setItem(index, 3, QTableWidgetItem(id))

    def favourites_list(self):
        """
        Displays nuke script of favourites list
        """
        nuke_data = self.nuke_script_collection.find_one({'user': self.username})
        self.Fav_Table.clear()
        fav_data = nuke_data['Favs']
        fav_len = len(fav_data)
        self.Fav_Table.setRowCount(fav_len)
        self.Fav_Table.setColumnCount(3)
        for index, fav_list in enumerate(reversed(fav_data)):
            script_name = fav_list['ScriptName']
            time = self.time_difference(fav_list['date'])
            id = str(fav_list['_id'])
            self.Fav_Table.setItem(index, 0, QTableWidgetItem(script_name))
            self.Fav_Table.setItem(index, 1, QTableWidgetItem(time))
            self.Fav_Table.setItem(index, 2, QTableWidgetItem(id))

    def clicked_received_list(self):
        """
        switch between send Table widget
        """
        self.SentList.clearSelection()
        self.rl = True

    def clicked_sent_list(self):
        """
        switch between received Table widget
        """
        self.ReceivedList.clearSelection()
        self.rl = False

    def paste_script(self):
        """
        Paste selected nuke script in nuke node graph
        """
        item = None
        if self.rl:
            row = self.ReceivedList.currentRow()
            current_id = self.ReceivedList.item(row, 3).text()
            all_items = self.nuke_script_collection.find_one({'user': self.username}, )
            paste_items = all_items['Received']
            for paste_item in paste_items:
                if current_id == str(paste_item['_id']):
                    item = paste_item['script']
        elif not self.rl:
            row = self.SentList.currentRow()
            current_id = self.SentList.item(row, 2).text()
            all_items = self.nuke_script_collection.find_one({'user': self.username}, )
            paste_items = all_items['Sent']
            for paste_item in paste_items:
                if current_id == str(paste_item['_id']):
                    item = paste_item['script']
        QApplication.clipboard().setText(item)
        nuke.nodePaste('%clipboard%')

    def paste_fav(self):
        """
        Paste selected favourite nuke script in nuke node graph
        """
        item = None
        row = self.Fav_Table.currentRow()
        current_id = self.Fav_Table.item(row, 2).text()
        all_items = self.nuke_script_collection.find_one({'user': self.username}, )
        fav_paste_items = all_items['Favs']
        for fav_paste_item in fav_paste_items:
            if current_id == str(fav_paste_item['_id']):
                item = fav_paste_item['script']
        QApplication.clipboard().setText(item)
        nuke.nodePaste('%clipboard%')

    @staticmethod
    def time_difference(date):
        """
        Changing date in to minutes and hours and seconds
        :param date: Date of selected nuke script
        :type date: datetime
        :return: Time in hours, minutes and seconds
        :rtype : Str
        """
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

    def add_context_menu(self, pos):
        """
        Adding context menu on table widget
        """
        context_menu = QMenu()
        add_fav = context_menu.addAction('Add Fav')
        add_del = context_menu.addAction('Delete')
        action = context_menu.exec_(self.ReceivedList.mapToGlobal(pos))
        if action == add_fav:
            self.add_favourites_table()
        elif action == add_del:
            self.delete_data()

    def add_favourites_table(self):
        """
        Selected nuke script sending to favourites list
        """
        selected_row = self.ReceivedList.currentRow()
        item = self.ReceivedList.item(selected_row, 3).text()
        rec_list = self.nuke_script_collection.find_one({'user': self.username})
        rec_list = rec_list['Received']
        for rec_item in rec_list:
            if rec_item['_id'] == ObjectId(item):
                add_fav = rec_item
        items_list = self.nuke_script_collection.find_one({'user': self.username})
        fav_len = len(items_list['Favs']) - 1
        fav_len = 1 + fav_len
        self.nuke_script_collection.update_one({'user': self.username},
                                               {'$set': {'Favs.{}'.format(fav_len): add_fav}})
        self.refresh_app()

    def auto_delete(self):
        """
        Auto deletes after two days from sent date
        """
        all_items = self.nuke_script_collection.find({})
        for index, items in enumerate(all_items):
            for item in items['Sent']:
                document_date = item['date']
                difference = self.now - document_date
                date = int(difference.days)
                if date >= 2:
                    self.nuke_script_collection.update_many({}, {'$pull': {'Sent': item}})

            for item in items['Received']:
                document_date = item['date']
                difference = self.now - document_date
                date = int(difference.days)
                if date >= 2:
                    self.nuke_script_collection.update_many({}, {'$pull': {'Received': item}})

    def delete_data(self):
        """
        Delete the selected favourites list
        """
        try:
            selected_row = self.Fav_Table.currentRow()
            item = self.Fav_Table.item(selected_row, 2).text()
            del_key = 'Favs'
        except:
            selected_row = self.ReceivedList.currentRow()
            item = self.ReceivedList.item(selected_row, 3).text()
            del_key = 'Received'
        collect_doc = self.nuke_script_collection.find_one({'user': self.username})
        for item_doc in collect_doc[del_key]:
            id = item_doc['_id']
            if id == ObjectId(item):
                self.nuke_script_collection.update_one({'user': self.username}, {'$pull': {del_key: item_doc}})
        self.refresh_app()

    def refresh_app(self):
        """
        Refresh the app

        """
        self.received_script_list()
        self.sent_recent_list()
        self.favourites_list()


def main():
    """
    Main function
    """
    main.window = NukeScriptShare()
