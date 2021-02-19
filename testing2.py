# import pymongo
# import datetime
# from bson import ObjectId
#
# SERVER = pymongo.MongoClient('localhost',27017)
# DB = SERVER['NukeShare']
# COLLECTION = DB['NukeData']
#
#
# now = datetime.datetime.now()
#
# # data = COLLECTION.insert_one({'user':'LENOVO',
# #                               'sent':{'script1':{'script1':'nukescript1','script1Date':now},'script2':{'script2':'nukescript2','script2Date':now},'script3':{'script3':'nukescript3','script3Date':now}},
# #                               'Received':{'script1':'nukescript1','script2':'nukescript2','script3':'nukescript3'},
# #                               'Favourites':{'script1':'nukescript1','script2':'nukescript2','script3':'nukescript3'}
# #                               })
#
# data = COLLECTION.insert_one({'user': 'jack',
#         'Sent': [
#             {'name_script': 'nuke_1',
#              '_id': ObjectId(),
#              'date': now},
#             {'name_script': 'nuke_11',
#              '_id': ObjectId(),
#              'date': now},
#         ],
#         'Received': [
#             {'name_script': 'nuke_1',
#              '_id': ObjectId(),
#              'date': now},
#             {'name_script': 'nuke_11',
#              '_id': ObjectId(),
#              'date': now},
#         ],
#         'Favs': [
#             {'name_script': 'nuke_1',
#              '_id': ObjectId(),
#              'date': now},
#             {'name_script': 'nuke_11',
#              '_id': ObjectId(),
#              'date': now},
#         ],
#         })
#
#
#
# # k = COLLECTION.find_one({'user':'DELL'},)
# # var = k['Recieved']
# # id = '5fd9a570b7aa8b72bdd2c43b'
# # for i in var:
# #     if id == str(i['_id']):
# #         print(i['name_script'])
# #
#
#
#
# # k = 'kana2'
# # COLLECTION.update_one({'user':'alex'},{'$set':{'sent.{}'.format(k):{'test':'script3','time':'now','_id':ObjectId()}}})
#
# # COLLECTION.update_one({'user': 'jack'},{'$set':{'Sent.4':{'namescript':'abcdefg'}}})
#
#
#
# # find = COLLECTION.find_one({'user': 'DELL'})
# # var = find['Sent']
# # for i in var:
# #     print(i['date'])
#
#
#
# # dict = find['sent']['script2']
#
#
# # var = COLLECTION.find_one({'user':'jack'})
# # sentlen = len(var['Sent'])-1
# # sentlen = 1 + sentlen
# # print(sentlen)
# # # if sentlen == -1:
# # #     sentlen = 0
#
# #COLLECTION.update_one({'user':'jack'},{'$set':{'Sent.{}'.format(sentlen):{'script':'script1','date':now,'_id':ObjectId()}}})
#
#

import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("ShareScriptUI.ui", parentWidget=self)
        self.ui.ShareButton.clicked.connect(lambda : self.close())
        self.ui.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())